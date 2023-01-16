from Hyperparameter import Hyperparameter 

class SingleHyperparameter(Hyperparameter):
    def __init__(self, name, value):
        Hyperparameter.__init__(self, name)
        self.value = value

    def __str__(self):
        return "SingleHyperparameter: " + self.name + " " + str(self.value)

    def __repr__(self):
        return self.__str__()

    