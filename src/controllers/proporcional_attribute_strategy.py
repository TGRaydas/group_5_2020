import sys
sys.path.append('..')
from controllers.abstract_attribute_strategy  import AbstractAttributeStrategy

class ProportionalAttributeStrategy(AbstractAttributeStrategy):
    def calculate(self,blocks, attribute, mass_attribute):
        value = 0
        mass = 0
        if len(blocks) == 0:
            return value
        for block in blocks:
            if block!= None:
                value += float(block[attribute]) * float(block[mass_attribute])
                mass += float(block[mass_attribute])
        return value/mass