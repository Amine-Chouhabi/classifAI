import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\algorithms\\hyperparameter\\Hyperparameter.py")
sys.path.append(file_dir)

from Hyperparameter import Hyperparameter
from RangeHyperparameter import RangeHyperparameter

class RangeHyperparameterBuilder:
    def __init__(self, root, name):
        self.root = root
        self.name = name
        self.max = None
        self.min = None
        self.step = None
        

        
    
    def max_(self, max):
        print("here")
        self.max = max
        return self
    
    def min_(self, min):
        self.min = min

        return self
    
    def step_(self, step):
        self.step = step
        self.root.hyperparameter = RangeHyperparameter(self.name, self.min, self.max, self.step)
        self.root.root.hyperparameters.append(self.root.hyperparameter)
        return self.root.root
        