import sys

argv = sys.argv
commands = ["-lf", "--load-file", "-p", "--print"]
options = ["grade", "mass", "num_blocks"]
mineral_name = ""
block_model_name = ""
coordinate_x = ""
coordinate_y = ""
coordinate_z = ""

if __name__ == "__main__":
	print(argv)
	if argv[1] == "-lf":
		block_model_name = argv[2]
        #llamar a funcion leer bd
	elif argv[1] == "-p":
		block_model_name = argv[2]
		#llamar a funcion print 
    elif argv[2] in options:
        block_model_name = argv[1]
        if argv[2] == "num_blocks":
            #llamar a funcnion numero de bloques con el block-model_name
            #aquiid deberia guardarse en una variable y si hay error impirmirlo
        else:
            print("Error on second argument")
    elif argv[6] in options:
        block_model_name = argv[1]
        coordinate_x = argv[2]
        coordinate_y = argv[3]
        coordinate_z = argv[4]
        mineral_name = argv[5]
        if argv[6] == "grade":
            #llamar a funcion grade con mineral_name y blockmodelname
        else:
            print("Error on sixth argument")
    elif argv[5] in options:
        block_model_name = argv[1]
        coordinate_x = argv[2]
        coordinate_y = argv[3]
        coordinate_z = argv[4]
        if argv[5] == "mass":
            #llamar a funcion mass
        #elif argv[5] = #nombre de  algun atributo:
            #llamar a funcion
        else:
            print("Error on fifth argument")

