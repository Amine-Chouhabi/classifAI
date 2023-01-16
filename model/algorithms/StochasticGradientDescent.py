from algorithms.Algorithm import Algorithm

class StochasticGradientDescent(Algorithm):
    def __init__(self, name):
        super().__init__(name)
        self.hyperparameters = None


    def __str__(self):
        return "StochasticGradientDescent: " + self.name + " " + str(self.hyperparameters)

    def __repr__(self):
        return self.__str__()

    def set_hyperparameter(self, name, value):
        self.hyperparameters[name] = value

    def set_hyperparameters(self, hyperparameters):
        self.hyperparameters = hyperparameters


    def get_hyperparameters_names(self):
        return [
            "loss",
            "penalty",
            "alpha",
            "l1_ratio",
            "fit_intercept",
            "max_iter",
            "tol",
            "shuffle",
            "verbose",
            "epsilon",
            "n_jobs",
            "random_state",
            "learning_rate",
            "eta0",
            "power_t",
            "early_stopping",
            "validation_fraction",
            "n_iter_no_change",
            "class_weight",
            "warm_start",
            "average"
        ]