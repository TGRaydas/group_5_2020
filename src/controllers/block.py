import json
from dbProvider import DBProvider

blocks = DBProvider.select_collection(name)


class Block:
	def __init__(block_columns, block_data):
		self.block_columns = block_columns
        self.block_data = block_data

	def to_json(self):
        block_json = {}
        for column_index in range(len(self.block_columns)):
            block_json[self.block_columns[column_index]] = self.block_data[column_index]
		return(block_json)

	def save_in_database(self):
		block = blocks.find_one({"x":self.block_data[1],"y":self.block_data[2],"z":self.block_data[3]})
		if block != None:
			return
		blocks.insert_one(self.to_json())

	def print_block(self):
		print(self.to_json())

    def block_mass(self):
        block_json = self.to_json()
        mass_name = input("Enter the name of mass column: ")
        if mass_name not in block_json.keys():
            return("The name of mass column was not valid")
        weight_name = input("[1]KG \n[2] TONS")
        if weight_name == "1":
            return(block_json[self.mass_name])
        elif weight_name == "2":
            return(block_json[self.weight_name]/1000)
        else:
            return("Your option was not valid")

    def block_grade(self, mineral_name):
        option = input('The mass name came in: \n[1] Percent\n[2] Tons')
        if option == "1"
            pass
        elif option == "2":
            pass

    def block_attribute(self, attribute):
        if attribute not in self.block_columns:
            return("Not valid attribute")
        return(attribute, self.to_json()[attribute])
