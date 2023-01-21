
from model.algorithms.hyperparameter.Hyperparameter import Hyperparameter
from model.algorithms.hyperparameter.SingleHyperparameter import SingleHyperparameter
from model.algorithms.hyperparameter.RangeHyperparameter import RangeHyperparameter

from RangeHyperparameterBuilder import RangeHyperparameterBuilder


class HyperparameterValues:
    def __init__(self, root, name):
        self.root = root
        self.name = name
        self.hyperparameter = None
    
    def set_range(self):

        #self.hyperparameter = RangeHyperparameter(self.name, min, max, step) 
        #self.root.hyperparameters.append(self.hyperparameter)
        builder = RangeHyperparameterBuilder(self, self.name)
        print(builder)
        return builder
        

    def set_value(self, value):
        self.hyperparameter = SingleHyperparameter(self.name, value)
        self.root.hyperparameters.append(self.hyperparameter)
        return self.root