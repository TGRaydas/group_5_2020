# SoftwareDesign_Group_5_Project_1
  This software saves into a database and prints to the command line the blocks of a "Mine Block Model" file.
 
 # REQUIREMENTS:
 
  Python version: Python >= 3.x.x  
   Pytohn library: PyMongo >= 3.1.x
   Mine Block Model File
 
 
 

# RUN PROGRAM:
   
   From the command line in the script  folder /src/ run "python3 main.py -lf [path_of_the_mine_block_model_file] [name_block_model]" 

   For saving and printing the blocks.

   From Command Line Interface to get  the Number of Blocks of a stored block model yo will run the next command line :

	"python3 main.py [block_model_name] num_blocks"


	From Command Line Interface to get  the Mass in Kg of a stored block model yo will run the next command line:

	"python3 main.py [block_model_name] [block_x] [block_y] [block_z] mass"


	From Command Line Interface to get  the Grade in Porcentage ofr each Mineral of a stored block model yo will run the next command line:

	"python3 main.py [block_model_name] [block_x] [block_y] [block_z] [mineral_name] grade"


	From Command Line Interface to get  all other attribute of a one block in astored block model yo will run the next command line:

	"python3 main.py [block_model_name] [block_x] [block_y] [block_z] [attribute_name]"


   From COmmand Line Interface to create a reblock of a Block Model, run the following code:

   "python3 main.py [block_model_name] reblock [amount_of_reblock_on_x] [amount_of_reblock_on_y] [amount_of_reblock_on_z]

   
# FLAGS:
   
   -lf [path__mine_block_model_file] [name_block_model]: Saves and prints into the command line the blocks specified in the path file.

 
# TESTS:
   
   To run the test of the block, run in the command line in de folder /src/test "python3 test_block.py -v"
   
   To run the test of the blockModel, run in the command line in de folder /src/test "python3 test_blockModel.py -v"
   
   
 
# DEVELOPED BY:
   PEDRO GRAND  
   RAIMUNDO MARIN  
   JUAN RODRIGUEZ  


