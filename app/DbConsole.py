# -*- coding: UTF-8 -*-
"""

Created by chen on 8/10/17.

"""

import numpy as np
from Role import Yewu, YewuJijinIndex, CaiwuJijinIndex

LINGYU_LEN = len(Yewu.query.all())
CAIWU_LEN = 4


# get lingyu index
def get_lingyu_index(name):
    r = Yewu.query.filter_by(name=name).first()
    return r.index


# get lingyu array
def get_lingyu_array(l):
    x = np.zeros(LINGYU_LEN)
    for name in l:
        id = get_lingyu_index(name)
        x[id] = 1
    return x


# get dict to represent lingyu
def get_lingyu_data():
    records = Yewu.query.all()
    res = []
    for record in records:
        res.append((record.index, record.name))
    return res


# get dict to represent caiwu
def get_caiwu_data():
    res = {'jingzichan': [(str(0), u"小型"), (str(1), u"中型"), (str(2), u"大型")], 'shouru': [(str(0), u"低"), (str(1), u"中"), (str(2), u"高")],
           'zhichu': [(str(0), u"低"), (str(1), u"中"), (str(2), u"高")], 'feiyong': [(str(0), u"低"), (str(1), u"中"), (str(2), u"高")]}
    return res

# get array to represent caiwu
def get_caiwu_array(l):
    res = np.zeros(CAIWU_LEN)
    res[0] = l['jingzichan']
    res[1] = l['shouru']
    res[2] = l['zhichu']
    res[3] = l['feiyong']
    return res



