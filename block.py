import json

class Block():
    def __init__(self, block_columns, block_data):
        self.block_columns = block_columns
        self.block_data = block_data

    def to_json(self):
        block_json = {}
        col_key = list(self.block_columns)
        col_data = list(self.block_data)
        for column_index in range(len(self.block_columns)):
            block_json[col_key[column_index]] = col_data[column_index]
        return(block_json)
    def get_key_values(self):
        return list(self.block_columns)
    def save_in_database(self, blocks):
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
            return("The name of mass column was not valid (should be mass)")
        weight_name = input("[1]KG \n[2] TONS")
        if weight_name == "1":
            return(block_json["mass"])
        elif weight_name == "2":
            return(block_json["mass"]/1000)
        else:
            return("Your option was not valid")

    def block_grade(self, mineral_name):
        option = input('Mineral weight value came in: \n[1] Percent\n[2] Tons\n[3] KG')
        if option == "1":
            self.to_json()[mineral_name]
        elif option == "2":
            block_mass_value = self.block_mass()
            if block_mass_value == "Your option was not valid":
                return False
            return((self.to_json()[mineral_name]/(block_mass_value*1000))*100)
        elif option == "3":
            block_mass_value = self.block_mass()
            if block_mass_value == "Your option was not valid":
                return False
            return(100*(self.to_json()[mineral_name]/(block_mass_value)))

    def block_attribute(self, attribute):
        if attribute not in self.block_columns:
            return("Not valid attribute")
        return(attribute, self.to_json()[attribute])
