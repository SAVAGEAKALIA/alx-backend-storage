#!/usr/bin/env python3
"""Task: 12 Log stats Question"""

from pymongo import MongoClient


# def print_ngx_logs(collection):
#     """Python function to Print Nginx Logs"""
#     try:
#         view = collection.find_one()
#         # print(view)
#         # logs_count = collection.find().count()
#         logs_count = collection.count_documents({})
#         print(f'{logs_count} logs')
#
#         get_count = 0
#         post_count = 0
#         put_count = 0
#         patch_count = 0
#         delete_count = 0
#         def_count = 0
#         view_all = list(collection.find())
#         # print(view_all)
#
#         for documents in range(len(view_all)):
#             for key, value in view_all[documents].items():
#                 if key == 'method' and value in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
#                     if value == 'GET':
#                         get_count += 1
#                     elif value == 'POST':
#                         post_count += 1
#                     elif value == 'PUT':
#                         put_count += 1
#                     elif value == 'PATCH':
#                         patch_count += 1
#                     else:
#                         delete_count += 1
#                 if value == 'GET' and view_all[documents]['path'] == '/status':
#                     def_count += 1
#
#         print(f'Methods: \n '
#               f'\t method GET: {get_count}\n'
#               f'\t method POST: {post_count}\n'
#               f'\t method PUT: {put_count}\n'
#               f'\t method PATCH: {patch_count}\n'
#               f'\t method DELETE: {delete_count}')
#
#         print(f'{def_count} status check')
#
#     except Exception as e:
#         print(f'Error: {e}')

def print_ngx_logs(collection):
    """Python function to Print Nginx Logs"""
    try:
        # Total logs count
        logs_count = collection.count_documents({})
        print(f'{logs_count} logs')

        # Aggregation for method counts
        methods_count = collection.aggregate([
            {"$group": {
                "_id": "$method",
                "count": {"$sum": 1}
            }},
            {"$match": {"_id": {"$in": ["GET", "POST", "PUT", "PATCH", "DELETE"]}}}
        ])

        # Store method counts in a dictionary
        method_counts = {method: 0 for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]}
        for method in methods_count:
            method_counts[method["_id"]] = method["count"]

        # Print method counts
        print(f'Methods:')
        for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
            print(f'\tmethod {method}: {method_counts[method]}')

        # GET /status count
        get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
        print(f'{get_status_count} status check')

    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    """If run directly on Terminal"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    # nginx_collection = client.logs.nginx
    # collections = logs_db.list_collection_names()
    # print(collections)
    nginx_collection = logs_db.nginx
    # print_ngx_logs(logs_db.nginx)
    print_ngx_logs(nginx_collection)
