from controllers.block import Block
from controllers.blockModel import BlockModel
from utils.dbProvider import DBProvider
database = DBProvider()
collection = database.select_collection("test")
block_columns = ["id","x", "y","z", "ton", "au"]
block1_value = ['4', '38', '28', '67', 20.83, 0.2]
block2_value = ['5', '39', '28', '67', 83.33, 0.3]
block3_value = ['0', '36', '28', '67', 20.83, 0.2]
block4_value = ['1', '37', '28', '67', 83.33, 0.3]
test_block1 = Block(block_columns,block1_value)
test_block2 = Block(block_columns, block2_value)
test_block3 = Block(block_columns,block3_value)
test_block4 = Block(block_columns, block4_value)
test_block1.save_in_database(collection)
test_block2.save_in_database(collection)
test_block3.save_in_database(collection)
test_block4.save_in_database(collection)
test_block_model = BlockModel("test")
test_rx = 10
test_ry = 10
test_rz = 10