# class for a dataset entry from a csv file or image file


class DataSetEntry:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "DataSetEntry: " + self.path
    
    def __repr__(self):
        return self.__str__()









    
    

    
    