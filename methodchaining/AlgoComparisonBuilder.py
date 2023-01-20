
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
            .C().set_range(0.1,2,0.5) \
            .kernel().set_value("linear") \
            .gamma().set_value(0.2) \
            .criterion().set_value(0.1) \
            .set_hyperparameter("splitter").set_value("best") \
        .end_hyperparameters() \
        .set_algorithms() \
            .svm("svm1") \
                .kernel() \
                .C() \
                .gamma() \
                .end()      \
            .svm("svm2") \
            .end() \
            .decision_tree("dt1") \
                .hyperparameter("splitter") \
                .hyperparameter("criterion") \
                .end() \
            .logistic_regression("lr1") \
            .end() \
        .end_algorithms() \
        .set_vizualisation() \
            .visualize_accuracy().as_pie_chart() \
            .visualize_loss().as_bar_chart() \
            .visualize_precision().as_graph() \
        .end_vizualisation() \
        .get_notebook_code()
        
    
    



