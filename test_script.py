from script import *
import unittest
from io import StringIO
import sys

test_block1 = Block(0, 36, 286, 67, -27, 20.83, 0, 0)
test_block2 = Block(1, 37, 286, 67, -117, 83.33, 0, 0)
json_test = {
					"_id": 0,
					 "x": 36, "y": 286,
					 "z": 67, "block_value": -27, 
					 "ton": 20.83, "destination": 0, 
					 "au": 0
				} 


class TestBlocks(unittest.TestCase):

    def test_to_json(self):
        self.assertEqual(test_block1.to_json(),json_test )

    def test_save_in_database(self):
        test_block1.save_in_database()
        block = blocks.find_one({"_id":test_block1._id})
        self.assertTrue(block)

    def test_print_block(self):
        output = StringIO()          
        sys.stdout = output                   
        test_block1.print_block()                                   
        sys.stdout = sys.__stdout__                   
        self.assertEqual(output.getvalue(), "{'_id': 0, 'x': 36, 'y': 286, 'z': 67, 'block_value': -27, 'ton': 20.83, 'destination': 0, 'au': 0}\n" )

        

if __name__ == "__main__":
    unittest.main()
    
