import pymongo
import sys

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

def load_blocks(path):
	blocks_file = open(path, "r")
	for block_row in blocks_file:
		block_data = block_row.strip().split(" ")
		block = Block(block_data[0], block_data[1], block_data[2], block_data[3], block_data[4], block_data[5], block_data[6], block_data[7])
		block.save_in_database()
		block.print_block()

def print_blocks():
	all_blocks = blocks.find({})
	for block_data in all_blocks:
		print(block_data)


# Commands

# -lf route_to_file
# -p print

argv = sys.argv


if __name__ == "__main__":
	print(argv)
	if argv[1] == "-lf":
		load_blocks(argv[2])
	elif argv[1] == "-p":
		print_blocks()
