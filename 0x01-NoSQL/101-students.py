#!/usr/bin/env python3
"""Task 14: Top Students"""


def top_students(mongo_collection):
    """Python function to sort students by average score"""
    # average_score = list(mongo_collection.find())
    average_score = list(mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        # {
        #     "$project": {"average_score": 1}
        # },

        {"$sort": {"averageScore": -1}}
    ]))

    return average_score
