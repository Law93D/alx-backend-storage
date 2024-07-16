#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection.
"""

from pymongo import MongoClient


def list_all_documents(database_name, collection_name):
    """
    Lists all documents in a MongoDB collection.

    Args:
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.

    Returns:
        list: A list of all documents in the collection.
    """
    client = MongoClient()
    db = client[database_name]
    collection = db[collection_name]
    documents = list(collection.find())
    client.close()
    return documents


if __name__ == "__main__":
    documents = list_all_documents("my_database", "users")
    print(f"All documents: {documents}")
