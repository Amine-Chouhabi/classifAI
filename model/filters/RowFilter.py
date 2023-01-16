# Filter class to remove extreme values from dataframe with pandas

from filters.Filter import Filter


class RowFilter(Filter):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "RowFilter"
    
    def __repr__(self) :
        return self.__str__()
    
