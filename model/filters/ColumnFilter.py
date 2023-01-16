# Filter class to remove unnecessary columns from dataframe

from filters.Filter import Filter


class ColumnFilter(Filter):
    def __init__(self, columns):
        super().__init__()
        self.columns = columns
    
    def __str__(self):
        return "ColumnFilter: " + str(self.columns)
    
    def __repr__(self) :
        return self.__str__()
    
