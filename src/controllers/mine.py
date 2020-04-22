import pymongo
import json
from block import Block

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["maclaughlin"]
blocks = mydb["blocks"]


class Mine:
	def __init__(self, name):
        self.name = name

	def mine_blocks(self):
        return len(blocks.find({}))

    def find_block_in_db(self, x, y, z):
        block = blocks.find_one({"x":x, "y" : y, "z" : z})
        if (block != None):
            return block
        return False 

    def grade_in_percent(self, x, y, z, mineral):
        pass

    def mass_in_kg(self, x, y, z):
        pass
