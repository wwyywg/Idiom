# _*_ coding: UTF-8 _*_
# 开发团队   :  未来科技
# 开发人员   :  ww
# 开发时间   :  2019-10-23 12:11
# 文件名称   :  models.py
# 开发工具   :  PyCharm
# 功能描述   :  models
from . import db
from datetime import datetime

# 会员数据模型
class Member(db.Model):
    __tablename__ = "member"
    id = db.Column(db.Integer, primary_key=True)    # 编号
    openid = db.Column(db.String(80))        # 微信用户id
    nickname = db.Column(db.String(100))            # 用户名
    avatar = db.Column(db.String(255))              # 头像
    sesion = db.Column(db.Integer)                  # 通过关卡
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间

    def __repr__(self):
        return '<User %r>' % self.nickname

# 考题数据模型
class Exam(db.Model):
    __tablename__ = "exam"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    pictureUrl = db.Column(db.String(255)) # 图片url
    answer = db.Column(db.String(20)) # 答案
    candidates = db.Column(db.String(100)) # 备选项
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    def __repr__(self):
        return '<Exam %r>' % self.answer
