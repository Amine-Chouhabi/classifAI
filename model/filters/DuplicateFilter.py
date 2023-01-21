#Filter class to remove duplicate values from dataframe with pandas

from model.filters.Filter import Filter

class DuplicateFilter(Filter):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "DuplicateFilter"

    def __repr__(self) :
        return self.__str__()
    
