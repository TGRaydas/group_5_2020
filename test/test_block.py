import sys
sys.path.append('..')
from unittest.mock import patch
from unittest import TestCase
import unittest
from io import StringIO
from utils.dbProvider import DBProvider
from block_test_cases_const import block1_value, block2_value, test_block1, test_block2, json_test, json_test_attr, block_columns

database = DBProvider()
collection = database.select_collection("test")

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
        block = collection.find_one({"x": str(test_block1.flyweight.block_data[1]),"y": str(test_block1.flyweight.block_data[2]),"z": str(test_block1.flyweight.block_data[3])})
        self.assertTrue(block, "the Block is save in database")

    #Method Tested: print_block
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_print_block(self):
        output = StringIO()          
        sys.stdout = output                   
        test_block1.print_block()                                   
        sys.stdout = sys.__stdout__                   
        self.assertEqual(output.getvalue(), "{'id': '0', 'x': '36', 'y': '286', 'z': '67', 'ton': '20.83', 'au': '0.2'}\n" )

    #Method Tested: block_attribute
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_block_attribute(self):
         json_without_attr = test_block2.block_attribute('z')
         self.assertEqual(json_without_attr, json_test_attr)
    #Method Tested: block_mass
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_block_mass_case_ton(self):
        self.assertEqual(test_block2.block_mass('ton','2'),0.08333)
    def test_block_mass_case_kg(self):    
        self.assertEqual(test_block2.block_mass('ton','1'),'83.33')
    def test_block_mass_case_invalid_attr(self):    
        self.assertEqual(test_block2.block_mass('tonn','1'), "The name of mass column was not valid (should be mass)")


    
    #Method Tested: block_grade
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_block_grade_case_tons_with_tons_mineral_type(self):
        self.assertEqual(test_block2.block_grade('au','ton','2','2'),0.360014400576023)
    def test_block_grade_case_kg_with_tons_mineral_type(self):
        self.assertEqual(test_block2.block_grade('au','ton','1','2'),0.000360014400576023)
    def test_block_grade_case_invalid_attribute_mass(self):
        self.assertEqual(test_block2.block_grade('au','tonn','2','2'),False)
    def test_block_grade_case_tons_and_percents_mineral_type(self):
        self.assertEqual(test_block2.block_grade('au','ton','2','1'),test_block2.to_json()['au'])
    def test_block_grade_case_tons_with_kg_mineral_type(self):        
        self.assertEqual(test_block2.block_grade('au','ton','2','3'), 360.01440057602304)


    #Method Tested: get_keys_values
    #Context: Passing test model blocks
    #Expectation: Should return OK
    def test_get_key_values(self):
        self.assertEqual(test_block1.get_key_values(), block_columns)
    

if __name__ == "__main__":
    unittest.main()
    
