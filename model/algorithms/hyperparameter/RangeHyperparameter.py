from model.algorithms.hyperparameter.Hyperparameter import Hyperparameter

class RangeHyperparameter(Hyperparameter):
    def __init__(self, name, min, max, step):
        Hyperparameter.__init__(self, name)
        self.min = min
        self.max = max
        self.step = step

    def __str__(self):
        return "RangeHyperparameter: " + self.name + " " + str(self.min) + " " + str(self.max) + " " + str(self.step)
    
    def __repr__(self):
        return self.__str__()
