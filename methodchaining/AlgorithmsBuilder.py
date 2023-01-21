import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\algorithms")
sys.path.append(file_dir)

from model.algorithms.Algorithm import Algorithm
from model.algorithms.SVM import SVM
from model.algorithms.NaiveBayes import NaiveBayes
from model.algorithms.RandomForest import RandomForest
from model.algorithms.DecisionTree import DecisionTree
from model.algorithms.LogisticRegression import LogisticRegression
from model.algorithms.KNearestNeighbours import KNearestNeighbours
from model.algorithms.StochasticGradientDescent import StochasticGradientDescent
from AlgorithmHyperparameterBuilder import AlgorithmHyperparameterBuilder

from model.algorithms.hyperparameter.SingleHyperparameter import SingleHyperparameter
from model.algorithms.hyperparameter.RangeHyperparameter import RangeHyperparameter

import nbformat




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

    
    
    
    def naive_bayes(self, name):
        if self.algorithms is None:
            self.algorithms = []
        
        # check if the same algorithm is already added
        for i in range(len(self.algorithms)):
            if self.algorithms[i].name == name:
                raise Exception("Algorithm already added: " + name)
        naive_bayes = NaiveBayes(name)
        self.algorithms.append(naive_bayes)
        builder = AlgorithmHyperparameterBuilder(self,name, self.algorithms)

        return builder
    
    def random_forest(self, name):
        if self.algorithms is None:
            self.algorithms = []
        
        # check if the same algorithm is already added
        for i in range(len(self.algorithms)):
            if self.algorithms[i].name == name:
                raise Exception("Algorithm already added: " + name)
        random_forest = RandomForest(name)
        self.algorithms.append(random_forest)
        builder = AlgorithmHyperparameterBuilder(self,name, self.algorithms)

        return builder
    
    def decision_tree(self, name):
        if self.algorithms is None:
            self.algorithms = []
        
        # check if the same algorithm is already added
        for i in range(len(self.algorithms)):
            if self.algorithms[i].name == name:
                raise Exception("Algorithm already added: " + name)
        decision_tree = DecisionTree(name)
        self.algorithms.append(decision_tree)
        builder = AlgorithmHyperparameterBuilder(self,name, self.algorithms)

        return builder
    
    def logistic_regression(self, name):
        if self.algorithms is None:
            self.algorithms = []
        
        # check if the same algorithm is already added
        for i in range(len(self.algorithms)):
            if self.algorithms[i].name == name:
                raise Exception("Algorithm already added: " + name)
        logistic_regression = LogisticRegression(name)
        self.algorithms.append(logistic_regression)
        builder = AlgorithmHyperparameterBuilder(self,name, self.algorithms)

        return builder
    
    def k_nearest_neighbours(self, name):
        if self.algorithms is None:
            self.algorithms = []
        
        # check if the same algorithm is already added
        for i in range(len(self.algorithms)):
            if self.algorithms[i].name == name:
                raise Exception("Algorithm already added: " + name)
        k_nearest_neighbours = KNearestNeighbours(name)
        self.algorithms.append(k_nearest_neighbours)
        builder = AlgorithmHyperparameterBuilder(self,name, self.algorithms)

        return builder
    
    def stochastic_gradient_descent(self, name):
        if self.algorithms is None:
            self.algorithms = []
        
        # check if the same algorithm is already added
        for i in range(len(self.algorithms)):
            if self.algorithms[i].name == name:
                raise Exception("Algorithm already added: " + name)
        stochastic_gradient_descent = StochasticGradientDescent(name)
        self.algorithms.append(stochastic_gradient_descent)
        builder = AlgorithmHyperparameterBuilder(self,name, self.algorithms)

        return builder

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




    def get_algorithms(self):
        return self.algorithms

    def get_notebook_code(self):
        cell = nbformat.v4.new_markdown_cell("## Setting the classifiers")
        self.root.notebook.cells.append(cell)
        code = ""
        if self.algorithms is None:
            return code
        code += "# setting the algorithms\n"
        algorithms_to_remove = []
        # set all algorithms
        for i in range(len(self.algorithms)):
            single_hyperparameters = []
            range_hyperparameter = None
            for j in range(len(self.algorithms[i].hyperparameters)):
                if isinstance(self.algorithms[i].hyperparameters[j], SingleHyperparameter):
                    single_hyperparameters.append(self.algorithms[i].hyperparameters[j])
                elif isinstance(self.algorithms[i].hyperparameters[j], RangeHyperparameter):
                    range_hyperparameter = self.algorithms[i].hyperparameters[j]
            if isinstance(self.algorithms[i], SVM):
                # replace the algorithm with multiple algorithms	
                # remove the algorithm
                if range_hyperparameter is not None:
                    algorithms_to_remove.append(self.algorithms[i])
                    values = []
                    current = range_hyperparameter.min
                    while current < range_hyperparameter.max:
                        values.append(current)
                        current += range_hyperparameter.step
                    for l in range(len(values)):
                        new_algorithm = SVM(self.algorithms[i].name+"_"+range_hyperparameter.name + "_" + str(l+1))
                        new_algorithm.set_hyperparameter(SingleHyperparameter(range_hyperparameter.name, values[l]))
                        
                        for k in range(len(single_hyperparameters)):
                            new_algorithm.set_hyperparameter(single_hyperparameters[k])
                        self.algorithms.append(new_algorithm)
                        code += new_algorithm.name + " = svm.SVC(" + range_hyperparameter.name + "=" + str(values[l]) + ","
                        for e in range(len(single_hyperparameters)):
                            code += single_hyperparameters[e].name + "=" + str(single_hyperparameters[e].name)
                            if e != len(single_hyperparameters) - 1:
                                code += ", "
                        code += ")\n"
                else:
                    # initialize the algorithm svm with the hyperparameters
                    code += self.algorithms[i].name + " = svm.SVC("
                    for j in range(len(self.algorithms[i].hyperparameters)):
                        code += self.algorithms[i].hyperparameters[j].name + "=" + self.algorithms[i].hyperparameters[j].name
                        if j != len(self.algorithms[i].hyperparameters) - 1:
                            code += ", "
                    code += ")\n"
                
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""



                
            elif isinstance(self.algorithms[i], NaiveBayes):
                if range_hyperparameter is not None:
                    algorithms_to_remove.append(self.algorithms[i])
                    values = []
                    current = range_hyperparameter.min
                    while current < range_hyperparameter.max:
                        values.append(current)
                        current += range_hyperparameter.step
                    for l in range(len(values)):
                        new_algorithm = NaiveBayes(self.algorithms[i].name+"_"+range_hyperparameter.name + "_" + str(l+1))
                        new_algorithm.set_hyperparameter(range_hyperparameter)
                        for k in range(len(single_hyperparameters)):
                            new_algorithm.set_hyperparameter(single_hyperparameters[k])
                        self.algorithms.append(new_algorithm)
                        code += new_algorithm.name + " = GaussianNB(" + range_hyperparameter.name + "=" + str(values[l]) + ","
                        for e in range(len(single_hyperparameters)):
                            code += single_hyperparameters[e].name + "=" + str(single_hyperparameters[e].name)
                            if e != len(single_hyperparameters) - 1:
                                code += ", "
                        code += ")\n"
                else:
                    # initialize the algorithm svm with the hyperparameters
                    code += self.algorithms[i].name + " = GaussianNB("
                    for j in range(len(self.algorithms[i].hyperparameters)):
                        code += self.algorithms[i].hyperparameters[j].name + "=" + self.algorithms[i].hyperparameters[j].name
                        if j != len(self.algorithms[i].hyperparameters) - 1:
                            code += ", "
                    code += ")\n"

                
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""


                
            
            elif isinstance(self.algorithms[i], RandomForest):

                if range_hyperparameter is not None:
                    algorithms_to_remove.append(self.algorithms[i])
                    values = []
                    current = range_hyperparameter.min
                    while current < range_hyperparameter.max:
                        values.append(current)
                        current += range_hyperparameter.step
                    for l in range(len(values)):
                        new_algorithm = RandomForest(self.algorithms[i].name+"_"+range_hyperparameter.name + "_" + str(l+1))
                        new_algorithm.set_hyperparameter(range_hyperparameter)
                        for k in range(len(single_hyperparameters)):
                            new_algorithm.set_hyperparameter(single_hyperparameters[k])
                        self.algorithms.append(new_algorithm)
                        code += new_algorithm.name + " = RandomForestClassifier(" + range_hyperparameter.name + "=" + str(values[l]) + ","
                        for e in range(len(single_hyperparameters)):
                            code += single_hyperparameters[e].name + "=" + str(single_hyperparameters[e].name)
                            if e != len(single_hyperparameters) - 1:
                                code += ", "
                        code += ")\n"
                else:
                    # initialize the algorithm svm with the hyperparameters
                    code += self.algorithms[i].name + " = RandomForestClassifier("
                    for j in range(len(self.algorithms[i].hyperparameters)):
                        code += self.algorithms[i].hyperparameters[j].name + "=" + self.algorithms[i].hyperparameters[j].name
                        if j != len(self.algorithms[i].hyperparameters) - 1:
                            code += ", "
                    code += ")\n"

                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""


            
            
            elif isinstance(self.algorithms[i], DecisionTree):
                if range_hyperparameter is not None:
                    algorithms_to_remove.append(self.algorithms[i])
                    values = []
                    current = range_hyperparameter.min
                    while current < range_hyperparameter.max:
                        values.append(current)
                        current += range_hyperparameter.step
                    for l in range(len(values)):
                        new_algorithm = DecisionTree(self.algorithms[i].name+"_"+range_hyperparameter.name + "_" + str(l+1))
                        new_algorithm.set_hyperparameter(range_hyperparameter)
                        for k in range(len(single_hyperparameters)):
                            new_algorithm.set_hyperparameter(single_hyperparameters[k])
                        self.algorithms.append(new_algorithm)
                        code += new_algorithm.name + " = DecisionTreeClassifier(" + range_hyperparameter.name + "=" + str(values[l]) + ","
                        for e in range(len(single_hyperparameters)):
                            code += single_hyperparameters[e].name + "=" + str(single_hyperparameters[e].name)
                            if e != len(single_hyperparameters) - 1:
                                code += ", "
                        code += ")\n"
                else:
                    # initialize the algorithm svm with the hyperparameters
                    code += self.algorithms[i].name + " = DecisionTreeClassifier("
                    for j in range(len(self.algorithms[i].hyperparameters)):
                        code += self.algorithms[i].hyperparameters[j].name + "=" + self.algorithms[i].hyperparameters[j].name
                        if j != len(self.algorithms[i].hyperparameters) - 1:
                            code += ", "
                    code += ")\n"

                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""

            
            elif isinstance(self.algorithms[i], LogisticRegression):
                if range_hyperparameter is not None:
                    algorithms_to_remove.append(self.algorithms[i])
                    values = []
                    current = range_hyperparameter.min
                    while current < range_hyperparameter.max:
                        values.append(current)
                        current += range_hyperparameter.step
                    for l in range(len(values)):
                        new_algorithm = LogisticRegression(self.algorithms[i].name+"_"+range_hyperparameter.name + "_" + str(l+1))
                        new_algorithm.set_hyperparameter(range_hyperparameter)
                        for k in range(len(single_hyperparameters)):
                            new_algorithm.set_hyperparameter(single_hyperparameters[k])
                        self.algorithms.append(new_algorithm)
                        code += new_algorithm.name + " = LogisticRegression(" + range_hyperparameter.name + "=" + str(values[l]) + ","
                        for e in range(len(single_hyperparameters)):
                            code += single_hyperparameters[e].name + "=" + str(single_hyperparameters[e].name)
                            if e != len(single_hyperparameters) - 1:
                                code += ", "
                        code += ")\n"
                else:
                    # initialize the algorithm svm with the hyperparameters
                    code += self.algorithms[i].name + " = LogisticRegression("
                    for j in range(len(self.algorithms[i].hyperparameters)):
                        code += self.algorithms[i].hyperparameters[j].name + "=" + self.algorithms[i].hyperparameters[j].name
                        if j != len(self.algorithms[i].hyperparameters) - 1:
                            code += ", "
                    code += ")\n"

                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""


            
            elif isinstance(self.algorithms[i], KNearestNeighbours):
                if range_hyperparameter is not None:
                    algorithms_to_remove.append(self.algorithms[i])
                    values = []
                    current = range_hyperparameter.min
                    while current < range_hyperparameter.max:
                        values.append(current)
                        current += range_hyperparameter.step
                    for l in range(len(values)):
                        new_algorithm = KNearestNeighbours(self.algorithms[i].name+"_"+range_hyperparameter.name + "_" + str(l+1))
                        new_algorithm.set_hyperparameter(range_hyperparameter)
                        for k in range(len(single_hyperparameters)):
                            new_algorithm.set_hyperparameter(single_hyperparameters[k])
                        self.algorithms.append(new_algorithm)
                        code += new_algorithm.name + " = KNeighborsClassifier(" + range_hyperparameter.name + "=" + str(values[l]) + ","
                        for e in range(len(single_hyperparameters)):
                            code += single_hyperparameters[e].name + "=" + str(single_hyperparameters[e].name)
                            if e != len(single_hyperparameters) - 1:
                                code += ", "
                        code += ")\n"
                else:
                    # initialize the algorithm svm with the hyperparameters
                    code += self.algorithms[i].name + " = KNeighborsClassifier("
                    for j in range(len(self.algorithms[i].hyperparameters)):
                        code += self.algorithms[i].hyperparameters[j].name + "=" + self.algorithms[i].hyperparameters[j].name
                        if j != len(self.algorithms[i].hyperparameters) - 1:
                            code += ", "
                    code += ")\n"

                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""


            
            elif isinstance(self.algorithms[i], StochasticGradientDescent):
                if range_hyperparameter is not None:
                    algorithms_to_remove.append(self.algorithms[i])
                    values = []
                    current = range_hyperparameter.min
                    while current < range_hyperparameter.max:
                        values.append(current)
                        current += range_hyperparameter.step
                    for l in range(len(values)):
                        new_algorithm = StochasticGradientDescent(self.algorithms[i].name+"_"+range_hyperparameter.name + "_" + str(l+1))
                        new_algorithm.set_hyperparameter(range_hyperparameter)
                        for k in range(len(single_hyperparameters)):
                            new_algorithm.set_hyperparameter(single_hyperparameters[k])
                        self.algorithms.append(new_algorithm)
                        code += new_algorithm.name + " = SGDClassifier(" + range_hyperparameter.name + "=" + str(values[l]) + ","
                        for e in range(len(single_hyperparameters)):
                            code += single_hyperparameters[e].name + "=" + str(single_hyperparameters[e].name)
                            if e != len(single_hyperparameters) - 1:
                                code += ", "
                        code += ")\n"
                else:
                    # initialize the algorithm svm with the hyperparameters
                    code += self.algorithms[i].name + " = SGDClassifier("
                    for j in range(len(self.algorithms[i].hyperparameters)):
                        code += self.algorithms[i].hyperparameters[j].name + "=" + self.algorithms[i].hyperparameters[j].name
                        if j != len(self.algorithms[i].hyperparameters) - 1:
                            code += ", "
                    code += ")\n"

                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            
            else:
                raise Exception("Invalid algorithm")
        
        # remove the algorithms that were created for the hyperparameter tuning
        for i in range(len(algorithms_to_remove)):
            self.algorithms.remove(algorithms_to_remove[i])

            
        # train the algorithms
        if self.actions is not None:
            if "train" in self.actions:
                code += "# training the algorithms\n"
                for i in range(len(self.algorithms)):
                    code += "start_" + self.algorithms[i].name + " = time.time()\n"
                    code += self.algorithms[i].name + ".fit(X_train, y_train)\n"
                    code += "end_" + self.algorithms[i].name + " = time.time()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            if "predict" in self.actions:
                code += "# predicting the algorithms\n"
                for i in range(len(self.algorithms)):
                    code += "y_pred_" + self.algorithms[i].name +" = " + self.algorithms[i].name + ".predict(X_test)\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""



            

        





            
        return code


    def end_algorithms(self):
        return self.root