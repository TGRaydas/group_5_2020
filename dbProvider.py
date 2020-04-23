import pymongo
from block import Block


class DBProvider():
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mines"]
    
    def select_collection(self, block_model_name):
        collection = self.db[block_model_name] 
        return collection

def load_blocks(path, name_data_set, columns_names, database):
	blocks_file = open(path, "r")
	for block_row in blocks_file:
		block_data = block_row.strip().split(" ")
		block = Block(columns_names, block_data)
		block.save_in_database(database)
		block.print_block()
