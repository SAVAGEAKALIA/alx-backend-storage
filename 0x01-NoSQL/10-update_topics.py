#!/usr/bin/env python3
"""Task 10. Change school topics"""


def update_topics(mongo_collection, name, topics):
    """Pyhton function to change school topics"""

    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
