# hyperparameter class 

class Hyperparameter:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "Hyperparameter: " + self.name + " " + str(self.value)
    
    def __repr__(self):
        return self.__str__()
    
    