import os
import sys

file_dir = os.path.dirname("C:\\Users\\user\\Desktop\\DSL-LAB2\\model\\DataSelector.py")
sys.path.append(file_dir)

from dataSelection.DataSelector import DataSelector
from dataSelection.DataSetEntry import DataSetEntry
from filters.Filter import Filter
from filters.NullFilter import NullFilter
from filters.OutliersFilter import OutliersFilter
from filters.DuplicateFilter import DuplicateFilter
from filters.ColumnFilter import ColumnFilter
from filters.RowFilter import RowFilter

NULL_FILTER = 0
OUTLIERS_FILTER = 1
DUPLICATES_FILTER = 2



class DataSelectorBuilder:
    def __init__(self, root):
        self.root = root
        self.data_selector = None

    def add_entry(self, path):
        if self.data_selector is None:
            self.data_selector = DataSelector([])
        self.data_selector.add_entry(DataSetEntry(path))
        return self
    
    def remove_null_values(self):
        if self.data_selector is None:
            self.data_selector = DataSelector([])
        self.data_selector.add_filter(NullFilter())
        return self
    
    def remove_outliers(self):
        if self.data_selector is None:
            self.data_selector = DataSelector([])
        self.data_selector.add_filter(OutliersFilter())
        return self
    
    def remove_duplicates(self):
        if self.data_selector is None:
            self.data_selector = DataSelector([])
        self.data_selector.add_filter(DuplicateFilter())
        return self
    
    def remove_columns(self, columns):
        if self.data_selector is None:
            self.data_selector = DataSelector([])
        self.data_selector.add_filter(ColumnFilter(columns))
        return self

    def remove_rows(self, rows):
        if self.data_selector is None:
            self.data_selector = DataSelector([])
        self.data_selector.add_filter(RowFilter(rows))
        return self    

    def end_selector(self):
        return self.root

    def get_notebook_code(self):
        code = ""
        if self.data_selector is None:
            return code
        code += "# reading the data\n"
        # merge all data entries in one dataframe
        code += "data = None\n"
        for i in range(len(self.data_selector.data_entries)):
            
            code += "data" + str(i) + " = pd.read_csv('" + self.data_selector.data_entries[i].path + "')\n"
            code += "data = pd.concat([data, data" + str(i) + "])\n"
        
        # apply all filters
        for i in range(len(self.data_selector.filters)):
            if isinstance(self.data_selector.filters[i], NullFilter):
                code += "# removing null values\n"
                code += "data = data.dropna()\n"
            elif isinstance(self.data_selector.filters[i], OutliersFilter):
                code += "# removing outliers\n"
                code += "data = data[(np.abs(stats.zscore(data)) < 3).all(axis=1)]\n"
            elif isinstance(self.data_selector.filters[i], DuplicateFilter):
                code += "# removing duplicates\n"
                code += "data = data.drop_duplicates()\n"
            elif isinstance(self.data_selector.filters[i], RowFilter):
                code += "# removing rows\n"
                code += "data = data.drop([" + ", ".join(self.data_selector.filters[i].rows) + "])\n"
            elif isinstance(self.data_selector.filters[i], ColumnFilter):
                code += "# removing columns\n"
                code += "data = data.drop(columns=['"
                code += "', '".join(self.data_selector.filters[i].columns)
                code += "'])\n"
        return code

    
    
    def __str__(self):
        return "DataSelectorBuilder: " + str(self.data_selector)

    def __repr__(self):
        return self.__str__()
    
    

        


