from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        school_collection = client.my_db.school
        schools = list_all(school_collection)
        for school in schools:
            print("[{}] {}".format(school.get('_id'), school.get('name')))
    except Exception as e:
        print(f"Error {e}")