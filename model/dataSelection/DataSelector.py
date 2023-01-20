# DataSelector class with DataEntries 

from model.dataSelection.DataSetEntry import DataSetEntry
class DataSelector:
    """Class for selecting data from a list of DataEntry objects"""
    def __init__(self, data_entries, filters= []):
        self.data_entries = data_entries
        self.filters = filters
    
    def __str__(self):
        return "DataSelector: " + str(self.data_entries) + " " + str(self.filters)
    
    def __repr__(self):
        return self.__str__()
    
    def set_entries(self, data_entries):
        self.data_entries = data_entries
    
    def set_filters(self, filters):
        self.filters = filters
    
    def add_filter(self, filter):
        self.filters.append(filter)
    
    def add_entry(self, data_entry):
        self.data_entries.append(data_entry)
    



    


    



