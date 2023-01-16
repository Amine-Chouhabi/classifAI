# abstract class for classification algorithms

from abc import ABC, abstractmethod

class Algorithm(ABC):   
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Algorithm: " + self.name + " " + str(self.hyperparameters)

    def __repr__(self):
        return self.__str__()



    @abstractmethod
    def get_hyperparameters_names(self):
        pass

