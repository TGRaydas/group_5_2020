import sys
sys.path.append('..')
from controllers.categorical_attribute_strategy import CategoricalAttributeStrategy
from controllers.proporcional_attribute_strategy import ProportionalAttributeStrategy
from controllers.continue_attribute_strategy import ContinueAttributeStrategy

class AttributeStrategyFactory:
    def strategy(self, blocks, attribute, mass_attribute,type_attribute):
        if (type_attribute == 'cat' ):
            return CategoricalAttributeStrategy()
        elif (type_attribute == 'prop' ):
            return ProportionalAttributeStrategy()
        elif (type_attribute == 'con' ):
            return ContinueAttributeStrategy()
        pass
