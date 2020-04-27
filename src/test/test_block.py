import sys
sys.path.append('..')
from controllers.block import Block
from unittest.mock import patch
from unittest import TestCase
import unittest
from io import StringIO
from utils.dbProvider import DBProvider

database = DBProvider()
collection = database.select_collection("test")
block_columns = ["id","x", "y","z", "ton", "au"]
block1_value = [0, 36, 286, 67, 20.83, 0.2]
block2_value = [1, 37, 286, 67, 83.33, 0.3]
test_block1 = Block(block_columns,block1_value)
test_block2 = Block(block_columns, block2_value)
json_test = {
					"id": 0,
					 "x": 36, 
                     "y": 286,
					 "z": 67, 
					 "ton": 20.83, 
					 "au": 0.2
				} 
json_test_attr = {
					"id": 1,
					 "x": 37, 
                     "y": 286, 
					 "ton": 83.33, 
					 "au": 0.3
				} 



#Test Class Block methods
class TestBlocks(TestCase):
    #Method Tested: to_json
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_to_json(self):
        self.assertEqual(test_block1.to_json(),json_test )

    #Method Tested: save_in_database
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_save_in_database(self):
        test_block1.save_in_database(collection)
        block = collection.find_one({"x":test_block1.block_data[1],"y":test_block1.block_data[2],"z":test_block1.block_data[3]})
        self.assertTrue(block, "the Block is save in database")

    #Method Tested: print_block
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_print_block(self):
        output = StringIO()          
        sys.stdout = output                   
        test_block1.print_block()                                   
        sys.stdout = sys.__stdout__                   
        self.assertEqual(output.getvalue(), "{'id': 0, 'x': 36, 'y': 286, 'z': 67, 'ton': 20.83, 'au': 0.2}\n" )

    #Method Tested: block_attribute
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_block_attribute(self):
         json_without_attr = test_block2.block_attribute('z')
         self.assertEqual(json_without_attr, json_test_attr)

    #Method Tested: block_mass
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_block_mass(self):
        self.assertEqual(test_block2.block_mass('ton','2'),0.08333)
        self.assertEqual(test_block2.block_mass('ton','1'),83.33)
        self.assertEqual(test_block2.block_mass('tonn','1'), "The name of mass column was not valid (should be mass)")


    
    #Method Tested: block_grade
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_block_grade(self):
        self.assertEqual(test_block2.block_grade('au','ton','2','2'),0.360014400576023)
        self.assertEqual(test_block2.block_grade('au','ton','1','2'),0.000360014400576023)
        self.assertEqual(test_block2.block_grade('au','tonn','2','2'),False)
        self.assertEqual(test_block2.block_grade('au','ton','2','1'),test_block2.to_json()['au'])
        self.assertEqual(test_block2.block_grade('au','ton','2','3'), 360.01440057602304)




    #Method Tested: get_keys_values
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_get_key_values(self):
        self.assertEqual(test_block1.get_key_values(), block_columns)

   
        
    

if __name__ == "__main__":
    unittest.main()
    
