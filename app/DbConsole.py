# -*- coding: UTF-8 -*-
"""

Created by chen on 8/10/17.

"""

import numpy as np
from sqlalchemy import desc
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
    res = [('0', u"低"), ('1', u"中"), ('2', u"高")]
    return res


# test purity
def test_purity(name, x):
    obj = PurityInfo.query.filter_by(name=name).first()
    if obj is None or obj.target != int(x):
        return False
    return True


# get management array
def get_management_data():
    res = get_filter_array(ManagementInfo.query.all())
    return res


# test management
def test_management(name, x):
    if len(x) == 0:
        return True
    obj = ManagementInfo.query.filter_by(name=name).first()
    if obj is None or obj.target not in x:
        return False
    return True


# get location array
def get_location_data():
    res = get_filter_array(LocationInfo.query.all())
    return res


# test location
def test_location(name, x):
    if len(x) == 0:
        return True
    obj = LocationInfo.query.filter_by(name=name).first()
    if obj is None or obj.target not in x:
        return False
    return True


# get meet_name array
def get_meet_data():
    res = []
    for record in FoundationRec.query.all():
        temp = (record.investor, record.investor)
        if temp not in res:
            res.append(temp)
    return res


# get interest_name array
def get_interest_data():
    res = []
    for record in FoundationSimilarity.query.all():
        temp = (record.foundationA, record.foundationA)
        if temp not in res:
            res.append(temp)
    return res


# get rec
def get_rec_data(X):
    target = FoundationRec.query.filter_by(investor=X)
    res = {}
    for t in target:
        res[t.foundation] = t.rating
    return res


# get similarity
def get_similarity_data(X):
    res = {}
    for item in X:
        target = FoundationSimilarity.query.filter_by(foundationA=item)
        for t in target:
            res[t.foundationB] = t.similarity
    return res


# get basic info
def get_basic_data():
    res = []
    records = BasicInfo.query.all()
    for record in records:
        res.append((record.name, record.name))
    return res


# get project info array
def get_project_array(X):
    name = [u"项目", u"业务领域", u"地址"]
    data = []
    target = ProjectInfo.query.filter_by(foundation=X)
    for t in target:
        data.append({name[0]: t.project, name[1]: t.field, name[2]: t.location})
    return data


# get basic info array
def get_basic_array(X):
    name = [u"基金会名称", u"宗旨", u"业务范围", u"成立时间",
            u"业务主管单位", u"原始基金", u"所在地",
            u"办公地址", u"理事长姓名", u"对外联系人邮箱", u"网站地址",
            u"基金会行业领域", u"评估等级"]
    target = BasicInfo.query.filter_by(name=X).first()
    data = {name[0]: target.name,
            name[1]: target.slogan,
            name[2]: target.quote,
            name[3]: target.time,
            name[4]: target.management,
            name[5]: target.money,
            name[6]: target.location,
            name[7]: target.office,
            name[8]: target.boss,
            name[9]: target.email,
            name[10]: target.website,
            name[11]: target.yewu,
            name[12]: target.level}
    return data

# get popularity data
def get_popular_data():
    target = FoundationPopularity.query.order_by(desc(FoundationPopularity.popularity)).limit(10).all()
    res = []
    for t in target:
        res.append(t.foundation)
    return res
