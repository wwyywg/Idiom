# _*_ coding: UTF-8 _*_
# 开发团队   :  未来科技
# 开发人员   :  ww
# 开发时间   :  2019-10-23 13:34
# 文件名称   :  manage.py
# 开发工具   :  PyCharm
# 功能描述   :  manage
from app import create_app

app = create_app('default')
app.run(host="0.0.0.0",port=8888,debug=True)