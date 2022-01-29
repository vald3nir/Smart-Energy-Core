# coding=utf-8
# !/usr/bin/python3

import pymongo

# DB CONFIG
_DB_USER_NAME = "dev"
_DB_USER_PASSWORD = "Em4SWKrUDatZ83b"
_DEFAULT_DATABASE = "EnergyConsumption"
_DB_HOST = f"smartenergycluster.jsanh.mongodb.net/{_DEFAULT_DATABASE}?retryWrites=true&w=majority"
_CLIENT_URL = f"mongodb+srv://{_DB_USER_NAME}:{_DB_USER_PASSWORD}@{_DB_HOST}"

print("MongoDB:", _CLIENT_URL)

class _MongoDBRemote:
    def __init__(self, database, collection) -> None:
        super().__init__()      
        self.collection = pymongo.MongoClient(_CLIENT_URL)[database][collection]

    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, new_value):
        self.collection.update_one(query, new_value, upsert=True)

    def insert_one(self, document):
        self.collection.insert_one(document=document)

    def insert_many(self, documents):
        self.collection.insert_many(documents=documents)

    def aggregate(self, pipeline):
        return self.collection.aggregate(pipeline=pipeline)

    def find_all(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    def last(self, limit=5):
        return list(self.collection.find().sort([('_id', pymongo.DESCENDING)]).limit(limit))

    def clear(self):
        self.collection.drop()

    def remove(self, query):
        self.collection.remove(query)


'''
To int databse local:
docker run -v ~/docker --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=dev -e MONGO_INITDB_ROOT_PASSWORD=1721 mongo
'''


class _MongoDBLocal(_MongoDBRemote):

    def __init__(self, database, collection) -> None:
        super().__init__(database, collection)

        # DB CONFIG
        _DB_USER_NAME = "dev"
        _DB_USER_PASSWORD = "1721"
        _DB_HOST = "127.0.0.1"
        _CLIENT_URL = f"mongodb://{_DB_USER_NAME}:{_DB_USER_PASSWORD}@{_DB_HOST}"

        self.collection = pymongo.MongoClient(_CLIENT_URL)[database][collection]


# Class used in the project
class MongoDB(_MongoDBRemote):
    def __init__(self, collection) -> None:
        super().__init__('smart_energy', collection)
