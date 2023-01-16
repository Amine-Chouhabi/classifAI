# Class for noteboook cells


from CellType import CellType

class Cell:
    """Class for notebook cells"""
    def __init__(self, number ,cell_type, source):
        self.cell_type = cell_type
        self.number = number
        self.source = source

    def __str__(self):
        return "Cell: " + self.cell_type.name + " " + self.source

    def __repr__(self):
        return self.__str__()
    
    def get_cell_type(self):
        return self.cell_type
    
    def get_number(self):
        return self.number

    def get_source(self):
        return self.source

    
