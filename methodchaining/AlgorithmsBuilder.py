import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\algorithms")
sys.path.append(file_dir)

from algorithms.Algorithm import Algorithm
from algorithms.SVM import SVM
from algorithms.NaiveBayes import NaiveBayes
from algorithms.RandomForest import RandomForest
from algorithms.DecisionTree import DecisionTree
from algorithms.LogisticRegression import LogisticRegression
from algorithms.KNearestNeighbours import KNearestNeighbours
from algorithms.StochasticGradientDescent import StochasticGradientDescent
from AlgorithmHyperparameterBuilder import AlgorithmHyperparameterBuilder



class AlgorithmsBuilder:
    def __init__(self, root, hyperparameters):
        self.root = root
        self.algorithms = None
        self.hyperparameters = hyperparameters
        self.actions = []


    def svm(self, name):
        if self.algorithms is None:
            self.algorithms = []
        
        # check if the same algorithm is already added
        for i in range(len(self.algorithms)):
            if self.algorithms[i].name == name:
                raise Exception("Algorithm already added: " + name)
        svm = SVM(name)
        self.algorithms.append(svm)
        builder = AlgorithmHyperparameterBuilder(self,name, self.algorithms)
        
        return builder

    
    
    
    def naive_bayes(self, name, hyperparameters_names):
        if self.algorithms is None:
            self.algorithms = []
        naive_bayes = NaiveBayes(name)
        naive_bayes_hyperparameters_names = naive_bayes.get_hyperparameters_names()
        # check if the hyperparameters are valid
        for i in range(len(hyperparameters_names)):
            if hyperparameters_names[i] not in naive_bayes_hyperparameters_names:
                raise Exception("Invalid hyperparameter name: " + hyperparameters_names[i])
        naive_bayes.set_hyperparameters(hyperparameters_names)
        self.algorithms.append(naive_bayes)
        return self
    
    def random_forest(self, name, hyperparameters_names):
        if self.algorithms is None:
            self.algorithms = []
        random_forest = RandomForest(name)
        random_forest_hyperparameters_names = random_forest.get_hyperparameters_names()
        # check if the hyperparameters are valid
        for i in range(len(hyperparameters_names)):
            if hyperparameters_names[i] not in random_forest_hyperparameters_names:
                raise Exception("Invalid hyperparameter name: " + hyperparameters_names[i])
        random_forest.set_hyperparameters(hyperparameters_names)
        self.algorithms.append(random_forest)
        return self
    
    def decision_tree(self, name, hyperparameters_names):
        if self.algorithms is None:
            self.algorithms = []
        decision_tree = DecisionTree(name)
        decision_tree_hyperparameters_names = decision_tree.get_hyperparameters_names()
        # check if the hyperparameters are valid
        for i in range(len(hyperparameters_names)):
            if hyperparameters_names[i] not in decision_tree_hyperparameters_names:
                raise Exception("Invalid hyperparameter name: " + hyperparameters_names[i])
        decision_tree.set_hyperparameters(hyperparameters_names)
        self.algorithms.append(decision_tree)
        return self
    
    def logistic_regression(self, name, hyperparameters_names):
        if self.algorithms is None:
            self.algorithms = []
        logistic_regression = LogisticRegression(name)
        logistic_regression_hyperparameters_names = logistic_regression.get_hyperparameters_names()
        # check if the hyperparameters are valid
        for i in range(len(hyperparameters_names)):
            if hyperparameters_names[i] not in logistic_regression_hyperparameters_names:
                raise Exception("Invalid hyperparameter name: " + hyperparameters_names[i])
        logistic_regression.set_hyperparameters(hyperparameters_names)
        self.algorithms.append(logistic_regression)
        return self
    
    def k_nearest_neighbours(self, name, hyperparameters_names):
        if self.algorithms is None:
            self.algorithms = []
        k_nearest_neighbours = KNearestNeighbours(name)
        k_nearest_neighbours_hyperparameters_names = k_nearest_neighbours.get_hyperparameters_names()
        # check if the hyperparameters are valid
        for i in range(len(hyperparameters_names)):
            if hyperparameters_names[i] not in k_nearest_neighbours_hyperparameters_names:
                raise Exception("Invalid hyperparameter name: " + hyperparameters_names[i])
        k_nearest_neighbours.set_hyperparameters(hyperparameters_names)
        self.algorithms.append(k_nearest_neighbours)
        return self
    
    def stochastic_gradient_descent(self, name, hyperparameters_names):
        if self.algorithms is None:
            self.algorithms = []
        stochastic_gradient_descent = StochasticGradientDescent(name)
        stochastic_gradient_descent_hyperparameters_names = stochastic_gradient_descent.get_hyperparameters_names()
        # check if the hyperparameters are valid
        for i in range(len(hyperparameters_names)):
            if hyperparameters_names[i] not in stochastic_gradient_descent_hyperparameters_names:
                raise Exception("Invalid hyperparameter name: " + hyperparameters_names[i])
        stochastic_gradient_descent.set_hyperparameters(hyperparameters_names)
        self.algorithms.append(stochastic_gradient_descent)
        return self

    def train(self):
        if self.algorithms is None:
            raise Exception("No algorithms were added")
        self.actions.append("train")
        return self
    
    def predict(self):
        if self.algorithms is None:
            raise Exception("No algorithms were added")
        self.actions.append("predict")
        return self
        
        


    def add_algorithm(self, algorithm):
        if self.algorithms is None:
            self.algorithms = []
        self.algorithms.append(algorithm)
        return self

    def end_algorithms(self):
        return self.root


    def get_algorithms(self):
        return self.algorithms

    def get_notebook_code(self):
        code = ""
        if self.algorithms is None:
            return code
        code += "# setting the algorithms\n"
        # set all algorithms
        for i in range(len(self.algorithms)):
            if isinstance(self.algorithms[i], SVM):
                # initialize the algorithm svm with the hyperparameters
                code += self.algorithms[i].name + " = svm.SVC("
                for j in range(len(self.algorithms[i].hyperparameters)):
                    code += self.algorithms[i].hyperparameters[j].name + "=" + self.algorithms[i].hyperparameters[j].name
                    if j != len(self.algorithms[i].hyperparameters) - 1:
                        code += ", "
                code += ")\n"
            elif isinstance(self.algorithms[i], NaiveBayes):
                # initialize the algorithm naive bayes with the hyperparameters
                code += self.algorithms[i].name + " = GaussianNB("
                for j in range(len(self.algorithms[i].hyperparameters)):
                    code += self.algorithms[i].hyperparameters[j] + "=" + self.algorithms[i].hyperparameters[j]
                    if j != len(self.algorithms[i].hyperparameters) - 1:
                        code += ", "
                code += ")\n"
            
            elif isinstance(self.algorithms[i], RandomForest):
                # initialize the algorithm random forest with the hyperparameters
                code += self.algorithms[i].name + " = RandomForestClassifier("
                for j in range(len(self.algorithms[i].hyperparameters)):
                    code += self.algorithms[i].hyperparameters[j] + "=" + self.algorithms[i].hyperparameters[j]
                    if j != len(self.algorithms[i].hyperparameters) - 1:
                        code += ", "
                code += ")\n"
            
            elif isinstance(self.algorithms[i], DecisionTree):
                # initialize the algorithm decision tree with the hyperparameters
                code += self.algorithms[i].name + " = DecisionTreeClassifier("
                for j in range(len(self.algorithms[i].hyperparameters)):
                    code += self.algorithms[i].hyperparameters[j] + "=" + self.algorithms[i].hyperparameters[j]
                    if j != len(self.algorithms[i].hyperparameters) - 1:
                        code += ", "
                code += ")\n"
            
            elif isinstance(self.algorithms[i], LogisticRegression):
                # initialize the algorithm logistic regression with the hyperparameters
                code += self.algorithms[i].name + " = LogisticRegression("
                for j in range(len(self.algorithms[i].hyperparameters)):
                    code += self.algorithms[i].hyperparameters[j] + "=" + self.algorithms[i].hyperparameters[j]
                    if j != len(self.algorithms[i].hyperparameters) - 1:
                        code += ", "
                code += ")\n"
            
            elif isinstance(self.algorithms[i], KNearestNeighbours):
                # initialize the algorithm k nearest neighbours with the hyperparameters
                code += self.algorithms[i].name + " = KNeighborsClassifier("
                for j in range(len(self.algorithms[i].hyperparameters)):
                    code += self.algorithms[i].hyperparameters[j] + "=" + self.algorithms[i].hyperparameters[j]
                    if j != len(self.algorithms[i].hyperparameters) - 1:
                        code += ", "
                code += ")\n"
            
            elif isinstance(self.algorithms[i], StochasticGradientDescent):
                # initialize the algorithm stochastic gradient descent with the hyperparameters
                code += self.algorithms[i].name + " = SGDClassifier("
                for j in range(len(self.algorithms[i].hyperparameters)):
                    code += self.algorithms[i].hyperparameters[j] + "=" + self.algorithms[i].hyperparameters[j]
                    if j != len(self.algorithms[i].hyperparameters) - 1:
                        code += ", "
                code += ")\n"
            
            else:
                raise Exception("Invalid algorithm")

            
        # train the algorithms
        if self.actions is not None:
            if "train" in self.actions:
                code += "# training the algorithms\n"
                for i in range(len(self.algorithms)):
                    code += "start_" + self.algorithms[i].name + " = time.time()\n"
                    code += self.algorithms[i].name + ".fit(X_train, y_train)\n"
                    code += "end_" + self.algorithms[i].name + " = time.time()\n"
            if "predict" in self.actions:
                code += "# predicting the algorithms\n"
                for i in range(len(self.algorithms)):
                    code += "y_pred_" + self.algorithms[i].name +" = " + self.algorithms[i].name + ".predict(X_test)\n"



            


            
        return code