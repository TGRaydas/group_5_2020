from controllers.block import Block

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
                     "z": 67,
					 "ton": 83.33, 
					 "au": 0.3
				} 