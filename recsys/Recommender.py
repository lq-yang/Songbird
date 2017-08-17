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
        rec = self.data[self.data[self.label] == pred].drop(self.data.columns[-1], axis=1)
        obj = self.extract(Xraw)
        obj = obj.reshape(1, obj.shape[0])
        key = rec.index.tolist()
        value = self.get_score(obj, rec)
        res = {k: v for k, v in zip(key, value[0])}
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


class MemoryBasedRecommender(object):
    """
    Memory based model focused on recommending based on history data
    """

    def __init__(self):
        pass

    def recommend(self):
        pass


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
        dist = cdist(obj, rec, metric='correlation')
        return dist


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
        dist = cdist(obj, rec, metric='hamming')
        return dist


class Filter:
    """
    Filter methods to filter out the final result
    """

    def __init__(self, data):
        self.data = data
        self.constraint = []

    def add_constrain(self, c):
        self.constraint.append(c)

    @staticmethod
    def get_sort(d, number=30):
        import operator
        res = sorted(d.items(), key=operator.itemgetter(1))
        l = min(number, len(res))
        return res[:l]

