import json
from controllers.block_flyweight_factory import BlockFlyweightFactory


class Block():
    def __init__(self, block_columns, block_data):
        self.flyweight = BlockFlyweightFactory().create_flyweight(block_columns, block_data)

    def __eq__(self, other):
        for index in range(len(self.flyweight.block_columns)):
            if self.flyweight.block_columns[index] != other.flyweight.block_columns[index]:
                return False
        for index in range(len(self.flyweight.block_data)):
            if self.flyweight.block_data[index] != other.flyweight.block_data[index]:
                return False
        return True

    def to_json(self):
        block_json = {}
        col_key = list(self.flyweight.block_columns)
        col_data = list(self.flyweight.block_data)
        for column_index in range(len(self.flyweight.block_columns)):
            block_json[col_key[column_index]] = str(col_data[column_index])
        return(block_json)

    def block_column_attr(self, block_model_name, database):
        collection = database.select_collection('models_attr')
        attr = collection.find_one({'model': block_model_name})
        print(block_model_name)
        return attr

    def info_json(self, block_model_name, database):
        block_json = {"grades": {}}
        col_key = list(self.flyweight.block_columns)
        col_data = list(self.flyweight.block_data)
        attr = self.block_column_attr(block_model_name, database)
        mass_value = 0
        for column_index in range(len(self.flyweight.block_columns)):
            if col_key[column_index] == attr['mass']:
                mass_value = float(col_data[column_index])
        print(attr['attr'],(self.flyweight.block_columns))
        for column_index in range(len(self.flyweight.block_columns)):
            if col_key[column_index] == "id":
                block_json["index"] = str(col_data[column_index])
            elif col_key[column_index] == "_id":
                continue
            elif col_key[column_index] == "x" or col_key[column_index] == "y" or col_key[column_index] == "z":
                block_json[col_key[column_index]] = str(col_data[column_index])
            elif col_key[column_index] == attr['mass']:
                block_json['mass'] = str(col_data[column_index])
            else:
                if attr['attr'][column_index - 1] == 'con':
                    block_json["grades"][col_key[column_index]] = (float(col_data[column_index])/mass_value)*100
                elif attr['attr'][column_index - 1] == 'prop':
                    block_json["grades"][col_key[column_index]] = float(col_data[column_index])
        return(block_json)

    def get_key_values(self):
        return list(self.flyweight.block_columns)

    def save_in_database(self, collections):
        block = collections.find_one({"x":self.flyweight.block_data[1],"y":self.flyweight.block_data[2],"z":self.flyweight.block_data[3]})
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
        if attribute not in self.flyweight.block_columns:
            return("Not valid attribute")
        return_attributes = {}
        for key in self.to_json().keys():
            if key != attribute and key != "_id":
                return_attributes[key] = self.to_json()[key]
        return_attributes[attribute] = self.to_json()[attribute]
        return(return_attributes)
