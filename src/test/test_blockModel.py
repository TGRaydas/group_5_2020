import sys
sys.path.append('..')
from controllers.block import Block
from controllers.blockModel import BlockModel
from unittest.mock import patch
from unittest import TestCase
import unittest
from io import StringIO
from utils.dbProvider import DBProvider

database = DBProvider()
collection = database.select_collection("test")
block_columns = ["id","x", "y","z", "ton", "au"]
block1_value = [4, 38, 286, 67, 20.83, 0.2]
block2_value = [5, 39, 286, 67, 83.33, 0.3]
block3_value = [0, 36, 286, 67, 20.83, 0.2]
block4_value = [1, 37, 286, 67, 83.33, 0.3]
test_block1 = Block(block_columns,block1_value)
test_block2 = Block(block_columns, block2_value)
test_block3 = Block(block_columns,block1_value)
test_block4 = Block(block_columns, block2_value)
test_block1.save_in_database(collection)
test_block2.save_in_database(collection)
test_block3.save_in_database(collection)
test_block4.save_in_database(collection)
test_block_model = BlockModel("test")



#Test Class BlockModel methods
class TestBlockModels(TestCase):
    #Method Tested: to_json
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_blocks_count(self):
        self.assertEqual(test_block_model.blocks_count(collection),4 )

    #Method Tested: save_in_database
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_find_block(self):
        block = collection.find_one({"x":38, "y" : 286, "z" : 67})
        test_block = Block(block.keys(), block.values())
        self.assertEqual(test_block.to_json()["id"], test_block_model.find_block(38,286,67, collection).to_json()["id"] )



if __name__ == "__main__":
    unittest.main()
    
