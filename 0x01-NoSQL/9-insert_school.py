#!/usr/bin/env python3
"""
Module for finding a document in a MongoDB collection.
"""

from pymongo import MongoClient


def find_document(database_name, collection_name, query):
    """
    Finds a document in a MongoDB collection.

    Args:
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        query (dict): The query to find the document.

    Returns:
        dict: The found document.
    """
    client = MongoClient()
    db = client[database_name]
    collection = db[collection_name]
    document = collection.find_one(query)
    client.close()
    return document


if __name__ == "__main__":
    query = {"name": "John Doe"}
    document = find_document("my_database", "users", query)
    print(f"Found document: {document}")
