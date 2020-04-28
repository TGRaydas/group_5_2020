import pymongo
import json
import sys
sys.path.append('..')
from controllers.block import Block
from utils.dbProvider import DBProvider



class BlockModel:
    def __init__(self, name):
        self.name = name

    def blocks_count(self, blocks):
        blocks_count = blocks.count()
        return blocks_count

    def find_block(self, x, y, z, collection):
        block = collection.find_one({"x":x, "y" : y, "z" : z})
        if (block != None):
            return Block(block.keys(), block.values())
        return False 
    
    def reblock(self,collection, rx,ry,rz):
        position = [-1,-1,-1]
        name_reblock_model = self.name + "_reblock"
        reblock_model = BlockModel(name_reblock_model)
        reblock_collection = DBProvider.select_collection(name_reblock_model)
        max_coords = self.max_coordenates(collection)
        x_max =max_coords[0]
        y_max =max_coords[1]
        z_max =max_coords[2]
        for x in range(0, x_max, rx):
            position = [position[0]+ 1, position[1], position[2]]
            for y in range(0, y_max, ry):
                position = [position[0], position[1] + 1, position[2]]
                for z in range(0, z_max, rz):
                    position = [position[0], position[1], position[2] + 1]
                    block = resize(collection, x,y,z, rx, ry, rz,position)
                    reblock_collection.insert_one(block)

    
    def max_coordenates(self, collection):
        max_x = collection.find_one({}).sort({"x":-1})["x"]
        max_y = collection.find_one({}).sort({"y":-1})["y"]
        max_z = collection.find_one({}).sort({"z":-1})["z"]
        return [max_x, max_y, max_z]


def resize(collection, x_start, y_start, z_start ,reblock_x, reblock_y, reblock_z, position):
    l = []
    id_block = position[0] + position[1] + position[2]
    new_block = {"id": id_block, "x": position[0], "y": position[1], "z": position[2] }
    for x in range(x_start, x_start+reblock_x):
    	for y in range(y_start, y_start+reblock_y):
    		for z in range(z_start, z_start+reblock_z):
    			block = collection.find_one({"x":x, "y" : y, "z" : z})
    			if block not in l and block != None:
    				l.append(block)
    #combinar los blocks 
    #tiene que retornar el block en json
    return new_block




