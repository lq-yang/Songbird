import pandas as pd
import numpy as np
import pickle

class ModelBasedRecommender(object):
    """
    Model-based recommender which uses classification model
    """
    def __init__(self, data, name, ref):
        self.data = data
        self.name = name
        self.ref = ref
        self.model = None
        self.result = []

    def get_result(self):
        print "recommender: " + self.name
        return self.result

    def load_model(self, model):
        self.model = model


class JuanZengBasedLingYu(ModelBasedRecommender):
    """
    Recommender juan zeng fang based on ling yu xinxi
    """
    def __init__(self, data, name, model, ref):
        super(JuanZengBasedLingYu, self).__init__(data, name)
        print "begin to use " + name
        self.load_model(model)

    def extract(self, Xraw):
        return ""

    def recommend(self, X):
        from sklearn.svm import SVC
        res = self.model.predict(X)
        self.result.add(res[0])






