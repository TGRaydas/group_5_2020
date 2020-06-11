import pymongo
import sys
import json
sys.path.append('..')
from controllers.block import Block


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


