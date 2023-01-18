import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\visualisation\\Visualisation.py")
sys.path.append(file_dir)

from PieChart import PieChart
from BarChart import BarChart
from Graph import Graph


class VizualisationBuilder:
    def __init__(self, root, algorithms):
        self.root = root
        self.algorithms = algorithms
        self.vizualisation = None
        self.target = []

    def add_pie_chart(self):
        self.vizualisation = PieChart()
        return self

    def add_bar_chart(self):
        self.vizualisation = BarChart()
        return self

    def add_graph(self):
        self.vizualisation = Graph()
        return self

    def visualize_accuracy(self):
        self.target.append("accuracy")
        return self
    
    def visualize_loss(self):
        self.target.append("loss")
        return self
    
    def visualize_precision(self):
        self.target.append("precision")
        return self

    def visualize_recall(self):
        self.target.append("recall")
        return self

    def visualize_f1_score(self):
        self.target.append("f1")
        return self
    
    def visualize_training_duration(self):
        self.target.append("training_duration")
        return self

    
    

    def end_vizualisation(self):
        return self.root

    
    def get_notebook_code(self):
        code = ""
        if self.vizualisation is None:
            return code
        code += "# visualizing the results\n"
        for i in range(len(self.target)):
                if self.target[i] == "accuracy":
                    code += "accuracies = []\n"
                    code += "algorithms = []\n"
                    for j in range(len(self.algorithms.get_algorithms())):
                        code += "algorithms.append('" + self.algorithms.get_algorithms()[j].name + "')\n"
                        code += "accuracies.append(metrics.accuracy_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + "))\n"
                    if isinstance(self.vizualisation, PieChart):
                        code += "plt.pie(accuracies, labels=algorithms)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, BarChart):
                        code += "plt.bar(algorithms, accuracies)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, Graph):
                        code += "plt.plot(algorithms, accuracies)\n"
                        code += "plt.show()\n"
                if self.target[i] == "loss":
                    code += "losses = []\n"
                    for j in range(len(self.algorithms.get_algorithms())):
                        
                        code += "losses.append(metrics.log_loss(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ", pos_label=\"1\"))\n"
                    if isinstance(self.vizualisation, PieChart):
                        code += "plt.pie(losses, labels=algorithms)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, BarChart):
                        code += "plt.bar(algorithms, losses)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, Graph):
                        code += "plt.plot(algorithms, losses)\n"
                        code += "plt.show()\n"
                        
                if self.target[i] == "precision":
                    code += "precisions = []\n"
                    for j in range(len(self.algorithms.get_algorithms())):
                        
                        code += "precisions.append(metrics.precision_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ", pos_label=\"1\"))\n"
                    if isinstance(self.vizualisation, PieChart):
                        code += "plt.pie(precisions, labels=algorithms)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, BarChart):
                        code += "plt.bar(algorithms, precisions)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, Graph):
                        code += "plt.plot(algorithms, precisions)\n"
                        code += "plt.show()\n"
                if self.target[i] == "recall":
                    code += "recalls = []\n"
                    for j in range(len(self.algorithms.get_algorithms())):
                        
                        code += "recalls.append(metrics.recall_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ", pos_label=\"1\"))\n"
                    if isinstance(self.vizualisation, PieChart):
                        code += "plt.pie(recalls, labels=algorithms)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, BarChart):
                        code += "plt.bar(algorithms, recalls)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, Graph):
                        code += "plt.plot(algorithms, recalls)\n"
                        code += "plt.show()\n"
                if self.target[i] == "f1":
                    code += "f1s = []\n"
                    for j in range(len(self.algorithms.get_algorithms())):
                        
                        code += "f1s.append(metrics.f1_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ", pos_label=\"1\"))\n"
                    if isinstance(self.vizualisation, PieChart):
                        code += "plt.pie(f1s, labels=algorithms)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, BarChart):
                        code += "plt.bar(algorithms, f1s)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, Graph):
                        code += "plt.plot(algorithms, f1s)\n"
                        code += "plt.show()\n"
                if self.target[i] == "training_duration":
                    code += "training_durations = []\n"
                    for j in range(len(self.algorithms.get_algorithms())):
                        
                        code += "training_durations.append(start_"+ self.algorithms.get_algorithms()[j].name + " - end_"+self.algorithms.get_algorithms()[j].name + ")\n"
                    if isinstance(self.vizualisation, PieChart):
                        code += "plt.pie(training_durations, labels=algorithms)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, BarChart):
                        code += "plt.bar(algorithms, training_durations)\n"
                        code += "plt.show()\n"
                    elif isinstance(self.vizualisation, Graph):
                        code += "plt.plot(algorithms, training_durations)\n"
                        code += "plt.show()\n"

        
            
                
                    
        return code
            
        

