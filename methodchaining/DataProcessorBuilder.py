

from methodchaining.Validators.DataProcessingValidator import DataProcessingValidator



from model.processors.DataProcessor import DataProcessor
from model.processors.FlattenProcessor import FlattenProcessor
from model.processors.NormalizeProcessor import NormalizeProcessor
from model.processors.DiscreteProcessor import DiscreteProcessor
from model.processors.SplitProcessor import SplitProcessor

import nbformat


FLATTEN_PROCESSOR = 0
NORMALIZE_PROCESSOR = 1
DISCRETE_PROCESSOR = 2

class DataProcessorBuilder:
    def __init__(self, root):
        self.root = root
        self.data_processor = None
        self.validator = DataProcessingValidator()


    def flatten(self):
        self.validator.entry_is_exist(self.root.data_selector)
        if self.data_processor is None:
            self.data_processor = DataProcessor([])
        self.data_processor.add_processor(FlattenProcessor())
        return self
    
    def normalize(self):
        if self.data_processor is None:
            self.data_processor = DataProcessor([])
        self.data_processor.add_processor(NormalizeProcessor())
        return self
    
    def discretize(self):
        if self.data_processor is None:
            self.data_processor = DataProcessor([])
        self.data_processor.add_processor(DiscreteProcessor())
        return self

    def split(self, test_size, random_state=42):
        if self.data_processor is None:
            self.data_processor = DataProcessor([])
        self.data_processor.add_processor(SplitProcessor(test_size, random_state))
        return self

    def end_processor(self):
        return self.root

    def get_notebook_code(self):
        cell = nbformat.v4.new_markdown_cell("## Pre Processing")
        self.root.notebook.cells.append(cell)
        code = ""
        if self.data_processor is None:
            return code
        code += "# processing the data\n"
        # apply all processors
        for i in range(len(self.data_processor.processors)):
            if isinstance(self.data_processor.processors[i], FlattenProcessor):
                code += "# flattening the data\n"
                code += "data = data.values.flatten()\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif isinstance(self.data_processor.processors[i], NormalizeProcessor):
                code += "# normalizing the data\n"
                code += "data = (data - data.min()) / (data.max() - data.min())\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif isinstance(self.data_processor.processors[i], DiscreteProcessor):
                code += "# discretizing the data\n"
                code += "data = pd.cut(data, bins=10, labels=False)\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
            elif isinstance(self.data_processor.processors[i], SplitProcessor):
                code += "# splitting the data\n"
                code += "X, y = data.drop(['label'], axis = 1), data['label']\n"
                code += "X_train, X_test, y_train, ytest = train_test_split(X, y, test_size=" + str(self.data_processor.processors[i].test_size) + ", random_state=" + str(self.data_processor.processors[i].random_state) + ")\n"
                cell = nbformat.v4.new_code_cell(code)
                self.root.notebook.cells.append(cell)
                code = ""
        

            
        return code

    def get_data_processor(self):
        return self.data_processor

    def get_root(self):
        return self.root

