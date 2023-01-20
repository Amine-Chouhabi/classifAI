
from AlgoComparisonBuilder import AlgoComparisonBuilder

def main2():
    algo_comparison_builder = AlgoComparisonBuilder("test")
    algo_comparison_builder \
        .select_data() \
            .add_entry("diabetes.csv") \
            .remove_columns(["Pregnancies"]) \
            .remove_rows([1, 2, 3]) \
            .rename_column("Glucose", "Glucose2") \
            .rename_column("Outcome", "label") \
            .remove_null_values() \
            .remove_outliers() \
            .remove_duplicates() \
            .end_selector() \
        .process_data() \
            .normalize() \
            .split(0.2, 45) \
            .end_processor() \
        .set_hyper_parameters() \
            .C().set_range() \
                .max_(2) \
                .min_(0.1) \
                .step_(0.4) \
            .kernel().set_value("linear") \
            .gamma().set_value(0.2) \
            .end_hyperparameters() \
        .set_algorithms() \
            .svm("svm1") \
                .kernel() \
                .C() \
                .gamma() \
                .end()      \
            .train() \
            .predict() \
            .end_algorithms() \
        .set_vizualisation() \
            .visualize_accuracy().as_graph().from_(0) \
            .visualize_loss().as_pie_chart().from_(100) \
            .visualize_precision().as_bar_chart().from_(0) \
            .visualize_recall().as_bar_chart().from_(0) \
            .visualize_f1_score().as_graph().from_(0) \
            .visualize_training_duration().as_graph().from_(0) \
            .rank_algorithms() \
        .end_vizualisation() \
        .get_notebook_code()
        


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
    main2()