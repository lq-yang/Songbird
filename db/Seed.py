# coding=utf-8

import pandas as pd

from app.Role import *

if __name__ == '__main__':

    # db.drop_all()
    db.create_all()

    #  input your new db
    #


    # # build db for lingyu label
    # lingyu_index_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/项目领域和序号对应.csv", header=0,
    #                                 encoding="utf-8")
    # for index in lingyu_index_data.index:
    #     record = lingyu_index_data.ix[index]
    #     print "name: %s, index: %s" %(record['name'], record['index'])
    #     db.session.add(Yewu(name=record['name'],
    #                         index=record['index']))
    #
    # # build db for yewu index
    # lingyu_distance_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/基金和序号对应(业务数据距离矩阵).csv",
    #                                    header=0, encoding="utf-8")
    # for index in lingyu_distance_data.index:
    #     record = lingyu_distance_data.ix[index]
    #     print "name: %s, index: %s" % (record['name'], record['label'])
    #     db.session.add(YewuJijinIndex(name=record['name'],
    #                                   index=record['label']))
    #
    # # build db for caiwu index
    # caiwu_distance_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/基金和序号对应(财务数据距离矩阵).csv",
    #                                   header=0, encoding="utf-8")
    # for index in caiwu_distance_data.index:
    #     record = caiwu_distance_data.ix[index]
    #     print "name: %s, index: %s" % (record['name'], record['label'])
    #     db.session.add(CaiwuJijinIndex(name=record['name'],
    #                                    index=record['label']))
    #
    # db.session.commit()
    # print "finish adding to database"

