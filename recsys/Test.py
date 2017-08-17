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
caiwu_rec = model.recommend('caiwu', caiwu_res)

# lingyu model
lingyu  = ['22', '23']
lingyu_res = model.recommend('lingyu', lingyu)

# find the common foundation
common_name = set.intersection(*tuple(set(d.keys()) for d in [caiwu_rec, lingyu_res]))
#
# # filter
# lingyu_filter = Filter.get_sort(lingyu_res, number=len(lingyu_res))
# for k1, k2 in zip(lingyu_filter, lingyu_res.iteritems()):
#     print "before sort: " + k2[0] + " score: " + str(k2[1])
#     print "after sort: " + k1[0] + " score: " + str(k1[1])
#

caiwu_filter = Filter.get_sort(caiwu_rec, number=len(caiwu_rec))
for k1, k2 in zip(caiwu_filter, caiwu_rec.iteritems()):
    print "before sort: " + k2[0] + " score: " + str(k2[1])
    print "after sort: " + k1[0] + " score: " + str(k1[1])





