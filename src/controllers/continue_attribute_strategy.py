import sys
sys.path.append('..')
from controllers.abstract_attribute_strategy  import AbstractAttributeStrategy

class ContinueAttributeStrategy(AbstractAttributeStrategy):
    def calculate(self,blocks, attribute, mass_attribute):
        value = 0
        if len(blocks) == 0:
            return value
        for block in blocks:
            if block != None:
                value += float(block[attribute])
        return value