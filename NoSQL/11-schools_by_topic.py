#!/usr/bin/env python3
"""Module to find schools by a specific topic in MongoDB."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools that have a specific topic."""
    return list(mongo_collection.find({"topics": topic}))
