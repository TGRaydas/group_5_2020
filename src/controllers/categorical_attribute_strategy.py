import sys
sys.path.append('..')
from controllers.abstract_attribute_strategy  import AbstractAttributeStrategy

class CategoricalAttributeStrategy(AbstractAttributeStrategy):
  def calculate(self,blocks, attribute, mass_attribute):
    attributes = []
    if len(blocks) == 0:
        return None
    for block in blocks:
        attributes.append(block[attribute])
    return max(set(attributes), key = attributes.count) 