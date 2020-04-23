import pymongo
import json
from block import Block
from dbProvider import DBProvider


class Mine:
    def __init__(self, name):
        self.name = name

    def mine_blocks(self, blocks):
        return len(blocks.find({}))

    def find_block(self, x, y, z, blocks):
        block = blocks.find_one({"x":x, "y" : y, "z" : z})
        if (block != None):
            return Block(block.keys(), block.values())
        return False 

   
