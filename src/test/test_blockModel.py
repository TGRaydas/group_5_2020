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
block1_value = [4, 38, 28, 67, 20.83, 0.2]
block2_value = [5, 39, 28, 67, 83.33, 0.3]
block3_value = [0, 36, 28, 67, 20.83, 0.2]
block4_value = [1, 37, 28, 67, 83.33, 0.3]
test_block1 = Block(block_columns,block1_value)
test_block2 = Block(block_columns, block2_value)
test_block3 = Block(block_columns,block3_value)
test_block4 = Block(block_columns, block4_value)
test_block1.save_in_database(collection)
test_block2.save_in_database(collection)
test_block3.save_in_database(collection)
test_block4.save_in_database(collection)
test_block_model = BlockModel("test")
test_rx = 2
test_ry = 2
test_rz = 2
test_blocks = [test_block1, test_block2]


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
        block = collection.find_one({"x":38, "y" : 28, "z" : 67})
        test_block = Block(block.keys(), block.values())
        self.assertEqual(test_block.to_json()["id"], test_block_model.find_block(38,28,67, collection).to_json()["id"] )

    #Method Tested: max_coordinates
    #Context: passing test model blocks
    #should return ok
    def test_max_coordinates(self):
        new_coordinates = test_block_model.max_coordenates(collection)
        self.assertEqual(new_coordinates, [39, 28 ,67])

    def test_continue_attributes(self):
        attribute = "ton"
        bks = [test_block1.to_json(), test_block2.to_json()]
        new_value = test_block_model.continue_attributes(bks, attribute)
        self.assertEqual(new_value, 104.16)

    def test_categorical_attributes(self):
        attribute = "ton"
        bks = [test_block1.to_json(), test_block2.to_json()]
        new_value = test_block_model.categorical_attributes(bks, attribute)
        self.assertEqual(new_value, 83.33)

    def test_proportinal_attributes(self):
        attribute = "au"
        bks = [test_block1.to_json(), test_block2.to_json()]
        new_value = test_block_model.proportinal_attributes(bks, attribute, "ton")
        self.assertEqual(new_value, ((83.33*0.3 + 20.83*0.2)/104.16))

    def test_reblock(self):
        #return collection with the new block model, so block 0, 0, 0 must exist
        new_attribute = ["continue", "proportional"]
        new_collection = test_block_model.reblock(collection, test_rx, test_ry, test_rz, new_attribute, "ton")
        new_block = new_collection.find_one({"x": 0, "y" : 0, "z" : 0}) 
        self.assertTrue(bool(new_block))

if __name__ == "__main__":
    unittest.main()
    
