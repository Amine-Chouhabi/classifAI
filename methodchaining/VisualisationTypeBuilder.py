
from model.visualisation.PieChart import PieChart
from model.visualisation.BarChart import BarChart
from model.visualisation.Graph import Graph

class VisualisationTypeBuilder:
    def __init__(self, root, target):
        self.root = root
        self.target = target
        self.visualisation = None

    def as_pie_chart(self):
        self.visualisation = PieChart()
        self.root.vizualisations[self.target] = self.visualisation
        return self

    def as_bar_chart(self):
        self.visualisation = BarChart()
        self.root.vizualisations[self.target] = self.visualisation
        return self

    def as_graph(self):
        self.visualisation = Graph()
        self.root.vizualisations[self.target] = self.visualisation
        return self
    
    def from_(self, value):
        self.root.vizualisations[self.target] = (self.visualisation, value)
        return self.root
    

    def visualize_loss(self):
        self.root.vizualisations[self.target] = (self.visualisation, 0)
        return self.root.visualize_loss()
    
    def visualize_accuracy(self):
        self.root.vizualisations[self.target] = (self.visualisation, 0)
        return self.root.visualize_accuracy()
    
    def visualize_precision(self):
        self.root.vizualisations[self.target] = (self.visualisation, 0)
        return self.root.visualize_precision()
    
    def visualize_recall(self):
        self.root.vizualisations[self.target] = (self.visualisation, 0)
        return self.root.visualize_recall()
    
    def visualize_f1_score(self):
        self.root.vizualisations[self.target] = (self.visualisation, 0)
        return self.root.visualize_f1_score()
    
    def visualize_training_duration(self):
        self.root.vizualisations[self.target] = (self.visualisation, 0)
        return self.root.visualize_training_duration()
    
    

    
