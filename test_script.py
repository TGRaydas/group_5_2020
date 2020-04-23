from block import Block
from unittest.mock import patch
from unittest import TestCase
import unittest
from io import StringIO
import sys
from dbProvider import DBProvider, load_blocks

database = DBProvider()
collection = database.select_collection("test")
block_columns = ["id","x", "y","z", "ton", "au"]
block1_value = [0, 36, 286, 67, 20.83, 0]
block2_value = [1, 37, 286, 67, 83.33, 1]
test_block1 = Block(block_columns,block1_value)
test_block2 = Block(block_columns, block2_value)
json_test = {
					"id": 0,
					 "x": 36, 
                     "y": 286,
					 "z": 67, 
					 "ton": 20.83, 
					 "au": 0
				} 

def get_input(text):
    return input(text)

class TestBlocks(TestCase):
   
    def test_to_json(self):
        self.assertEqual(test_block1.to_json(),json_test )

    def test_save_in_database(self):
        test_block1.save_in_database(collection)
        block = collection.find_one({"x":test_block1.block_data[1],"y":test_block1.block_data[2],"z":test_block1.block_data[3]})
        self.assertTrue(block, "the Block is save in database")

    def test_print_block(self):
        output = StringIO()          
        sys.stdout = output                   
        test_block1.print_block()                                   
        sys.stdout = sys.__stdout__                   
        self.assertEqual(output.getvalue(), "{'id': 0, 'x': 36, 'y': 286, 'z': 67, 'ton': 20.83, 'au': 0}\n" )

    def test_block_attribute(self):
         attribute = test_block2.block_attribute('x')
         self.assertEqual(attribute, ("x",37))

    @patch('builtins.input', side_effect=['ton','2'])
    def test_block_mass(self, mock_input):
        self.assertEqual(test_block2.block_mass(),0.08333)



        
        
       


if __name__ == "__main__":
    unittest.main()
    
