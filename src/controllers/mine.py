import pymongo
import json
from block import Block
from dbProvider import DBProvider


class Mine:
	def __init__(self, name):
        self.name = name

	def mine_blocks(self):
        return len(blocks.find({}))

    def find_block(self, x, y, z):
        block = blocks.find_one({"x":x, "y" : y, "z" : z})
        if (block != None):
            return Block(block.keys(), block.values())
        return False 

    def grade_in_percent(self, x, y, z, mineral):
        pass

    def mass_in_kg(self, x, y, z, mass_column_name):
        block = self.find_block(self, x, y ,z)
        block.
        pass
