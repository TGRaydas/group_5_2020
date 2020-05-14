import sys
sys.path.append('..')
import utils.dbProvider as dbp
from controllers.block import Block
from controllers.blockModel import BlockModel
from controllers.subscriber import Subscriber
argv = sys.argv
database = dbp.DBProvider()


class App(Subscriber):   
    def handle(self, event):
        print(event)
    def run(self):
    #Load blocks from a file giving the path into database
        if argv[1] == "-lf":
            block_model_name = argv[3]
            print("Insert the column names in the order of the file separated by one space")
            column_raw = input()
            columns_names = column_raw.split(" ")       
            path = argv[2]                              
            collection = database.select_collection(block_model_name)
            block_model = BlockModel(block_model_name)
            database.add_subscriber(self)
            database.load_blocks(path,block_model_name,columns_names)
        #Number of mine blocks
        elif argv[2] == "num_blocks":
            block_model_name = argv[1]
            block_model = BlockModel(block_model_name)
            collection = database.select_collection(block_model_name)
            block_model.add_subscriber(self)
            result = block_model.blocks_count(collection)
            print(result)
        #Mass value of block
        elif len(argv) > 5 and argv[5] == "mass":
            mass_name = input("Enter the name of mass column: ")
            weight_name = input("[1]KG \n[2]TONS\n")
            block_model_name = argv[1]
            coordinate_x = argv[2]
            coordinate_y = argv[3]
            coordinate_z = argv[4]
            block_model = BlockModel(block_model_name)
            db = database.select_collection(block_model_name)
            block_model.add_subscriber(self)
            block = block_model.find_block(coordinate_x,coordinate_y,coordinate_z, db)
            if block:
                result = block.block_mass(mass_name, weight_name)
                print(result)
            else:
                print("Block not found")
        #reblock
        elif argv[2] =="reblock":
            block_model_name = argv[1]
            reblock_x = int(argv[3])
            reblock_y = int(argv[4])
            reblock_z = int(argv[5])
            collection = database.select_collection(block_model_name)
            block_model = BlockModel(block_model_name)
            print("Insert the attributes types printed bellow separeted by space")
            print("Types:\n\tCategorical: cat\n\tProportional: prop\n\tContinue: con")
            print(' '.join(map(str, block_model.reblock_model_attributes(collection))))
            attributes_types = input('').split()
            mass_attribute = input('Insert the name of mass attribute\n')
            block_model.add_subscriber(self)
            reblock_model_collection = block_model.reblock(collection, reblock_x, reblock_y, reblock_z, attributes_types, mass_attribute)
            reblock_collection = reblock_model_collection.find({})
            for block in reblock_collection:
                print(block)

        #grade
        elif len(argv) > 6 and argv[6] == "grade":
            mineral_type_value = input('Mineral weight value came in: \n[1] Percent\n[2] Tons\n[3] KG\n')
            mass_name = input("Enter the name of mass column: ")
            weight_name = input("[1]KG \n[2]TONS\n")
            block_model_name = argv[1]
            coordinate_x = argv[2]
            coordinate_y = argv[3]
            coordinate_z = argv[4]
            mineral_name = argv[5]
            block_model = BlockModel(block_model_name)
            collection = database.select_collection(block_model_name)
            block_model.add_subscriber(self)
            block = block_model.find_block(coordinate_x,coordinate_y,coordinate_z, collection)
            block.add_subscriber(self)
            result = block.block_grade(mineral_name,mass_name, weight_name, mineral_type_value)
            print(result)
        #attribute
        elif len(argv) == 6:
            block_model_name = argv[1]
            coordinate_x = argv[2]
            coordinate_y = argv[3]
            coordinate_z = argv[4]
            collection = database.select_collection(block_model_name)
            block_model = BlockModel(block_model_name)
            block_model.add_subscriber(self)
            block = block_model.find_block(coordinate_x,coordinate_y,coordinate_z, collection)
            if argv[5] not in block.to_json().keys():
                print("Invalid attribute")
            else:
                print(block.block_attribute(argv[5]))


App().run()



        