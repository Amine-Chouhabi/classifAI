import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\algorithms\\hyperparameter\\Hyperparameter.py")
sys.path.append(file_dir)

from SingleHyperparameter import SingleHyperparameter
from RangeHyperparameter import RangeHyperparameter

class AlgorithmHyperparameterBuilder:
    def __init__(self, root,algorithm_name, algorithms):
        self.root = root
        self.algorithms = algorithms
        self.algorithm_name = algorithm_name
    
    def with_(self):
        return self
    
    def hyperparameter(self, hyperparameter_name):
        # dictionary of hyperparameters with hteir type (single or range)
        single_or_range = None

        # check if name appears in the list of hyperparameters for the algorithm
        for hyperparameter in self.root.hyperparameters.hyperparameters:
            if hyperparameter.name == hyperparameter_name:
                
                # search for the algirthm in the list of algorithms
                for algorithm in self.algorithms:
                    if algorithm.name == self.algorithm_name:
                        # check if the hyperparameter belongs to the algorithm
                        hyperparameter_names = algorithm.get_hyperparameters_names()
                        if hyperparameter_name in hyperparameter_names:
                            algorithm.set_hyperparameter(hyperparameter)
                        else :
                            raise ValueError("Hyperparameter is not valid for the algorithm")         
                return self
        raise ValueError("Hyperparameter "+ hyperparameter_name +" not defined")
    
    def learning_rate(self):
        return self.hyperparameter("learning_rate")
    
    def batch_size(self):
        return self.hyperparameter("batch_size")
    
    def max_depth(self):
        return self.hyperparameter("max_depth")
    
    def n_estimators(self):
        return self.hyperparameter("n_estimators")
    
    def criterion(self):
        return self.hyperparameter("criterion")

    def C(self):
        return self.hyperparameter("C")
    
    def kernel(self):
        return self.hyperparameter("kernel")

    def gamma(self):
        return self.hyperparameter("gamma")

    def degree(self):
        return self.hyperparameter("degree")

    def epsilon(self):
        return self.hyperparameter("epsilon")

    def n_neighbors(self):
        return self.hyperparameter("n_neighbors")

    def p(self):
        return self.hyperparameter("p")

    def random_state(self):
        return self.hyperparameter("random_state")

    def n_jobs(self):
        return self.hyperparameter("n_jobs")
    
    def verbose(self):
        return self.hyperparameter("verbose")
    
    def solver(self):
        return self.hyperparameter("solver")

    

        
    
    def end(self):
        return self.root
        




