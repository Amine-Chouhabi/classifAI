import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\visualisation\\Visualisation.py")
sys.path.append(file_dir)

from PieChart import PieChart
from BarChart import BarChart
from Graph import Graph
from VisualisationTypeBuilder import VisualisationTypeBuilder

import nbformat



class VizualisationBuilder:
    def __init__(self, root, algorithms):
        self.root = root
        self.algorithms = algorithms
        self.vizualisations = {}
        self.target = []

    def visualize_accuracy(self):
        self.target.append("accuracy")
        builder = VisualisationTypeBuilder(self, "accuracy")
        return builder
    
    def visualize_loss(self):
        self.target.append("loss")
        builder = VisualisationTypeBuilder(self, "loss")
        return builder
    
    def visualize_precision(self):
        self.target.append("precision")
        builder = VisualisationTypeBuilder(self, "precision")
        return builder

    def visualize_recall(self):
        self.target.append("recall")
        builder = VisualisationTypeBuilder(self, "recall")
        return builder

    def visualize_f1_score(self):
        self.target.append("f1")
        builder = VisualisationTypeBuilder(self, "f1")
        return builder
    
    def visualize_training_duration(self):
        self.target.append("training_duration")
        builder = VisualisationTypeBuilder(self, "training_duration")
        return builder

    
    

    def end_vizualisation(self):
        return self.root

    
    def get_notebook_code(self):
        cell = nbformat.v4.new_markdown_cell("## Visualisation of the results")
        self.root.notebook.cells.append(cell)
        code = ""
        if self.vizualisations is None:
            return code
        code += "# visualizing the results\n"
        # get the algorithms names in a list
        code += "algorithms = []\n"
        for k in range(len(self.algorithms.get_algorithms())):
            code += "algorithms.append('" + self.algorithms.get_algorithms()[k].name + "')\n"
        cell = nbformat.v4.new_code_cell(code)
        self.root.notebook.cells.append(cell)
        code = ""

        # loop through dictionary and add code for each visualisation
        for key, value in self.vizualisations.items():
            if key == "accuracy":
                code += "accuracies = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "accuracies.append(metrics.accuracy_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + "))\n"
                if isinstance(value, PieChart):
                    # figure size
                    code += "plt.figure(figsize=(10, 10))\n"                        
                    code += "plt.pie(accuracies, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"                                   
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Accuracy of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, accuracies)\n"
                    # title
                    code += "plt.title('Accuracy of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, accuracies)\n"
                    # title
                    code += "plt.title('Accuracy of the algorithms')\n"
                    code += "plt.show()\n"
                
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "loss":
                code += "losses = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "losses.append(metrics.log_loss(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + "))\n"
                if isinstance(value, PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(losses, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Loss of the algorithms')\n"
            
                    code += "plt.show()\n"
                elif isinstance(value, BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, losses)\n"
                    # title
                    code += "plt.title('Loss of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, losses)\n"
                    # title
                    code += "plt.title('Loss of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "precision":
                code += "precisions = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "precisions.append(metrics.precision_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ", pos_label=\"1\"))\n"
                if isinstance(value, PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(precisions, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Precision of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, precisions)\n"
                    # title
                    code += "plt.title('Precision of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, precisions)\n"
                    # title
                    code += "plt.title('Precision of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "recall":
                code += "recalls = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "recalls.append(metrics.recall_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ", pos_label=\"1\"))\n"
                if isinstance(value, PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(recalls, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Recall of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, recalls)\n"
                    # title
                    code += "plt.title('Recall of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, recalls)\n"
                    # title
                    code += "plt.title('Recall of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "f1":
                code += "f1s = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "f1s.append(metrics.f1_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ", pos_label=\"1\"))\n"
                if isinstance(value, PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(f1s, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('F1 of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, f1s)\n"
                    # title
                    code += "plt.title('F1_score of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, f1s)\n"
                    # title
                    code += "plt.title('F1_score of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "training_duration":
                code += "durations = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "durations.append(end_" + self.algorithms.get_algorithms()[j].name +"-" + "start_"+ self.algorithms.get_algorithms()[j].name+")\n"
                if isinstance(value, PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(durations, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Training duration of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, durations)\n"
                    # title
                    code += "plt.title('Training duration of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value, Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, durations)\n"
                    # title
                    code += "plt.title('Training duration of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""

            
        
            
                
                    
        return code
            
        

