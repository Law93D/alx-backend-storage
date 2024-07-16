#!/usr/bin/env python3
import pymongo

def list_all(mongo_collection):
    """Lists all documents in a collection"""
    return list(mongo_collection.find())

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    collection = client.database_name.collection_name
    docs = list_all(collection)
    for doc in docs:
        print(doc)
