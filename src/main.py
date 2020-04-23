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
    print(argv)
    if len(argv) >= 2:
        block_model_name = argv[2]
        mine = Mine(block_model_name)
        db = database.select_collection(block_model_name)
        if argv[1] == "-lf":  
            print("Insert the column names in the order of the file separated by one space")
            print("Some of this must be 'mass', 'x', 'y', 'z'")
            print("If this is not respected unexpected behaviour may occur.")
            column_raw = input()
            columns_names = column_raw.split(" ")       
            path = argv[3]                              
            collection = database.select_collection(block_model_name)
            mine = Mine(block_model_name)
            dbp.load_blocks(block_model_name,block_model_name,columns_names, collection)
        elif argv[2] == "-p":
            block_model_name = argv[1]
            #llamar a funcion print 
        elif argv[2] in options:
            block_model_name = argv[1]
            if argv[2] == "num_blocks":
                mine = Mine(block_model_name)
                collection = database.select_collection(block_model_name)
                result = mine.mine_blocks(collection)
                print(result)
            else:
                print("Error on second argument")
        elif len(argv) >= 7:
            if argv[6] in options:
                    block_model_name = argv[1]
                    coordinate_x = argv[2]
                    coordinate_y = argv[3]
                    coordinate_z = argv[4]
                    mineral_name = argv[5]
                    if argv[6] == "grade":
                        mine = Mine(block_model_name)
                        db = database.select_collection(block_model_name)
                        block = mine.find_block(coordinate_x,coordinate_y,coordinate_z, db)
                        result = block.block_grade(mineral_name)
                        print(result)
                    else:
                        print("Error on sixth argument")
        elif argv[5] in options and len(argv)>4:
            block_model_name = argv[1]
            coordinate_x = argv[2]
            coordinate_y = argv[3]
            coordinate_z = argv[4]
            if argv[5] == "mass":
                mine = Mine(block_model_name)
                db = database.select_collection(block_model_name)
                block = mine.find_block(coordinate_x,coordinate_y,coordinate_z, db)
                print(block)
                if block:
                    result = block.block_mass()
                    print(result)
                else:
                    print("Block not found")
        
        elif len(argv)> 5  and argv[5] in mine.find_block(coordinate_x,coordinate_y,coordinate_z, db).get_key_values():
            block_model_name = argv[1]
            coordinate_x = argv[2]
            coordinate_y = argv[3]
            coordinate_z = argv[4]
            block = mine.find_block(coordinate_x,coordinate_y,coordinate_z, db)
            result = block.block_attribute(argv[5])
            print(result)
        else:
            print("Error on arguments")
    else:
        print("Not enough arguments")

