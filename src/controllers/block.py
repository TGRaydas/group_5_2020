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
    def save_in_database(self, collections):
        block = collections.find_one({"x":self.block_data[1],"y":self.block_data[2],"z":self.block_data[3]})
        if block != None:
            return
        collections.insert_one(self.to_json())

    def print_block(self):
        print(self.to_json())

    def block_mass(self, mass_name, weight_name):
        block_json = self.to_json()
        if mass_name not in block_json.keys():
            return("The name of mass column was not valid (should be mass)")
        if weight_name == "1":
            return(block_json[mass_name])
        elif weight_name == "2":
            return(float(block_json[mass_name])/1000)
        else:
            return("Your option was not valid")

    def block_grade(self, mineral_name, mass_name, weight_name, mineral_type_value):
        if mineral_type_value == "1":
            return(self.to_json()[mineral_name])
        elif mineral_type_value == "2":
            block_mass_value = self.block_mass(mass_name, weight_name)
            if block_mass_value == "Your option was not valid" or block_mass_value == "The name of mass column was not valid (should be mass)":
                return False
            return((float(self.to_json()[mineral_name])/(float(block_mass_value)*1000))*100)
        elif mineral_type_value == "3":
            block_mass_value = self.block_mass(mass_name, weight_name)
            if block_mass_value == "Your option was not valid" or block_mass_value == "The name of mass column was not valid (should be mass)":
                return False
            return(100*(float(self.to_json()[mineral_name])/float(block_mass_value)))

    def block_attribute(self, attribute):
        if attribute not in self.block_columns:
            return("Not valid attribute")
        return_attributes = {}
        return_attributes[attribute] = self.to_json()[attribute]
        return(return_attributes)
