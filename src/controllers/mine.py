import pymongo
import json
import sys
sys.path.append('..')
from controllers.block import Block
from utils.dbProvider import DBProvider


class Mine:
    def __init__(self, name):
        self.name = name

    def mine_blocks(self, blocks):
        a = blocks.count()
        return a

    def find_block(self, x, y, z, blocks):
        block = blocks.find_one({"x":x, "y" : y, "z" : z})
        if (block != None):
            return Block(block.keys(), block.values())
        return False 

   
