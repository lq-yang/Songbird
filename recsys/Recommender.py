import pandas as pd
import numpy as np
from sklearn.svm import SVC

class ModelBasedRecommender(object):

    """
    Model-based recommender which uses classification model
    """
    def __init__(self, name, data, model):
        self.name = name
        self.data = data
        self.model = model
        cols = self.data.columns
        self.label = cols[-1]

    def extract(self, Xraw):
        pass

    def predict(self, Xraw):
        X = self.extract(Xraw)
        pred = self.model.predict(X)
        return pred[0]

    def recommend(self, Xraw):
        pred = self.predict(Xraw)
        rec = self.data[self.data[self.label] == pred]
        res = rec.index.tolist()
        score = self.get_score(rec)
        # self.print_result(res)
        return res

    def get_score(self, obj, rec):
        pass

    def get_data(self):
        return self.data

    @staticmethod
    def print_result(result):
        for n in result:
            print n

    def __repr__(self):
        print self.name


class ModelFactory(object):
    """
    Model factory to use
    """
    def __init__(self, data, model):
        self.model = {"lingyu": JuanZengBasedLingYu("lingyu", data["lingyu"], model["lingyu"]),
                      "caiwu": JuanZengBasedCaiwu("caiwu", data["caiwu"], model["caiwu"])}

    def return_model(self, name):
        return self.model[name]

    def predict(self, name, X):
        model = self.return_model(name)
        return model.predict(X)

    def recommend(self, name, X):
        model = self.return_model(name)
        return model.recommend(X)


class JuanZengBasedLingYu(ModelBasedRecommender):
    """
    Recommender juan zeng fang based on ling yu xinxi
    """

    def __init__(self, name, data, model):
        super(JuanZengBasedLingYu, self).__init__(name, data, model)

    def extract(self, Xraw):
        from DbConsole import get_lingyu_array
        return get_lingyu_array(Xraw)

    def get_score(self, obj, rec):
        from scipy.spatial.distance import cdist

class JuanZengBasedCaiwu(ModelBasedRecommender):
    """
    Recommender juan zeng based on zi jin
    """

    def __init__(self, name, data, model):
        super(JuanZengBasedCaiwu, self).__init__(name, data, model)

    def extract(self, Xraw):
        from DbConsole import get_caiwu_array
        return get_caiwu_array(Xraw)

    def get_score(self, obj, rec):
        from scipy.spatial.distance import cdist
        from DbConsole import CAIWU_LEN
        obj

