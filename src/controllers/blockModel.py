import pymongo
import json
import sys
sys.path.append('..')
from controllers.block import Block
from utils.dbProvider import DBProvider


class BlockModel:
    def __init__(self, name):
        self.name = name

    def mine_blocks(self, blocks):
        blocks_count = blocks.count()
        return blocks_count

    def find_block(self, x, y, z, collection):
        block = collection.find_one({"x":x, "y" : y, "z" : z})
        if (block != None):
            return Block(block.keys(), block.values())
        return False 
