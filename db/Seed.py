# coding=utf-8

import pandas as pd

from app.Role import *

if __name__ == '__main__':

    db.drop_all()
    db.create_all()

    # location_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/所在地信息.csv",
    #                                     header=0, encoding="utf-8")
    # for index in location_data.index:
    #     record = location_data.ix[index]
    #     print "name: %s, target: %s" %(record['name'], record['target'])
    #     db.session.add(LocationInfo(name = record['name'], target =  record['target']))
    #
    # purity_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/透明度信息.csv",
    #                                     header=0, encoding="utf-8")
    # for index in purity_data.index:
    #     record = purity_data.ix[index]
    #     print "name: %s, target: %s" % (record['name'], record['target'])
    #     db.session.add(PurityInfo(name=record['name'], target=record['target']))
    #
    # management_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/主管单位信息.csv",
    #                                     header=0, encoding="utf-8")
    # for index in management_data.index:
    #     record = management_data.ix[index]
    #     print "name: %s, target: %s" % (record['name'], record['target'])
    #     db.session.add(ManagementInfo(name=record['name'], target=record['target']))
    #
    # db.session.commit()
    #
    # #  input your new db
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
    # db.session.commit()
    # print "finish adding to database"
    #
    # # build db for foundation popularity
    # popularity_file = open('/Users/lanqingy/Desktop/Songbird/data/foundation_popularity.txt', 'r')
    # lines = popularity_file.readlines()
    # for line in lines:
    #     lst = line.split('\t')
    #     db.session.add(FoundationPopularity(foundation=unicode(lst[0], 'utf-8'),
    #                                         popularity=int(lst[1])))
    # popularity_file.close()
    #
    # # build db for foundation similarity
    # similarity_file = open('/Users/lanqingy/Desktop/Songbird/data/foundation_similarity.txt', 'r')
    # lines = similarity_file.readlines()
    # for line in lines:
    #     lst = line.split('\t')
    #     db.session.add(FoundationSimilarity(foundationA=unicode(lst[0], 'utf-8'),
    #                                         foundationB=unicode(lst[1], 'utf-8'),
    #                                         similarity=int(lst[2])))
    # similarity_file.close()
    #
    # # build db for foundation recommendation
    # itemcf_file = open('/Users/lanqingy/Desktop/Songbird/data/itemcf.txt', 'r')
    # lines = itemcf_file.readlines()
    # for line in lines:
    #     lst = line.split('\t')
    #     db.session.add(FoundationRec(investor=unicode(lst[0], 'utf-8'),
    #                                  foundation=unicode(lst[1], 'utf-8'),
    #                                  rating=float(lst[2])))
    # itemcf_file.close()

    # build db for project info
    project_info = pd.read_csv('/Users/lanqingy/Desktop/Songbird/data/project.csv', header=0, encoding="utf-8")
    for index in project_info.index:
        line = project_info.ix[index]
        db.session.add(ProjectInfo(foundation=line['foundation'],
                                   project=line['project'],
                                   field=line['field'],
                                   location=line['location']))

    db.session.commit()
    print "finish adding to database"

