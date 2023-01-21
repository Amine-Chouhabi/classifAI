# Filter class to remove extreme values from dataframe with pandas

from model.filters.Filter import Filter


class RowFilter(Filter):
    def __init__(self, rows):
        super().__init__()
        self.rows = rows
    
    def __str__(self):
        return "RowFilter"
    
    def __repr__(self) :
        return self.__str__()
    
