import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\algorithms\\hyperparameter\\Hyperparameter.py")
sys.path.append(file_dir)

class AlgorithmHyperparameterBuilder:
    def __init__(self, root, algorithms):
        self.root = root
        self.algorithms = algorithms
        self.hyperparameters = None

    def set_hyperparameters(self, hyperparameters):
        self.hyperparameters = hyperparameters
        return self

    def end_hyperparameters(self):
        for algorithm in self.algorithms:
            algorithm.set_hyperparameters(self.hyperparameters)
        return self.root


