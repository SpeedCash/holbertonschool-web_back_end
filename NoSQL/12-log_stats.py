#!/usr/bin/env python3

import pymongo


def connect_to_mongo(
    host="localhost",
    port=27017,
    database="logs",
    collection="nginx"
):
    """Connects to the MongoDB database and collection.

    Args:
        host: The hostname of the MongoDB server (default: localhost).
        port: The port number of the MongoDB server (default: 27017).
        database: The name of the database to connect to (default: logs).
        collection: The name of the collection to connect to (default: nginx).

    Returns:
        A pymongo.collection.Collection object representing the connection.
    """
    client = pymongo.MongoClient(host, port)
    return client[database][collection]


def count_documents(collection, query=None):
    """Counts the number of documents in the collection matching a query.

    Args:
        collection: A pymongo.collection.Collection object.
        query: A dictionary representing the query filter (default: None).

    Returns:
        The number of documents matching the query.
    """
    return collection.count_documents(query)
    if query else collection.count_documents()


def get_method_counts(collection):
    """Counts the number of documents for each HTTP method.

    Args:
        collection: A pymongo.collection.Collection object.

    Returns:
        A dictionary mapping HTTP methods ("GET", "POST",
        "PUT", "PATCH", "DELETE") to their counts.
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: count_documents(collection, {"method": method})
        for method in methods
    }
    return method_counts


def get_status_check_count(collection):
    """Counts the number of documents with method=GET and path=/status.

    Args:
        collection: A pymongo.collection.Collection object.

    Returns:
        The number of documents matching the criteria.
    """
    status_check_query = {"method": "GET", "path": "/status"}
    status_checks = count_documents(collection, status_check_query)
    return status_checks


def main():
    """Connects to MongoDB, retrieves and displays statistics."""
    collection = connect_to_mongo()
    total_logs = count_documents(collection)

    print(f"{total_logs} logs")

    method_counts = get_method_counts(collection)
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    status_checks = get_status_check_count(collection)
    print(f"{status_checks} status check")


if __name__ == "__main__":
    main()
