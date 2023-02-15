# coding:utf-8
import os

import yaml


class _const:
    class ConstError(TypeError): pass

    class ConstCaseError(ConstError): pass

    def __init__(self):
        yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "conf/global.yml")
        with open(yaml_path, 'r', encoding='UTF-8') as f:
            temp = yaml.load(f.read(), yaml.FullLoader)
            self.SCHDULE_TIME = temp['wx']['schdule']['time']
            self.APPID = temp['wx']['appId']
            self.APPSECREATE = temp['wx']['appSecreate']
            self.ACCESSTOKENURL = temp['wx']['accessTokenUrl']
            self.TOKEN = temp['wx']['token']
            self.WX_MAX_RESPONSE_TOKEN = temp['wx']['maxResponseToken']
            self.WX_TEMPUTER = temp['wx']['temputure']
            self.MY_QR_ID = temp['wx']['MyQRId']
            self.OPENAI_APPID = temp['openAi']['appId']
            self.AL_MODELS = temp['openAi']['model']
            self.OPENAI_URL = temp['openAi']['url']
            self.WX_REQUEST_TIMEOUT = temp['openAi']['wxRequestTimeout']
            self.WEB_REQUEST_TIMEOUT = temp['openAi']['webRequestTimeout']

            """web页面"""
            self.WEB_MOBILE_URL = temp['web']['mobile']['url']
            self.WITHE_LIST = ('')

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(_const, "_instance"):
            _const._instance = _const(*args, **kwargs)
        return _const._instance
