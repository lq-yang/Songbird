# -*- coding: UTF-8 -*-
"""

Created by chen on 8/10/17.

"""

import numpy as np
from Role import *

LINGYU_LEN = len(Yewu.query.all())
CAIWU_LEN = 4


# get lingyu index
def get_lingyu_index(name):
    r = Yewu.query.filter_by(index=name).first()
    return r.name


# get lingyu array
def get_lingyu_array(l):
    x = np.zeros(LINGYU_LEN)
    for name in l:
        id = int(name)
        x[id] = 1
    return x


# get dict to represent lingyu
def get_lingyu_data():
    records = Yewu.query.all()
    res = []
    for record in records:
        res.append((str(record.index), record.name))
    return res


# get dict to represent caiwu
def get_caiwu_data():
    res = {'jingzichan': [('0', u"小型"), ('1', u"中型"), ('2', u"大型")],
           'shouru': [('0', u"低"), ('1', u"中"), ('2', u"高")],
           'zhichu': [('0', u"低"), ('1', u"中"), ('2', u"高")],
           'feiyong': [('0', u"低"), ('1', u"中"), ('2', u"高")]}
    return res


# get array to represent caiwu
def get_caiwu_array(l):
    res = np.zeros(CAIWU_LEN)
    res[0] = l['jingzichan']
    res[1] = l['shouru']
    res[2] = l['zhichu']
    res[3] = l['feiyong']
    return res


# get filter array
def get_filter_array(records):
    res = []
    for record in records:
        t = (record.target, record.target)
        if t not in res:
            res.append(t)
    return res


# get purity array
def get_purity_data():
    res = [('0', u"低"), ('1', u"一般"), ('2', u"高")]
    return res


# get management array
def get_management_data():
    res = get_filter_array(ManagementInfo.query.all())
    return res


# get location array
def get_location_data():
    res = get_filter_array(LocationInfo.query.all())
    return res
