import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from controllers.block import Block
from controllers.blockModel import BlockModel
from unittest.mock import patch
from unittest import TestCase
import unittest
from io import StringIO
from utils.dbProvider import DBProvider

database = DBProvider()
collection = database.select_collection("test")
database.clear_collection("test")
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



# Test Class BlockModel methods
class TestBlockModels(TestCase):
    # Method Tested: to_json
    # Context: Passing test model blocks
    # Expectation: Should return OK
    # def test_blocks_count(self):
    #     self.assertEqual(test_block_model.blocks_count(collection),4 )

    # Method Tested: save_in_database
    # Context: Passing test model blocks
    # Expectation: Should return OK
    def test_find_block_valid(self):
        block = collection.find_one({"x":'38', "y" : '28', "z" : '67'})
        test_block = Block(block.keys(), block.values())
        self.assertEqual(test_block.to_json()["id"], test_block_model.find_block('38', '28', '67', collection).to_json()["id"] )
    
    def test_find_block_invalid(self):
        self.assertEqual(test_block_model.find_block('96', '28', '67', collection), False )
    # Method Tested: max_coordinates
    # Context: passing test model blocks
    # should return ok
    def test_max_coordinates(self):
        new_coordinates = test_block_model.max_coordinates(collection)
        self.assertEqual(new_coordinates, ['39', '28' , '67'])

    # Method Tested: continue_attributes
    # Context: passing test model blocks
    # should return ok
    def test_continue_attributes(self):
        attribute = "ton"
        bks = [test_block1.to_json(), test_block2.to_json()]
        new_value = test_block_model.continues_attributes(bks, attribute)
        self.assertEqual(new_value, 104.16)

    # Method Tested: categorical_attributes
    # Context: passing test model blocks
    # should return ok
    def test_categorical_attributes(self):
        attribute = "ton"
        bks = [test_block1.to_json(), test_block2.to_json()]
        new_value = test_block_model.categorical_attributes(bks, attribute)
        self.assertEqual(new_value, '83.33')

    # Method Tested: proporcional_attributes
    # Context: passing test model blocks
    # should return ok
    def test_proportinal_attributes(self):
        attribute = "au"
        bks = [test_block1.to_json(), test_block2.to_json()]
        new_value = test_block_model.proportinal_attributes(bks, attribute, "ton")
        self.assertEqual(new_value, ((83.33*0.3 + 20.83*0.2)/104.16))

    # Method Tested: reblock
    # Context: passing test model blocks
    # should return ok
    # proving first and last block of a new model block
    # def test_reblock(self):
    #     new_attribute = ["con", "prop"]
    #     new_collection = test_block_model.reblock(collection, test_rx, test_ry, test_rz, new_attribute, "ton")
    #     first_block = new_collection.find_one({"x": 0, "y" : 0, "z" : 0}) 
    #     last_block = new_collection.find_one({"x": 3, "y" : 2, "z" : 6}) 
    #     self.assertTrue(first_block, last_block)
    
    # Method Tested: create_reblocked_block
    # Context: passing test model blocks
    # should return ok
    # risize return a json of a new block with new parameters
    # def test_create_reblocked_block(self):
    #     new_attribute = ["con", "prop"]
    #     test_resize = test_block_model.create_reblocked_block(collection,30,20,60,10,10,10,[3,2,6],83,new_attribute,"ton")
    #     self.assertEqual(test_resize, {'id': 83, 'x': 3, 'y': 2, 'z': 6, 'ton': '208.32', 'au': '0.2800019201228879'})


if __name__ == "__main__":
    unittest.main()
    
