# coding=utf-8
from Web import db


# 业务领域和序号对应
class Yewu(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    index = db.Column(db.Integer, unique=True)


# 地理位置信息
class LocationInfo(db.Model):
    name = db.Column(db.String(400), primary_key=True)
    target = db.Column(db.String(400))


# 透明度信息
class PurityInfo(db.Model):
    name = db.Column(db.String(400), primary_key=True)
    target = db.Column(db.Integer)


# 业务主管单位
class ManagementInfo(db.Model):
    name = db.Column(db.String(400), primary_key=True)
    target = db.Column(db.String(400))


# 项目信息
class ProjectInfo(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    foundation = db.Column(db.String(400))
    project = db.Column(db.String(400))
    field = db.Column(db.String(400))
    location = db.Column(db.String(400))


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


# 基本信息
class BasicInfo(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), primary_key=True)
    slogan = db.Column(db.Text)
    quote = db.Column(db.Text)
    time = db.Column(db.Text)
    management = db.Column(db.String(200))
    money = db.Column(db.String(100))
    location = db.Column(db.String(200))
    office = db.Column(db.String(200))
    boss = db.Column(db.String(100))
    email = db.Column(db.String(200))
    website = db.Column(db.String(200))
    yewu = db.Column(db.String(200))
    level = db.Column(db.String(20))
