#!/bin/usr/env python3
"""Task: 8. List all documents in Python"""


def list_all(mongo_collection):
    """Function to list all documents in Mongo Collection

        :param mongo_collection:
    """

    if mongo_collection is not None:
        return list(mongo_collection.find())
    else:
        return []
