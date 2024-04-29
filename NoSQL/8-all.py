#!/usr/bin/env python3
"""Module to list all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """List all documents in a given collection."""
    return list(mongo_collection.find())
