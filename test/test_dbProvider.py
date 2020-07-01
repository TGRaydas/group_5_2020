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
collection = database.select_collection("test_prec")
database.clear_collection("test_prec")
prec = ["0 1 1", "4 2 5 0", "1 0", "5 0"]
test_block_model = BlockModel("test_prec")




# Test Class dbProvider methods
class TestDbProvider(TestCase):
    # Method Tested: load_prec
    # Context: Passing test model blocks
    # Expectation: Should return OK
    def test_load_prec(self):
        self.assertEqual(database.load_prec(prec, "test"), True )


if __name__ == "__main__":
    unittest.main()
    
