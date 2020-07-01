# SoftwareDesign_Group_5_Project_1
  This software saves into a database and prints to the command line the blocks of a "Mine Block Model" file.

# PRODUCTION URL
   https://group-5-api.herokuapp.com/
 
 # REQUIREMENTS:
 
   Python version: Python >= 3.x.x  
   Pytohn library: PyMongo >= 3.1.x
   pip3 install Flask
   pip3 install Flask-Cors
   Mine Block Model File
 
 
# RUN API:
   From the command line in the script  folder /src/ run "python3 main.py"
   The api run in  "http://127.0.0.1:5000/"

# API DOCUMENTATION:
   The following structure is an example of what is required to get all a blocks in block model in endpoint GET: api/block_models/
   return:

   {
      "block_models":
                  [{"name": "kd"}, {"name": "newman_reblock"}, {"name": "zuck_small_reblock"}, {"name": "test"}, {"name": "TEST"}, {"name": "newman"}, {"name": "test_reblock"}, {"name": "zuck_small"}]
   }


   The following structure is an example of what is required to get all a blocks in block model in endpoint GET: api/block_models/<block_model_name>/blocks
   return:

   {
      "block_model": 
               {"blocks": 
               [{"au": "0.2", "id": "4", "ton": "20.83", "x": "38", "y": "28", "z": "67"}, {"au": "0.3", "id": "5", "ton": "83.33", "x": "39", "y": "28", "z": "67"}, {"au": "0.2", "id": "0", "ton": "20.83", "x": "36", "y": "28", "z": "67"}, {"au": "0.3", "id": "1", "ton": "83.33", "x": "37", "y": "28", "z": "67"}]
               }
   }

   The following structure is an example of what is required to get a block info in block model in endpoint GET: api/block_models/<block_model_name>/blocks/<index>
   return:

   {
   "block" : {
         "index": <index>,
         "x": <x>,
         "y": <y>,
         "z": <z>,
         "grades": { 
         "au" : <au grade in %>,
         "cu" : <cu grade in %>,
         },
         "mass" : <mass in kg>
      }
   }
 

   The following structure is an example of what is required to insert a block model in endpoint POST: api/block_models/<block_model_name>/blocks

   {
      "columns": "id x y z cost value rock_tonnes ore_tonnes",
      "data": ["0 1 1 1 0.23 4.34 5 0.07634","1 1 1 2 0.001 1.34 7 0.034"]
   }  


   The following structure is an example of what is required to reblock a block model in endpoint POST: /api/block_models/<block_model_name>/reblock
   {
      "reblock_x": "2",
      "reblock_y": "2",
      "reblock_z": "2",
      "attributes_types": "prop prop con prop",
      "mass_attribute": "rock_tonnes"
   }

   The following structure is an example of what is required to load a precedence of  a block model in endpoint POST: /api/block_models/<block_model_name>/prec
   {
      "prec_list": ["0 1 34", "1 3 2 0 45", "2 0"]
   }

   the following format is an example of the Extract function for that model block and returns the blocks that should be extracted, in  endpoint POST: 
   api/block_models/<name>/blocks/<index>/extract
   { 
      "blocks": [{"index":123},{"index":124},{"index":125}] 
   }




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


