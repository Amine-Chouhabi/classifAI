# Filter class to remove extreme values from dataframe with pandas

from model.filters.Filter import Filter


class OutliersFilter(Filter):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "OutliersFilter"
    
    def __repr__(self) :
        return self.__str__()
    
