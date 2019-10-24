# _*_ coding: UTF-8 _*_
# 开发团队   :  未来科技
# 开发人员   :  ww
# 开发时间   :  2019-10-23 12:14
# 文件名称   :  MemberService.py
# 开发工具   :  PyCharm
# 功能描述   :  MemberService
import requests, json
from config import Config

class MemberService():

    @staticmethod
    def getWeChatOpenId(code):
        url = ("https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&"
               "js_code={2}&grant_type=authorization_code".format(Config.AppID, Config.AppSecret, code))
        r = requests.get(url)
        res = json.loads(r.text)
        openid = None
        if 'openid' in res:
            openid = res['openid']
        return openid