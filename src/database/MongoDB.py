import pymongo

_DB_USER_NAME = "dev"
_DB_USER_PASSWORD = "Em4SWKrUDatZ83b"

_PROJECT_NAME = 'smart_energy'
_DEFAULT_DATABASE = "EnergyConsumption"

_DB_HOST = f"smartenergycluster.jsanh.mongodb.net/{_DEFAULT_DATABASE}?retryWrites=true&w=majority"
_CLIENT_URL = f"mongodb+srv://{_DB_USER_NAME}:{_DB_USER_PASSWORD}@{_DB_HOST}"

# if __name__ == '__main__':
#     print(_CLIENT_URL)


class MongoDB:
    def __init__(self, collection) -> None:
        super().__init__()
        self.collection = pymongo.MongoClient(_CLIENT_URL)[_PROJECT_NAME][collection]  # FOR USE REMOTE
        # self.collection = pymongo.MongoClient()[_PROJECT_NAME][collection]  # FOR USE LOCAL

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

    def find_all(self, query={}, sort_field='_id'):
        return list(self.collection.find(query).sort([(sort_field, pymongo.ASCENDING)]))

    def last(self, limit=5):
        return list(self.collection.find().sort([('_id', pymongo.DESCENDING)]).limit(limit))

    def clear(self):
        self.collection.drop()

    def remove(self, query):
        self.collection.remove(query)

    def distinct(self, query):
        return self.collection.distinct(query)
