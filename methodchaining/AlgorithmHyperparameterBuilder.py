import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\algorithms\\hyperparameter\\Hyperparameter.py")
sys.path.append(file_dir)

class AlgorithmHyperparameterBuilder:
    def __init__(self, root,algorithm_name, algorithms):
        self.root = root
        self.algorithms = algorithms
        self.algorithm_name = algorithm_name
    
    def with_(self):
        return self
    
    def hyperparameter(self, hyperparameter_name):
        # check if name appears in the list of hyperparameters for the algorithm
        for hyperparameter in self.root.hyperparameters.hyperparameters:
            print("here ===============================")
            print(hyperparameter.name)
            print(hyperparameter_name)
            if hyperparameter.name == hyperparameter_name:
                # search for the algirothm in the list of algorithms
                for algorithm in self.algorithms:
                    if algorithm.name == self.algorithm_name:
                        # check if the hyperparameter belongs to the algorithm
                        hyperparameter_names = algorithm.get_hyperparameters_names()
                        if hyperparameter_name in hyperparameter_names:
                            algorithm.set_hyperparameter(hyperparameter)
                        else :
                            raise ValueError("Hyperparameter is not valid for the algorithm")         
                return self
        raise ValueError("Hyperparameter name not found")
    
    def end(self):
        return self.root
        




