import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\algorithms\\hyperparameter\\Hyperparameter.py")
sys.path.append(file_dir)

from Hyperparameter import Hyperparameter
from SingleHyperparameter import SingleHyperparameter
from RangeHyperparameter import RangeHyperparameter

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