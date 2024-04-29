#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def log_stats():
    """Print statistics about nginx logs from MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    logs_count = nginx_collection.count_documents({})
    print(f"{logs_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    # Splitting the statement to adhere to the line length limit
    status_filter = {"method": "GET", "path": "/status"}
    status_check = nginx_collection.count_documents(status_filter)
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
