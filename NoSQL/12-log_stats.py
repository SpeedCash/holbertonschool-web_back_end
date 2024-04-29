#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields random numbers.
"""

from pymongo import MongoClient


def log_stats():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    nginx_collection = db['nginx']

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_checks = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")


if __name__ == "__main__":
    log_stats()
