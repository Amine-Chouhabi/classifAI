import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\model\\algorithms\\hyperparameter\\Hyperparameter.py")
sys.path.append(file_dir)

from Hyperparameter import Hyperparameter
from SingleHyperparameter import SingleHyperparameter
from RangeHyperparameter import RangeHyperparameter

class HyperParametersBuilder:
    def __init__(self, root):
        self.root = root
        self.hyperparameters = None

    def add_hyperparameter(self, name, value):
        if self.hyperparameters is None:
            self.hyperparameters = []
        self.hyperparameters.append(SingleHyperparameter(name, value))
        return self

    def add_range_hyperparameter(self, name, min, max, step):
        if self.hyperparameters is None:
            self.hyperparameters = []
        self.hyperparameters.append(RangeHyperparameter(name, min, max, step))
        return self

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

    

    