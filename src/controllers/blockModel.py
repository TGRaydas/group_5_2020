import pymongo
import json
import sys
sys.path.append('..')
from controllers.block import Block
from utils.dbProvider import DBProvider
from pymongo.collation import Collation




class BlockModel:
    def __init__(self, name):
        self.name = name
        self.model_keys = None

    def blocks_count(self, blocks):
        blocks_count = blocks.count()
        return blocks_count

    def find_block(self, x, y, z, collection):
        block = collection.find_one({"x":x, "y" : y, "z" : z})
        if (block != None):
            return Block(block.keys(), block.values())
        return False 
    
    def reblock_model_attributes(self, collection):
        block = collection.find({})[0]
        self.model_keys = list(block.keys())[5:]
        return(list(block.keys())[5:])

    def reblock(self,collection, rx, ry, rz, attributes_types, mass_attribute):
        position = [-1,-1,-1]
        name_reblock_model = self.name + "_reblock"
        reblock_model = BlockModel(name_reblock_model)
        DBProvider().clear_collection(name_reblock_model)
        reblock_collection = DBProvider().select_collection(name_reblock_model)
        max_coords = self.max_coordenates(collection)
        x_max =int(max_coords[0])
        y_max =int(max_coords[1])
        z_max =int(max_coords[2])
        counter = 0
        for x in range(0, x_max, rx):
            position = [position[0]+ 1, -1, -1]
            for y in range(0, y_max, ry):
                position = [position[0], position[1] + 1, -1]
                for z in range(0, z_max, rz):
                    position = [position[0], position[1], position[2] + 1]
                    block = self.resize(collection, x, y, z, rx, ry, rz,position, counter, attributes_types, mass_attribute)
                    reblock_collection.insert_one(block)
                    counter += 1
        return reblock_collection

    def continue_attributes(self, blocks, attribute):
        value = 0
        if len(blocks) == 0:
            return value
        for block in blocks:
            if block != None:
                value += float(block[attribute])
        return value

    def proportinal_attributes(self, blocks, attribute, mass_attribute):
        value = 0
        mass = 0
        if len(blocks) == 0:
            return value
        for block in blocks:
            if block!= None:
                value += float(block[attribute]) * float(block[mass_attribute])
                mass += float(block[mass_attribute])
        return value/mass

    def categorical_attributes(self, blocks, attribute):
        attributes = []
        if len(blocks) == 0:
            return None
        for block in blocks:
            attributes.append(block[attribute])
        return max(set(attributes), key = attributes.count) 


    def max_coordenates(self, collection):
        max_x = collection.find({}).sort([('x',-1)]).collation(Collation(locale='fr_CA',numericOrdering= True))[0]["x"]
        max_y = collection.find({}).sort([("y",-1)]).collation(Collation(locale='fr_CA',numericOrdering= True))[0]["y"]
        max_z = collection.find({}).sort([("z",-1)]).collation(Collation(locale='fr_CA',numericOrdering= True))[0]["z"]
        return [max_x, max_y, max_z]


    def resize(self, collection, x_start, y_start, z_start ,reblock_x, reblock_y, reblock_z, position, counter, attributes_types, mass_attribute):
        all_blocks = [] # lista de blocks a combinar
        id_block = counter
        new_block = {"id": id_block, "x": position[0], "y": position[1], "z": position[2] }
        for x in range(x_start, x_start+reblock_x):
            for y in range(y_start, y_start+reblock_y):
                for z in range(z_start, z_start+reblock_z):
                    block = collection.find_one({"x":str(x), "y" : str(y), "z" : str(z)})
                    if block not in all_blocks and block != None:
                        all_blocks.append(block)
        offset = 5
        for attr_index in range(len(attributes_types)):
            attr = self.model_keys[attr_index]
            if attributes_types[attr_index] == "categorical":
                new_block[attr] = self.categorical_attributes(all_blocks, attr)
            elif attributes_types[attr_index] == "proportional":
                new_block[attr] = self.proportinal_attributes(all_blocks, attr, mass_attribute)
            elif attributes_types[attr_index] == "continue":
                new_block[attr] = self.continue_attributes(all_blocks, attr)

        #combinar los blocks 
        #tiene que retornar el block en json con los attr sumados
        return new_block





