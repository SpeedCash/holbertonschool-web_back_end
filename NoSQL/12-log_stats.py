#!/usr/bin/env python3

import pymongo


def connect_to_mongo(host="localhost", port=27017,
                     database="logs", collection="nginx", **kwargs):
    """Connects to MongoDB."""
    return pymongo.MongoClient(host, port, **kwargs)[database][collection]


def get_method_counts(collection):
    """Counts documents for each HTTP method."""
    pipeline = [{"$group": {"_id": "$method", "count": {"$sum": 1}}}]
    return {doc['_id']: doc['count'] for doc in collection.aggregate(pipeline)}


def get_status_check_count(collection):
    """Counts method=GET and path=/status."""
    return collection.count_documents({"method": "GET", "path": "/status"})


def main():
    """Connects to MongoDB, retrieves and displays statistics."""
    collection = connect_to_mongo()
    total_logs = collection.estimated_document_count()

    print(f"{total_logs} logs")

    method_counts = get_method_counts(collection)
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    status_checks = get_status_check_count(collection)
    print(f"{status_checks} status check")


if __name__ == "__main__":
    main()
