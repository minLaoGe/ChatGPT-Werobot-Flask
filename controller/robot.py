import json
import time

from werobot.replies import ImageReply

import utils.ExceptionConst as ue

from werobot import WeRoBot
import urllib
import requests
from utils.globalConst import _const
from flask import current_app
import utils.EventConst as uec
from utils.requestToGPT import sendToGPT

const = _const.instance()
robot = WeRoBot(
    token=const.TOKEN,  # 对应公众号的token设置
    # encoding_aes_key=const.AES_SECRET,# 明文传输不需要填写
    # app_id=const.APPID#明文传输不需要填写
)

# 明文模式不需要下面三项
robot.config["APP_ID"] = const.APPID
robot.config["APP_SECRET"] = const.APPSECREATE

client = robot.client
# robot.config['ENCODING_AES_KEY'] = ''

on_subscribe = '你好~\n我是智能管家GPT, 有什么能帮您的吗？/::$'
timeout = 30  # 超时时间


def get_citys_in_msg(msg):
    # 获取消息中包含的城市
    api_url = 'http://www.yangyingming.com/api/parse_city?%s' % (urllib.parse.urlencode({'msg': msg}))
    citys = urllib.request.urlopen(api_url).read().decode('utf8')
    return citys


def get_weather(city):
    # 获取天气数据
    url = 'http://wthrcdn.etouch.cn/weather_mini'
    param = urllib.parse.urlencode({
        'city': city,
    })
    api_url = '%s?%s' % (url, param)
    wdata = requests.get(api_url).text
    return wdata


# 被关注
@robot.subscribe
def subscribe(message):
    return on_subscribe


@robot.key_click(uec.CONTRACTE_ME)
def contactMe(message):
    return ImageReply(message=message, media_id=const.MY_QR_ID)


@robot.key_click(uec.TALK_A_JOKE_EVENT)
def contactMe(message):
    return sendToGPT("讲个笑话吧")


@robot.text
def echo(message):
    current_app.logger.info("收到请求")
    text = message.content
    lenth = len(text.encode('gbk'))
    if lenth > 100:
        return ue.TOO_LONG_EXCEPTION
    start = time.time()

    try:
        print("当前使用的models是： ", const.AL_MODELS)
        result = sendToGPT(text)
        end = time.time()
        current_app.logger.info("请求用时:{}scend".format(str(end - start)))
        return result

    except Exception as e:
        end = time.time()
        current_app.logger.info("出现异常用用时:{}scend".format(str(end - start)))
        return ue.BUSY_EXCEPTION




def get_img_media_id(img_url, img_file_name):
    """
    * 上传临时素菜
    * 1、临时素材media_id是可复用的。
    * 2、媒体文件在微信后台保存时间为3天，即3天后media_id失效。
    * 3、上传临时素材的格式、大小限制与公众平台官网一致。
    """
    resource = urllib.request.urlopen(img_url)
    f_name = img_file_name
    with open(f_name, 'wb') as f:
        f.write(resource.read())
    # media_json = client.upload_media("image", open(r"./img_media.jpg", "rb")) ## 临时素材
    media_json = client.upload_permanent_media("image", open(r"./img_media.jpg", "rb"))  ##永久素材
    media_id = media_json['media_id']
    media_url = media_json['url']
    print('微信素材id:', media_id)
    return media_id


if __name__ == '__main__':
    sd = " sdf ".strip();
    print(sd)
