import pymongo
import sys
import json
sys.path.append('..')
from controllers.block import Block
from bson.json_util import dumps


class DBProvider():
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://190.162.2.76:27017/")
        self.db = self.client["mines"]
        self.collection = None
    
    def select_collection(self, block_model_name):
        collection = self.db[block_model_name] 
        self.collection = collection
        return collection

    def load_blocks(self, data, name_data_set, columns_names):
        blocks_file = data
        for block_row in blocks_file:
            block_data = block_row.strip().split(" ")
            block = Block(columns_names, block_data)
            block.save_in_database(self.collection)
            block.print_block()

    def clear_collection(self, block_model_name):
        collection = self.db[block_model_name] 
        collection.drop()
        self.collection = self.db[block_model_name] 
        return collection

    def get_blocks_names(self):
        collections = []
        for collection in self.db.list_collection_names():
            collections.append({"name": collection})
        return collections

    def get_span_id(self):
        print("aqui", self.db["span"].count())
        if self.db["span"].count() == 0:
           span_id = 0
        else:
            span = self.db["span"].find().sort([("_id",-1)]).limit(1)
            span_id = list(span)[0]["span_id"]
        return span_id


    def create_span_id(self):
        id = self.get_span_id()
        collection = self.db["span"]
        span_id = id +1
        span = collection.insert({"span_id": span_id})
        return span_id



