
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
        self.algorithms = AlgorithmsBuilder(self)
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
            .split(0.2, ) \
            .end_processor() \
        .set_hyper_parameters() \
            .add_hyperparameter("learning_rate",0.1) \
            .add_hyperparameter("max_depth", 3) \
            .add_hyperparameter("n_estimators", 100) \
            .add_hyperparameter("epochs", 100) \
            .add_hyperparameter("batch_size", 32) \
            .add_range_hyperparameter("learning_rate", 0.1, 0.2, 0.02) \
            .end_hyperparameters() \
        .set_algorithms() \
            .add_svm("svm1",[]) \
            .add_logistic_regression("logistic1",["C", "penalty"]) \
            .add_random_forest("random_forest1",["n_estimators", "max_depth"]) \
            .add_k_nearest_neighbours("knn1",["n_neighbors", "weights"]) \
            .train() \
            .predict() \
            .end_algorithms() \
        .set_vizualisation() \
            .add_pie_chart() \
            .visualize_accuracy().as_pie_chart() \
            .visualize_precision() \
            .visualize_recall() \
            .visualize_f1_score() \
            .visualize_training_duration()  \
            .end_vizualisation() \
        .get_notebook_code()
        
        
    
    



