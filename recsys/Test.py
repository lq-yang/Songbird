# -*- coding: UTF-8 -*-

import random
from Util import *
from Recommender import *

# prepare data, mode, reference
data, model = prepare_all()

# prepare model
model = ModelFactory(data, model)

# caiwu model
caiwu_res = {}
caiwu_res["jingzichan"] = 1
caiwu_res["shouru"] = 0
caiwu_res["zhichu"] = 1
caiwu_res["feiyong"] = 0
pre = model.predict('caiwu', caiwu_res)
caiwu_data = model.return_model('caiwu').get_data()
rec = caiwu_data[caiwu_data.label == pre].drop()
true = model.return_model('caiwu').extract(caiwu_res)
# model.recommend('caiwu', caiwu_res)

from scipy.spatial.distance import cdist
dist = cdist()





