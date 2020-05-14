from controllers.block_flyweight import BlockFlyweight

class BlockFlyweightFactory:
	def __init__(self):
		self.block_flyweight_map = {}
	def create_flyweight(self, block_columns, block_data):
		hash_map = hash((frozenset(block_columns), tuple(block_data)))
		if hash_map not in self.block_flyweight_map:
			self.block_flyweight_map[hash_map] = BlockFlyweight(block_columns, block_data)
		return self.block_flyweight_map[hash_map]