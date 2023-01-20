
from AlgoComparisonBuilder import AlgoComparisonBuilder

def main():
    algo_comparison_builder = AlgoComparisonBuilder("test")
    algo_comparison_builder \
    .add_markdown("# This is a markdown cell") \
    .add_markdown("## This is a markdown cell") \
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
            .C().set_range().max_(2).min_(0.1).step_(0.4) \
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
                .end() \
            .logistic_regression("lr1") \
            .end() \
            .train() \
            .predict() \
        .end_algorithms() \
        .set_vizualisation() \
            .visualize_accuracy().as_bar_chart() \
            .visualize_loss().as_bar_chart() \
            .visualize_precision().as_graph() \
            .visualize_training_duration().as_pie_chart() \
        .end_vizualisation() \
        .get_notebook_code()
        
    
    

if __name__ == '__main__':
    main()