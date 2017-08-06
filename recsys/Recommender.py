import pandas as pd
import numpy as np
from sklearn.svm import SVC

class ModelBasedRecommender(object):
    """
    Model-based recommender which uses classification model
    """
    def __init__(self, name, data, model):
        self.name = name
        self.data = data[self.name]
        self.model = model[self.name]
        cols = self.data.columns
        self.label = cols[-1]

    def print_result(self, result):
        for n in result:
            print n

class JuanZengBasedLingYu(ModelBasedRecommender):
    """
    Recommender juan zeng fang based on ling yu xinxi
    """
    def __init__(self, name, data, model):
        super(JuanZengBasedLingYu, self).__init__(name, data, model)

    def extract(self, Xraw):
        return ""

    def predict(self, X):
        pred = self.model.predict(X)
        return pred[0]

    def recommend(self, X):
        pred = self.predict(X)
        res = self.data[self.data[self.label] == pred].index.tolist()
        self.print_result(res)
        return res

    def get_score(self):
        return 0


class JuanZengBasedZijin(ModelBasedRecommender):
    """
    Recommender juan zeng based on zi jin
    """
    def __init__(self, name, data, model):
        super(ModelBasedRecommender, self).__init__(name, data, model)




