# _*_ coding: UTF-8 _*_
# 开发团队   :  未来科技
# 开发人员   :  ww
# 开发时间   :  2019-10-23 11:32
# 文件名称   :  __init__.py.py
# 开发工具   :  PyCharm
# 功能描述   :  __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()   # 实例化SQLAlchemy
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name]) # 获取配置信息中的开发环境
    config[config_name].init_app(app)           # 初始化app
    db.init_app(app)

    # 注册蓝图
    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app