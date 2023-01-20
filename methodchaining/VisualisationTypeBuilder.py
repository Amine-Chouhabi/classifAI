import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\ClassifAI\\model\\visualisation\\Visualisation.py")
sys.path.append(file_dir)

from PieChart import PieChart
from BarChart import BarChart
from Graph import Graph

class VisualisationTypeBuilder:
    def __init__(self, root, target):
        self.root = root
        self.target = target
        self.visualisation = None

    def as_pie_chart(self):
        self.visualisation = PieChart()
        self.root.vizualisations[self.target] = self.visualisation
        return self.root

    def as_bar_chart(self):
        self.visualisation = BarChart()
        self.root.vizualisations[self.target] = self.visualisation
        return self.root

    def as_graph(self):
        self.visualisation = Graph()
        self.root.vizualisations[self.target] = self.visualisation
        return self.root
