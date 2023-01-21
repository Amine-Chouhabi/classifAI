

from model.algorithms.hyperparameter.Hyperparameter import Hyperparameter
from model.algorithms.hyperparameter.RangeHyperparameter import RangeHyperparameter

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
        