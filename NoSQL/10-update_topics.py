#!/usr/bin/env python3
"""Module to update topics in a school document based on the school name."""


def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document based on the school name."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
