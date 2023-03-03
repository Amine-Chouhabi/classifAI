

from model.visualisation.PieChart import PieChart
from model.visualisation.BarChart import BarChart
from model.visualisation.Graph import Graph
from VisualisationTypeBuilder import VisualisationTypeBuilder

import nbformat



class VizualisationBuilder:
    def __init__(self, root, algorithms):
        self.root = root
        self.algorithms = algorithms
        self.vizualisations = {}
        self.target = ""

    def visualize_accuracy(self):
        builder = VisualisationTypeBuilder(self, "accuracy")
        return builder
    
    def visualize_loss(self):
        builder = VisualisationTypeBuilder(self, "loss")
        return builder
    
    def visualize_precision(self):
        builder = VisualisationTypeBuilder(self, "precision")
        return builder

    def visualize_recall(self):
        builder = VisualisationTypeBuilder(self, "recall")
        return builder

    def visualize_f1_score(self):
        builder = VisualisationTypeBuilder(self, "f1")
        return builder
    
    def visualize_training_duration(self):
        builder = VisualisationTypeBuilder(self, "training_duration")
        return builder

    

    
    

        

    def see_recap(self):
        self.target = "rank"
        return self

    
    

    def end_vizualisation(self):
        return self.root

    
    def get_notebook_code(self):
        cell = nbformat.v4.new_markdown_cell("## Visualisation of the results")
        self.root.notebook.cells.append(cell)
        code = ""
        if self.vizualisations is None:
            return code
        code += "# visualizing the results\n"
        print(self.vizualisations.items())

        # loop through dictionary and add code for each visualisation
        for key, value in self.vizualisations.items():
            if key == "accuracy":

                n = value[1]
                # plot only the accuracies higher than n
                code += "accuracies = []\n"
                code += "algorithms = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "if metrics.accuracy_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ") > " + str(n) + ":\n"
                    code += "\taccuracies.append(metrics.accuracy_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + "))\n"
                    code += "\talgorithms.append('" + self.algorithms.get_algorithms()[j].name + "')\n"
                if isinstance(value[0], PieChart):
                    # figure size
                    code += "plt.figure(figsize=(10, 10))\n"                        
                    code += "plt.pie(accuracies, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"                                   
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Accuracy of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, accuracies)\n"
                    # title
                    code += "plt.title('Accuracy of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, accuracies)\n"
                    # title
                    code += "plt.title('Accuracy of the algorithms')\n"
                    code += "plt.show()\n"
                
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "loss":
                n = value[1]
                # plot only the losses lower than n
                code += "losses = []\n"
                code += "algorithms = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "if metrics.log_loss(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ") < " + str(n) + ":\n"
                    code += "\tlosses.append(metrics.log_loss(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + "))\n"
                    code += "\talgorithms.append('" + self.algorithms.get_algorithms()[j].name + "')\n"
                if isinstance(value[0], PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(losses, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Loss of the algorithms')\n"
            
                    code += "plt.show()\n"
                elif isinstance(value[0], BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, losses)\n"
                    # title
                    code += "plt.title('Loss of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, losses)\n"
                    # title
                    code += "plt.title('Loss of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "precision":
                n = value[1]
                # plot only the precisions higher than n
                code += "precisions = []\n"
                code += "algorithms = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "if metrics.precision_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ") > " + str(n) + ":\n"
                    code += "\tprecisions.append(metrics.precision_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + "))\n"
                    code += "\talgorithms.append('" + self.algorithms.get_algorithms()[j].name + "')\n"
                if isinstance(value[0], PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(precisions, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Precision of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, precisions)\n"
                    # title
                    code += "plt.title('Precision of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, precisions)\n"
                    # title
                    code += "plt.title('Precision of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "recall":
                n = value[1]
                # plot only the recalls higher than n
                code += "recalls = []\n"
                code += "algorithms = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "if metrics.recall_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ") > " + str(n) + ":\n"
                    code += "\trecalls.append(metrics.recall_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + "))\n"
                    code += "\talgorithms.append('" + self.algorithms.get_algorithms()[j].name + "')\n"
                if isinstance(value[0], PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(recalls, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Recall of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, recalls)\n"
                    # title
                    code += "plt.title('Recall of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, recalls)\n"
                    # title
                    code += "plt.title('Recall of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "f1":
                n = value[1]
                # plot only the f1s higher than n
                code += "f1s = []\n"
                code += "algorithms = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "if metrics.f1_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + ") > " + str(n) + ":\n"
                    code += "\tf1s.append(metrics.f1_score(ytest, y_pred_" + self.algorithms.get_algorithms()[j].name + "))\n"
                    code += "\talgorithms.append('" + self.algorithms.get_algorithms()[j].name + "')\n"
                if isinstance(value[0], PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(f1s, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('F1 of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, f1s)\n"
                    # title
                    code += "plt.title('F1_score of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, f1s)\n"
                    # title
                    code += "plt.title('F1_score of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif key == "training_duration":
                n = value[1]
                # plot only the training durations higher than n
                code += "durations = []\n"
                code += "algorithms = []\n"
                for j in range(len(self.algorithms.get_algorithms())):
                    code += "if end_" + self.algorithms.get_algorithms()[j].name +"- start_"+ self.algorithms.get_algorithms()[j].name + " > " + str(n) + ":\n"
                    code += "\tdurations.append(end_" + self.algorithms.get_algorithms()[j].name +"- start_"+ self.algorithms.get_algorithms()[j].name + ")\n"
                    code += "\talgorithms.append('" + self.algorithms.get_algorithms()[j].name + "')\n"
                if isinstance(value[0], PieChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.pie(durations, labels=algorithms, autopct='%1.1f%%', shadow=True, startangle=90)\n"
                    code += "plt.axis('equal')\n"
                    # title
                    code += "plt.title('Training duration of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], BarChart):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.bar(algorithms, durations)\n"
                    # title
                    code += "plt.title('Training duration of the algorithms')\n"
                    code += "plt.show()\n"
                elif isinstance(value[0], Graph):
                    code += "plt.figure(figsize=(10, 10))\n"  
                    code += "plt.plot(algorithms, durations)\n"
                    # title
                    code += "plt.title('Training duration of the algorithms')\n"
                    code += "plt.show()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
        if self.target == "rank":

            
            code += "table = [[]]\n"
            for key in self.vizualisations:
                code += "table[0].append(['" + key + "'])\n"
            for j in range(len(self.algorithms.get_algorithms())):
                code += "table.append(['" + self.algorithms.get_algorithms()[j].name + "'])\n"
                for key in self.vizualisations:
                    if key == "precision":
                        code += "table[" + str(j+1) + "].append(precisions[" + str(j) + "])\n"
                    elif key == "accuracy":
                        code += "table[" + str(j+1) + "].append(accuracies[" + str(j) + "])\n"
                    elif key == "recall":
                        code += "table[" + str(j+1) + "].append(recalls[" + str(j) + "])\n"
                    elif key == "f1":
                        code += "table[" + str(j+1) + "].append(f1s[" + str(j) + "])\n"
                    elif key == "training_duration":
                        code += "table[" + str(j+1) + "].append(durations[" + str(j) + "])\n"
            

            
            code += "print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))\n"
            cell = nbformat.v4.new_code_cell(code)
            self.root.notebook.cells.append(cell)
            code = ""

            
        
            
                
                    
        return code
            
        

