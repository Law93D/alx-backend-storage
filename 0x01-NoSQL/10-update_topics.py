#!/usr/bin/env python3
"""
Module for updating the topics of a school document in a MongoDB collection
"""

from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Args:
    mongo_collection (pymongo.collection.Collection): pymongo collection object
    name (str): the school name to update
    topics (list): list of topics approached in the school

    Returns:
    pymongo.results.UpdateResult: result of the update operation
    """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
