#!/usr/bin/env python3
"""
Module for inserting a document into a MongoDB collection.
"""

from pymongo import MongoClient


def insert_document(database_name, collection_name, document):
    """
    Inserts a document into a MongoDB collection.

    Args:
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        document (dict): The document to be inserted.

    Returns:
        str: The inserted document's _id.
    """
    client = MongoClient()
    db = client[database_name]
    collection = db[collection_name]
    result = collection.insert_one(document)
    client.close()
    return str(result.inserted_id)


if __name__ == "__main__":
    doc = {"name": "John Doe", "age": 30, "occupation": "Software Engineer"}
    inserted_id = insert_document("my_database", "users", doc)
    print(f"Inserted document ID: {inserted_id}")
