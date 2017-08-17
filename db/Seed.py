# coding=utf-8

import pandas as pd

from app.Role import *

if __name__ == '__main__':

    db.drop_all()
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

    # build db for foundation popularity
    popularity_file = open('/Users/lanqingy/Desktop/Songbird/data/foundation_popularity.txt', 'r')
    lines = popularity_file.readlines()
    for line in lines:
        lst = line.split('\t')
        db.session.add(FoundationPopularity(foundation=unicode(lst[0], 'utf-8'),
                                            popularity=int(lst[1])))
    popularity_file.close()

    # build db for foundation similarity
    similarity_file = open('/Users/lanqingy/Desktop/Songbird/data/foundation_similarity.txt', 'r')
    lines = similarity_file.readlines()
    for line in lines:
        lst = line.split('\t')
        db.session.add(FoundationSimilarity(foundationA=unicode(lst[0], 'utf-8'),
                                            foundationB=unicode(lst[1], 'utf-8'),
                                            similarity=int(lst[2])))
    similarity_file.close()

    # build db for foundation recommendation
    itemcf_file = open('/Users/lanqingy/Desktop/Songbird/data/itemcf.txt', 'r')
    lines = itemcf_file.readlines()
    for line in lines:
        lst = line.split('\t')
        db.session.add(FoundationRec(investor=unicode(lst[0], 'utf-8'),
                                     foundation=unicode(lst[1], 'utf-8'),
                                     rating=float(lst[2])))
    itemcf_file.close()

    db.session.commit()
    print "finish adding to database"

