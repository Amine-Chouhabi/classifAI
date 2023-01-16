# Filter class to remove null values from dataframe with pandas

from filters.Filter import Filter

class NullFilter(Filter):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "NullFilter"
    
    def __repr__(self) :
        return self.__str__()