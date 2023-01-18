
from DataSelectorBuilder import DataSelectorBuilder
from DataProcessorBuilder import DataProcessorBuilder
from HyperParametersBuilder import HyperParametersBuilder
from AlgorithmsBuilder import AlgorithmsBuilder
from VizualisationBuilder import VizualisationBuilder


class AlgoComparisonBuiilder:
    def __init__(self, name):
        self.name = name
        self.data_selector = None
        self.data_processor = None
        self.hyper_parameters = None
        self.algorithms = None
        self.vizualisations = None
    
    def select_data(self):
        self.data_selector = DataSelectorBuilder(self)
        return self.data_selector

    def process_data(self):
        self.data_processor = DataProcessorBuilder(self)
        return self.data_processor
    
    def set_hyper_parameters(self):
        self.hyper_parameters = HyperParametersBuilder(self)
        return self.hyper_parameters
    
    def set_algorithms(self):
        self.algorithms = AlgorithmsBuilder(self,self.hyper_parameters)
        return self.algorithms
    
    def set_vizualisation(self):
        self.vizualisations = VizualisationBuilder(self, self.algorithms)
        return self.vizualisations


    def get_notebook_code(self):
        code = ""
        if self.data_selector is not None:
            code += self.data_selector.get_notebook_code()
        if self.data_processor is not None:
            code += self.data_processor.get_notebook_code()
        if self.hyper_parameters is not None:
            code += self.hyper_parameters.get_notebook_code()
        if self.algorithms is not None:
            code += self.algorithms.get_notebook_code()
        if self.vizualisations is not None:
            code += self.vizualisations.get_notebook_code()
        print(code)



# test 
algo_comparison_builder = AlgoComparisonBuiilder("test")
algo_comparison_builder \
    .select_data() \
        .add_entry("diabetes.csv") \
        .add_entry("diabetes.csv") \
        .add_entry("diabetes.csv") \
        .add_entry("diabetes.csv") \
            .remove_null_values() \
            .remove_outliers() \
            .remove_duplicates() \
            .end_selector() \
        .process_data() \
            .normalize() \
            .split(0.2, 33) \
            .end_processor() \
        .set_hyper_parameters() \
            .learning_rate().set_value(0.1) \
            .C().set_value(0.1) \
            .kernel().set_value("linear") \
            .gamma().set_value(0.2) \
        .end_hyperparameters() \
        .set_algorithms() \
            .svm("svm1") \
                .hyperparameter("C") \
                .hyperparameter("kernel") \
                .hyperparameter("gamma") \
                .end()      \
            .svm("svm2") \
            .end() \
        .end_algorithms() \
        .get_notebook_code()
        
    
    



