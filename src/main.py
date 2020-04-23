import sys
sys.path.append('..')
import utils.dbProvider as dbp
from controllers.block import Block
from controllers.mine import Mine


argv = sys.argv
commands = ["-lf", "--load-file", "-p", "--print"]
options = ["grade", "mass", "num_blocks"]
mineral_name = ""
block_model_name = ""
coordinate_x = ""
coordinate_y = ""
coordinate_z = ""
database = dbp.DBProvider()


if __name__ == "__main__":
    #Load blocks from a file giving the path into database
    if argv[1] == "-lf":
        block_model_name = argv[3]
        print("Insert the column names in the order of the file separated by one space")
        print("Some of this must be 'mass', 'x', 'y', 'z'")
        print("If this is not respected unexpected behaviour may occur.")
        column_raw = input()
        columns_names = column_raw.split(" ")       
        path = argv[2]                              
        collection = database.select_collection(block_model_name)
        mine = Mine(block_model_name)
        database.load_blocks(path,block_model_name,columns_names)
    #Number of mine blocks
    elif argv[2] == "num_blocks":
        mine = Mine(block_model_name)
        collection = database.select_collection(block_model_name)
        result = mine.mine_blocks(collection)
        print(result)
    #Mass value of block
    elif argv[5] == "mass":
        block_model_name = argv[1]
        coordinate_x = argv[2]
        coordinate_y = argv[3]
        coordinate_z = argv[4]
        mine = Mine(block_model_name)
        db = database.select_collection(block_model_name)
        block = mine.find_block(coordinate_x,coordinate_y,coordinate_z, db)
        if block:
            result = block.block_mass()
            print(result)
        else:
            print("Block not found")
    #Mass
    elif len(argv) == 6:
        block_model_name = argv[1]
        coordinate_x = argv[2]
        coordinate_y = argv[3]
        coordinate_z = argv[4]
        collection = database.select_collection(block_model_name)
        mine = Mine(block_model_name)
        block = mine.find_block(coordinate_x,coordinate_y,coordinate_z, collection)
        if argv[5] not in block.to_json().keys():
            print("Invalid attribute")
        else:
            print(block.block_attribute(argv[5]))

    elif argv[6] == "grade":
        block_model_name = argv[1]
        coordinate_x = argv[2]
        coordinate_y = argv[3]
        coordinate_z = argv[4]
        mineral_name = argv[5]
        mine = Mine(block_model_name)
        collection = database.select_collection(block_model_name)
        block = mine.find_block(coordinate_x,coordinate_y,coordinate_z, collection)
        result = block.block_grade(mineral_name)
        print(result)



