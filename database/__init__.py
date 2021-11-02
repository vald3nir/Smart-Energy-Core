# coding=utf-8
# !/usr/bin/python3

import pymongo

# DB CONFIG
_DATABASE = "smart_energy"
# DB_USER_NAME = "dev"
# DB_USER_PASSWORD = "njOcs9iCSBCO8Gro"
# DB_HOST = "realmcluster.ikdg6.mongodb.net"
#
# _USER_ID = f"{DB_USER_NAME}:{DB_USER_PASSWORD}@{DB_HOST}"
# _CLIENT_URL = f"mongodb+srv://{_USER_ID}/{_DATABASE}?retryWrites=true&w=majority"


class MongoDB:
    def __init__(self, collection, ) -> None:
        super().__init__()
        self.collection = pymongo.MongoClient()[_DATABASE][collection]

    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, new_value):
        self.collection.update_one(query, new_value, upsert=True)

    def insert_one(self, query):
        self.collection.insert_one(query)

    def aggregate(self, query):
        self.collection.aggregate(query)

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
