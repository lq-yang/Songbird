# coding=utf-8
from Web import db


# 业务领域和序号对应
class Yewu(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    index = db.Column(db.Integer, unique=True)


# 业务领域距离矩阵需要的序号对应
class YewuJijinIndex(db.Model):
    name = db.Column(db.String(400), primary_key=True)
    index = db.Column(db.Integer, unique=True)


# 财务数据距离矩阵需要的序号对应
class CaiwuJijinIndex(db.Model):
    name = db.Column(db.String(400), primary_key=True)
    index = db.Column(db.Integer, unique=True)


# 项目基金会热门度
class FoundationPopularity(db.Model):
    foundation = db.Column(db.String(400), primary_key=True)
    popularity = db.Column(db.Integer)


# 项目基金会相似度
class FoundationSimilarity(db.Model):
    foundationA = db.Column(db.String(400), primary_key=True)
    foundationB = db.Column(db.String(400), primary_key=True)
    similarity = db.Column(db.Integer)


# 基于itemCF的推荐
class FoundationRec(db.Model):
    investor = db.Column(db.String(400), primary_key=True)
    foundation = db.Column(db.String(400), primary_key=True)
    rating = db.Column(db.Float)
