
from DataSelectorBuilder import DataSelectorBuilder
from DataProcessorBuilder import DataProcessorBuilder
from HyperParametersBuilder import HyperParametersBuilder
from AlgorithmsBuilder import AlgorithmsBuilder
from VizualisationBuilder import VizualisationBuilder

import nbformat



class AlgoComparisonBuilder:
    def __init__(self, name):
        self.name = name
        self.data_selector = None
        self.data_processor = None
        self.hyper_parameters = None
        self.algorithms = None
        self.vizualisations = None
        self.notebook = nbformat.v4.new_notebook()
    
    def select_data(self):
        self.data_selector = DataSelectorBuilder(self)
        return self.data_selector

    def process_data(self):
        self.data_processor = DataProcessorBuilder(self)
        return self.data_processor
    
    def set_hyper_parameters(self):
        self.hyper_parameters = HyperParametersBuilder(self)
        return self.hyper_parameters
    
    def set_algorithms(self):
        self.algorithms = AlgorithmsBuilder(self,self.hyper_parameters)
        return self.algorithms
    
    def set_vizualisation(self):
        self.vizualisations = VizualisationBuilder(self, self.algorithms)
        return self.vizualisations

    def add_markdown(self, text):
        cell = nbformat.v4.new_markdown_cell(text)
        self.notebook.cells.append(cell)
        return self

    


    def get_notebook_code(self):
        cell = nbformat.v4.new_markdown_cell("ClassifAI - Notebook to compare machine learning classifiers")
        self.notebook.cells.append(cell)

        code = "import pandas as pd \n"
        code += "import numpy as np \n"
        code += "from scipy import stats \n"
        code += "from sklearn.model_selection import train_test_split\n"
        code += "import time\n"
        code += "import matplotlib.pyplot as plt\n"
        code += "from sklearn.model_selection import train_test_split\n"
        code += "from sklearn.tree import DecisionTreeClassifier\n"
        code += "from sklearn.linear_model import LogisticRegression\n"
        code += "from sklearn.ensemble import RandomForestClassifier\n"
        code += "from sklearn.neighbors import KNeighborsClassifier\n"
        code += "from sklearn import svm\n"
        code += "from sklearn.naive_bayes import BernoulliNB\n"
        code += "from sklearn.naive_bayes import GaussianNB\n"
        code += "from sklearn.metrics import accuracy_score\n"
        code += "from sklearn import metrics\n"
        code += "from tabulateimport tabulate\n"
        cell = nbformat.v4.new_code_cell(code)
        self.notebook.cells.append(cell)
        code = ""




        if self.data_selector is not None:
            code += self.data_selector.get_notebook_code()
        if self.data_processor is not None:
            code += self.data_processor.get_notebook_code()
        if self.hyper_parameters is not None:
            code += self.hyper_parameters.get_notebook_code()
        if self.algorithms is not None:
            code += self.algorithms.get_notebook_code()
        if self.vizualisations is not None:
            code += self.vizualisations.get_notebook_code()


        file_name = self.name + ".ipynb"

        with open("../"+file_name, "w") as f:
            nbformat.write(self.notebook, f)




