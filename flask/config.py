# _*_ coding: UTF-8 _*_
# 开发团队   :  未来科技
# 开发人员   :  ww
# 开发时间   :  2019-10-23 11:58
# 文件名称   :  config.py
# 开发工具   :  PyCharm
# 功能描述   :  config
class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 小程序配置信息
    AppID = 'wx71b05d2d6379bc20'                    # 小程序的AppID
    AppSecret = '596df588a558c5e9a2552c2505dde6b5'  # 小程序的AppSecret

    @staticmethod
    def init_app(app):
        '''初始化配置文件'''
        pass

# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wa123456@127.0.0.1:3306/idiom'
    DEBUG = True

# define the config
config = {
    'default': DevelopmentConfig
}