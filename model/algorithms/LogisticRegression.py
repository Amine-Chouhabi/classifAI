from model.algorithms.Algorithm import Algorithm

class LogisticRegression(Algorithm):
    def __init__(self, name):
        super().__init__(name)
        self.hyperparameters = []


    def __str__(self):
        return "LogisticRegression: " + self.name + " " + str(self.hyperparameters)

    def __repr__(self):
        return self.__str__()

    def set_hyperparameter(self, hyperparameter):
        self.hyperparameters.append(hyperparameter)
    

    def set_hyperparameters(self, hyperparameters):
        self.hyperparameters = hyperparameters

    def clone(self):
        return LogisticRegression(self.name)


    def get_hyperparameters_names(self):
        return [
            "penalty",
            "dual",
            "tol",
            "C",
            "fit_intercept",
            "intercept_scaling",
            "class_weight",
            "random_state",
            "solver",
            "max_iter",
            "multi_class",
            "verbose",
            "warm_start",
            "n_jobs",
            "l1_ratio"
        ]