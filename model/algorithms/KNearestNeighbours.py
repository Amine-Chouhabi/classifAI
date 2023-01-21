from model.algorithms.Algorithm import Algorithm

class KNearestNeighbours(Algorithm):
    def __init__(self, name):
        super().__init__(name)
        self.hyperparameters = []


    def __str__(self):
        return "KNearestNeighbours: " + self.name + " " + str(self.hyperparameters)

    def __repr__(self):
        return self.__str__()

    def set_hyperparameter(self, hyperparameter):
        self.hyperparameters.append(hyperparameter)

    def set_hyperparameters(self, hyperparameters):
        self.hyperparameters = hyperparameters

    def clone(self):
        return KNearestNeighbours(self.name)


    def get_hyperparameters_names(self):
        return [
            "n_neighbors",
            "weights",
            "algorithm",
            "leaf_size",
            "p",
            "metric",
            "metric_params",
            "n_jobs"
        ]