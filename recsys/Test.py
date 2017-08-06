# -*- coding: UTF-8 -*-

import random
from Util import *
from Recommender import *

def test_model(model):
    """
    :param model:
    :return: test model with true y and predict y
    """
    data = model.data
    cols = data.columns
    index = random.randint(0, len(data))
    X = data.iloc[index][cols[:-1]]
    y_true = data.iloc[index][cols[-1]]
    y_pred = model.predict(X)
    print "true label: " + str(y_true) + "  predict label: " + str(y_pred)
    res = model.recommend(X)
    print "recommend"
    for k, v in enumerate(res):
        print "no.%d"%k + ": " + v
    return res

# prepare data, mode, reference
data, model = prepare_all()

# JuanZengBasedLingYu test
jzly = JuanZengBasedLingYu("JuanZengBasedLingYu", data, model)
jzly_res = test_model(jzly)






