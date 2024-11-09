#!/usr/bin/env python3
"""Task 11. Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Python function to return list of schools having specific topics"""

    return list(mongo_collection.find({'topics': topic}))
