#!/usr/bin/env python3
"""
Module for inserting a school document into a MongoDB collection
"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs

    Args:
    mongo_collection (pymongo.collection.Collection): pymongo collection object
    kwargs: key-value pairs for the document to be inserted

    Returns:
    pymongo.results.InsertOneResult: the inserted document's id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
