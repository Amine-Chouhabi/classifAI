# class to process dataSets from dataSelector

class DataProcessor:
    def __init__(self, processors = []):
        self.processors = processors
    
    def __str__(self):
        return "DataProcessor: " + str(self.processors)
    
    def __repr__(self):
        return self.__str__()
    
    def add_processor(self, processor):
        self.processors.append(processor)
    

        
    
