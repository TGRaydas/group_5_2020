import requests
import json
from unittest import TestCase
import unittest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import main
import requests
from block_test_cases_const import json_test

class TestEndpoints(TestCase):

    # endpoint tested: GET /api/block_models/
    # should return: OK
    def test_get_block_model_names(self):
        URL = "https://group-5-api.herokuapp.com/api/block_models/"
        response_json = requests.get(URL)
        response_dictionary = response_json.json()
        if len(response_dictionary) > 1:
            self.assertTrue(("name" in response_dictionary[0]), "The response of one item works.")
        elif len(response_dictionary) == 1:
            self.assertTrue(("name" in response_dictionary), "The response of one item works.")
    # endpoint tested: GET /api/block_models/<blockModel-Name>/blocks
    # should return: OK
    def test_get_blocks_of_model(self):
        URL = "https://group-5-api.herokuapp.com/api/block_models/test/blocks/"
        response_json = requests.get(URL)
        response_dictionary = response_json.json()
        self.assertEqual(json_test["id"], response_dictionary[2]["id"])

if __name__ == "__main__":
    unittest.main()
  
