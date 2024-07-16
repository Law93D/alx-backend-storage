#!/usr/bin/env python3
"""
Module for deleting a document from a MongoDB collection.
"""

from pymongo import MongoClient


def delete_document(database_name, collection_name, query):
    """
    Deletes a document from a MongoDB collection.

    Args:
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        query (dict): The query to find the document.

    Returns:
        int: The number of documents deleted.
    """
    client = MongoClient()
    db = client[database_name]
    collection = db[collection_name]
    result = collection.delete_one(query)
    client.close()
    return result.deleted_count


if __name__ == "__main__":
    query = {"name": "John Doe"}
    deleted_count = delete_document("my_database", "users", query)
    print(f"Deleted {deleted_count} document(s)")
