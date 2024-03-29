#!/usr/bin/env python3
"""Lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a given collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The collection
    to list documents from.

    Returns:
    list: A list of documents in the collection, or an empty list
    if the collection is empty.
    """
    documents = mongo_collection.find()
    return list(documents) if documents else []
