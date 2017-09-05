import numpy as np


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
        x = self.extract(Xraw)
        pred = self.model.predict(x)
        return pred[0]

    def recommend(self, Xraw):
        pred = self.predict(Xraw)
        rec = self.data[self.data[self.label] == pred].drop(self.data.columns[-1], axis=1)
        obj = self.extract(Xraw)
        obj = obj.reshape(1, obj.shape[0])
        key = rec.index.tolist()
        value = self.get_score(obj, rec)
        res = {k: float(v) for k, v in zip(key, value[0])}
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

    def __init__(self, name):
        self.name = name

    def recommend(self, x):
        pass


class ModelFactory(object):
    """
    Model factory to use
    """

    def __init__(self, data, model):
        self.model = {"lingyu": JuanZengBasedLingYu("lingyu", data["lingyu"], model["lingyu"]),
                      "caiwu": JuanZengBasedCaiwu("caiwu", data["caiwu"], model["caiwu"]),
                      "rec": JuanZengBasedRec("rec"),
                      "similarity": JuanZengBasedSimilarity("similarity")}

    def return_model(self, name):
        return self.model[name]

    def predict(self, name, x):
        model = self.return_model(name)
        return model.predict(x)

    def recommend(self, name, x):
        model = self.return_model(name)
        return model.recommend(x)


class JuanZengBasedLingYu(ModelBasedRecommender):
    """
    Recommender juan zeng fang based on ling yu info
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


class JuanZengBasedRec(MemoryBasedRecommender):
    """
    Recommender foundation based on memory
    """

    def __init__(self, name):
        super(JuanZengBasedRec, self).__init__(name)

    def recommend(self, x):
        from DbConsole import get_rec_data
        res = get_rec_data(x)
        return res


class JuanZengBasedSimilarity(MemoryBasedRecommender):
    """
    Recommender foundation based on similarity
    """

    def __init__(self, name):
        super(JuanZengBasedSimilarity, self).__init__(name)

    def recommend(self, x):
        from DbConsole import get_similarity_data
        res = get_similarity_data(x)
        return res


class FilterFactory:
    """
    Filter methods to filter out the final result
    """

    def __init__(self, ref=None):
        self.constraint = {}
        self.ref = ref

    def add_constraint(self, name, c):
        self.constraint[name] = c

    def clear_constraint(self):
        self.constraint = []

    def get_result(self, x, order=3):
        res = self.add_result(x, order)
        self.constraint.clear()
        l = min(10, len(res))
        return res[:l]

    def test_result(self, x):
        from DbConsole import test_location, test_management, test_purity
        for k, v in self.constraint.iteritems():
            if k == 'location':
                if not test_location(x, v):
                    return False
            if k == 'management':
                if not test_management(x, v):
                    return False
            if k == 'purity':
                if not test_purity(x, v):
                    return False
        return True

    def add_result(self, x, order=3):
        from collections import Counter
        keys = []
        res = []
        for v in x.itervalues():
            keys.append(v[0])
        count = Counter(keys)
        count = sorted(count.items(), key=lambda y: -y[1])

        # add results that are common
        for member in count:
            if member[1] > 1 and self.test_result(member[0]):
                res.append(member[0])
        names = ['rec', 'similarity', 'lingyu', 'caiwu']

        # add some in rec and similarity
        if x.has_key('rec'):
            for member in x['rec']:
                if member not in res and self.test_result(member[0]):
                    res.append(member[0])
        if x.has_key('similarity'):
            i = 0
            for member in x['similarity']:
                if member not in res and self.test_result(member[0]):
                    res.append(member[0])
                    i += 1
                    if i == 2:
                        break

        # get the data
        d1 = x['lingyu']
        d2 = x['caiwu']

        # different order strategy
        if order == 3:
            i, j = 0, 0
            while len(res) < 10 and i < len(d1) and j < len(d2):
                while d1[i][0] in res or not self.test_result(d1[i][0]):
                    i += 1
                if i < len(d1):
                    res.append(d1[i][0])
                while d2[j][0] in res or not self.test_result(d2[j][0]):
                    j += 1
                if j < len(d2):
                    res.append(d2[j][0])
        else:
            if order == 2:
                d1, d2 = d2, d1
            rem = 10 - len(res)
            i, j = 0, 0
            for k in range(len(d1)):
                if d1[k][0] in res or not self.test_result(d1[k][0]):
                    continue
                else:
                    res.append(d1[k][0])
                    i += 1
                    if i == rem / 2:
                        break
            for k in range(len(d2)):
                if d2[k][0] in res or not self.test_result(d2[k][0]):
                    continue
                else:
                    res.append(d2[k][0])
                    j += 1
                    if len(res) == 10:
                        break
        return res

    def get_sort(self, d, asc=True, array=None):
        if array and len(array) > 0:
            res = self.get_sort_helper(d, array)
        else:
            if asc:
                res = sorted(d.items(), key=lambda x: x[1])
            else:
                res = sorted(d.items(), key=lambda x: -x[1])
        return res

    def get_sort_helper(self, d, array):
        from sklearn.preprocessing import scale
        from scipy.spatial.distance import cdist
        data = self.ref['caiwu_ref']
        names = []
        sec_d = []
        for item in d.items():
            names.append(item[0])
            sec_d.append(item[1])
        Y = np.array([i for i in array.values()])
        Y.shape = (1, len(Y))
        X = data.ix[names, array.keys()].values
        l = X.shape[1]
        A = np.vstack([X, Y])
        A = scale(A, axis=0, with_mean=True, with_std=True, copy=True)
        X = A[-1, :].reshape(1, l)
        Y = A[:-1, :].reshape(len(A[:-1, :]), l)
        fir_d = cdist(Y, X, metric="euclidean").tolist()
        Z = zip(names, fir_d, sec_d)
        Z = sorted(Z, key = lambda x: (x[1], x[2]))
        Z = [(k[0], k[2]) for k in Z]
        return Z


    @staticmethod
    def get_popular():
        from DbConsole import get_popular_data
        return get_popular_data()

    def get_hottag(self):
        return self.ref['hottag']


class SearchFactory:
    """
    Search methods to find the projects info and basic info of the foundation
    """

    def __init__(self):
        pass

    @staticmethod
    def get_project_info(x):
        from DbConsole import get_project_array
        return get_project_array(x)

    @staticmethod
    def get_basic_info(x):
        from DbConsole import get_basic_array
        return get_basic_array(x)
