import os
import sys
from HyperparameterValues import HyperparameterValues


file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\algorithms\\hyperparameter\\Hyperparameter.py")
sys.path.append(file_dir)

from Hyperparameter import Hyperparameter
from SingleHyperparameter import SingleHyperparameter
from RangeHyperparameter import RangeHyperparameter

class HyperParametersBuilder:
    def __init__(self, root):
        self.root = root
        self.hyperparameters = []


    def set_hyperparameter(self, name):
        hyperparameterBuilder = HyperparameterValues(self, name)
        return hyperparameterBuilder
    
    def learning_rate(self):
        return self.set_hyperparameter("learning_rate")
    
    def batch_size(self):
        return self.set_hyperparameter("batch_size")
    
    def max_depth(self):
        return self.set_hyperparameter("max_depth")
    
    def n_estimators(self):
        return self.set_hyperparameter("n_estimators")
    
    def criterion(self):
        return self.set_hyperparameter("criterion")
    
    def C(self):
        return self.set_hyperparameter("C")
    
    def kernel(self):
        return self.set_hyperparameter("kernel")
    
    def gamma(self):
        return self.set_hyperparameter("gamma")
    
    def degree(self):
        return self.set_hyperparameter("degree")
    
    def epsilon(self):
        return self.set_hyperparameter("epsilon")
    
    def n_neighbors(self):
        return self.set_hyperparameter("n_neighbors")
    
    def p(self):
        return self.set_hyperparameter("p")

    def random_state(self):
        return self.set_hyperparameter("random_state")
    
    def verbose(self):
        return self.set_hyperparameter("verbose")
    
    def max_iter(self):
        return self.set_hyperparameter("max_iter")
    
    def n_jobs(self):
        return self.set_hyperparameter("n_jobs")
    
    def activation(self):
        return self.set_hyperparameter("activation")
    
    def solver(self):
        return self.set_hyperparameter("solver")
        
    

    


    

    
    def end_hyperparameters(self):
        return self.root

    def get_notebook_code(self):
        code = ""
        if self.hyperparameters is None:
            return code
        code += "# setting the hyperparameters\n"
        # set all hyperparameters
        for i in range(len(self.hyperparameters)):
            if isinstance(self.hyperparameters[i], SingleHyperparameter):
                code += self.hyperparameters[i].name + " = " + str(self.hyperparameters[i].value) + "\n"
            elif isinstance(self.hyperparameters[i], RangeHyperparameter):
                code += self.hyperparameters[i].name + " = np.arange(" + str(self.hyperparameters[i].min) + ", " + str(self.hyperparameters[i].max) + ", " + str(self.hyperparameters[i].step) + ")\n"
        return code

    

    def get_hyperparameters(self):
        return self.hyperparameters

    

    