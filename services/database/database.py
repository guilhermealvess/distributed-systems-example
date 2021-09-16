from pymongo import MongoClient



class Database:
    def __init__(self) -> None:
        client = MongoClient('mongodb://app:1997@localhost:27017')
        self.__database = client.gRPC

    def getCollection(self, collection:str):
        return self.__database[collection]

    def findAll(self, collection):
        col = self.getCollection(collection)
        return list(col.find({}))

    def findById(self, collection, id):
        col = self.getCollection(collection)
        return col.find_one({'_id': id})

    def insertMany(self, collection, data: list):
        col = self.getCollection(collection)
        col.insert_many(data)