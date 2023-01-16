# class for comparing classification algorithms


from dataSelection.DataSelector import DataSelector
from processors.DataProcessor import DataProcessor
from algorithms.Algorithm import Algorithm


class AlgoComparison:
    def __init__(self, dataSelector, dataProcessor, algorithms):
        self.dataSelector = dataSelector
        self.dataProcessor = dataProcessor
        self.algorithms = algorithms

    def __str__(self):
        return "AlgoComparison: " + str(self.dataSelector) + " " + str(self.dataProcessor) + " " + str(self.algorithms)

    def __repr__(self):
        return self.__str__()

