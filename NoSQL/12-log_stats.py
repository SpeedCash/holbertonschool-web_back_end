#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def log_stats():
    """Print statistics about nginx logs from MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Count total logs
    logs_count = nginx_collection.count_documents({})
    print(f"{logs_count} logs")

    # Count logs per method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    # Count logs where method=GET and path=/status
    status_filter = {"method": "GET", "path": "/status"}
    status_count = nginx_collection.count_documents(status_filter)
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()
