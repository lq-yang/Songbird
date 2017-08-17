# coding=utf-8

import pandas as pd

from app.Role import *

if __name__ == '__main__':

    db.drop_all()
    db.create_all()

    location_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/所在地信息.csv",
                                        header=0, encoding="utf-8")
    for index in location_data.index:
        record = location_data.ix[index]
        print "name: %s, target: %s" %(record['name'], record['target'])
        db.session.add(LocationInfo(name = record['name'], target =  record['target']))

    purity_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/透明度信息.csv",
                                        header=0, encoding="utf-8")
    for index in purity_data.index:
        record = purity_data.ix[index]
        print "name: %s, target: %s" % (record['name'], record['target'])
        db.session.add(PurityInfo(name=record['name'], target=record['target']))

    management_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/主管单位信息.csv",
                                        header=0, encoding="utf-8")
    for index in management_data.index:
        record = management_data.ix[index]
        print "name: %s, target: %s" % (record['name'], record['target'])
        db.session.add(ManagementInfo(name=record['name'], target=record['target']))

    db.session.commit()

    #  input your new db

    # build db for lingyu label
    lingyu_index_data = pd.read_csv(u"/home/chen/Documents/WorkSpace/Songbird/src/data/项目领域和序号对应.csv", header=0,
                                    encoding="utf-8")
    for index in lingyu_index_data.index:
        record = lingyu_index_data.ix[index]
        print "name: %s, index: %s" %(record['name'], record['index'])
        db.session.add(Yewu(name=record['name'],
                            index=record['index']))

    db.session.commit()
    print "finish adding to database"



