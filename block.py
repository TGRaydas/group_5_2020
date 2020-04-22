import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["maclaughlin"]
blocks = mydb["blocks"]


class Block:
	def __init__(self, _id, x, y, z, block_value, ton, destination, au):
		self._id = _id
		self.x = x
		self.y = y
		self.z = z
		self.block_value = block_value
		self.ton = ton
		self.destination = destination
		self.au = au
	def to_json(self):
		return(
				{
					"_id": self._id,
					 "x": self.x, "y": self.y,
					 "z": self.z, "block_value": self.block_value, 
					 "ton": self.ton, "destination": self.destination, 
					 "au": self.au
				}
			)
	def save_in_database(self):
		block = blocks.find_one({"_id":self._id})
		if block != None:
			return
		blocks.insert_one(self.to_json())
	def print_block(self):
		print(self.to_json())
	def find_block_in_db(self, x, y, z):
		block = blocks.find_one({"x":x, "y" : y, "z" : z})
        if (block != None):
            key_values = block.keys()
            #a block has been found and later to be returned, now we save into the object the json obtained
            attibutes = []
            for value in key_values:
                attibutes.append(block[value])
            return Block(*attributes)#* hace que un arreglo se vuelva var1, var2, sirve para que no se pase un arreglo, y pase cada variable
        return False 
    def number_of_blocks:
        return blocks.count()

    def block_mass(self, x, y, z):
        #find the block
        block = find_block_in_db(self, x, y, z)
        if (block):
            if not block["ton"]:
                return [False, "No value saved for block"]
            
            return [True, block["ton"]]
        return [False, "Block not found"]

    def block_grade(self, x, y, z, mineral):
        #find the block
        block = find_block_in_db(self, x, y, z)
        if (block):
            if not block[mineral]:
                return [False, "No value saved for block, try using the another abreviation for the mineral."]
            return [True, block["ton"]]
        return  [False, "Block not found"]

    def block_attribute(self, x, y, z, attribute):
        #find the block
        block = find_block_in_db(self, x, y, z)
        if (block):
            if not block[attribute]:
                return [False, "No value saved for block, try using another attribute."]
            return [True, block[attibute]]
        return  [False, "Block not found"]
