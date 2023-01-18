from algorithms.Algorithm import Algorithm

class RandomForest(Algorithm):
    def __init__(self, name):
        super().__init__(name)
        self.hyperparameters = []

    def __str__(self):
        return "RandomForest: " + self.name + " " + str(self.hyperparameters)

    def __repr__(self):
        return self.__str__()

    def set_hyperparameter(self, hyperparameter):
        self.hyperparameters.append(hyperparameter)

    def set_hyperparameters(self, hyperparameters):
        self.hyperparameters = hyperparameters



    def get_hyperparameters_names(self):
        return [
            "n_estimators",
            "criterion",
            "max_depth",
            "min_samples_split",
            "min_samples_leaf",
            "min_weight_fraction_leaf",
            "max_features",
            "max_leaf_nodes",
            "min_impurity_decrease",
            "min_impurity_split",
            "bootstrap",
            "oob_score",
            "n_jobs",
            "random_state",
            "verbose",
            "warm_start",
            "class_weight",
            "ccp_alpha",
            "max_samples",
        ]