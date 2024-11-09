#!/usr/bin/env python3
"""Task 9. Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """Python function that inserts new document based on Kwargs
        :param1 mongo_collection:
    """
    mongo_collection.insert_one({**kwargs})

    list_id = [mongo_collection.find_one({**kwargs})]
    for item in list_id:
        for key, value in item.items():
            if key == "_id":
                return value
