#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def log_stats():
    """Function to print stats about nginx logs."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    logs_count = nginx_collection.count_documents({})
    print(f"{logs_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"{method}: {count}")

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check} status checks")


if __name__ == "__main__":
    log_stats()
