#!/usr/bin/env python3
"""
Module for updating a document in a MongoDB collection.
"""

from pymongo import MongoClient


def update_document(database_name, collection_name, query, update):
    """
    Updates a document in a MongoDB collection.

    Args:
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        query (dict): The query to find the document.
        update (dict): The update to be applied to the document.

    Returns:
        int: The number of documents matched and modified.
    """
    client = MongoClient()
    db = client[database_name]
    collection = db[collection_name]
    result = collection.update_one(query, {"$set": update})
    client.close()
    return result.matched_count, result.modified_count


if __name__ == "__main__":
    query = {"name": "John Doe"}
    update = {"age": 31}
    matched, modified = update_document("my_database", "users", query, update)
    print(f"Matched {matched} document(s), modified {modified} document(s)")
