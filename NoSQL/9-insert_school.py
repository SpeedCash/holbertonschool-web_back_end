#!/usr/bin/env python3
"""Module to insert a document into a MongoDB collection based on kwargs."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in the collection based on kwargs."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
