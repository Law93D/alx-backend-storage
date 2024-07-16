#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection
"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
    mongo_collection (pymongo.collection.Collection): pymongo collection object

    Returns:
    list: list of all documents in the collection
    """
    return list(mongo_collection.find())
