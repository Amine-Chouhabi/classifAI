
from Validators.DataSelectionValidator import DataSelectionValidator

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from model.dataSelection.DataSelector import DataSelector
from model.dataSelection.DataSetEntry import DataSetEntry
from model.filters.Filter import Filter
from model.filters.NullFilter import NullFilter
from model.filters.OutliersFilter import OutliersFilter
from model.filters.DuplicateFilter import DuplicateFilter
from model.filters.ColumnFilter import ColumnFilter
from model.filters.RowFilter import RowFilter

import nbformat


NULL_FILTER = 0
OUTLIERS_FILTER = 1
DUPLICATES_FILTER = 2



class DataSelectorBuilder:
    def __init__(self, root):
        self.root = root
        self.data_selector = None
        self.validator = DataSelectionValidator()
        self.column_code = ""

    def add_entry(self, path):
        if self.data_selector is None:
            self.data_selector = DataSelector([])
        # check if the file is not csv throw exception
        if (path.endswith(".csv") == False):
            raise ValueError("The file should be csv")
        self.data_selector.add_entry(DataSetEntry(path))
        return self
    
    def remove_null_values(self):
        self.validator.entry_is_exist(self.data_selector)
        self.data_selector.add_filter(NullFilter())
        return self
    
    def remove_outliers(self):
        self.validator.entry_is_exist(self.data_selector)
        self.data_selector.add_filter(OutliersFilter())
        return self
    
    def remove_duplicates(self):
        self.validator.entry_is_exist(self.data_selector)
        self.data_selector.add_filter(DuplicateFilter())
        return self
    
    def remove_columns(self, columns):
        self.validator.entry_is_exist(self.data_selector)
        self.data_selector.add_filter(ColumnFilter(columns))
        return self

    def remove_rows(self, rows):
        self.validator.entry_is_exist(self.data_selector)
        self.data_selector.add_filter(RowFilter(rows))
        return self    

    def rename_column(self, old_name, new_name):
        self.validator.entry_is_exist(self.data_selector)
        self.column_code += "# renaming columns\n"
        self.column_code += "data = data.rename(columns={'" + old_name + "':'" + new_name + "'})\n"
        
        return self

    def end_selector(self):
        self.validator.entry_is_exist(self.data_selector)
        return self.root

    def get_notebook_code(self):
        
        cell = nbformat.v4.new_markdown_cell("## Data selection")
        self.root.notebook.cells.append(cell)
        code = ""
        if self.data_selector is None:
            return code
        code += "# reading the data\n"
        # merge all data entries in one dataframe
        code += "data = None\n"
        for i in range(len(self.data_selector.data_entries)):
            
            code += "data" + str(i) + " = pd.read_csv('" + self.data_selector.data_entries[i].path + "')\n"
            code += "data = pd.concat([data, data" + str(i) + "])\n"
        cell = nbformat.v4.new_code_cell(code)
        self.root.notebook.cells.append(cell)
        if self.column_code != "":
            cell = nbformat.v4.new_code_cell(self.column_code)
            self.root.notebook.cells.append(cell)
        code = ""
        
        # apply all filters
        for i in range(len(self.data_selector.filters)):
            if isinstance(self.data_selector.filters[i], NullFilter):
                code += "# removing null values\n"
                code += "data = data.dropna()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif isinstance(self.data_selector.filters[i], OutliersFilter):
                code += "# removing outliers\n"
                code += "data = data[(np.abs(stats.zscore(data)) < 3).all(axis=1)]\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif isinstance(self.data_selector.filters[i], DuplicateFilter):
                code += "# removing duplicates\n"
                code += "data = data.drop_duplicates()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif isinstance(self.data_selector.filters[i], RowFilter):
                code += "# removing rows\n"
                code += "data = data.drop(" + str(self.data_selector.filters[i].rows) + ")\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif isinstance(self.data_selector.filters[i], ColumnFilter):
                code += "# removing columns\n"
                code += "data = data.drop(columns=['"
                code += "', '".join(self.data_selector.filters[i].columns)
                code += "'])\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
        return code

    
    
    def __str__(self):
        return "DataSelectorBuilder: " + str(self.data_selector)

    def __repr__(self):
        return self.__str__()
    
    

        


