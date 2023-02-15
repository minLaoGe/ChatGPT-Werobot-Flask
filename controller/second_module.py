from flask import Flask, request, make_response,Blueprint
import hashlib
from wechatpy import parse_message, create_reply
from utils.globalConst import _const


blueprint = Blueprint('second_module', __name__,url_prefix='/api/whocare')

WECHAT_TOKEN = _const().TOKEN


@blueprint.route('/weixin', methods=['GET', 'POST'])
def wechat():
    args = request.args
    print(args)

    signature = args.get('signature')
    timestamp = args.get('timestamp')
    nonce = args.get('nonce')
    echostr = args.get('echostr')

    # 1. 将token、timestamp、nonce三个参数进行字典序排序
    temp = [WECHAT_TOKEN, timestamp, nonce]
    temp.sort()
    # 2. 将三个参数字符串拼接成一个字符串进行sha1加密
    temp = "".join(temp)
    # sig是我们计算出来的签名结果
    sig = hashlib.sha1(temp.encode('utf8')).hexdigest()

    # 3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
    if sig == signature:
        # 根据请求方式.返回不同的内容 ,如果是get方式,代表是验证服务器有效性
        # 如果POST方式,代表是微服务器转发给我们的消息
        if request.method == "GET":
            return echostr
        else:
            xml = request.data
            msg = parse_message(xml)
            if msg.type == 'text':
                reply = create_reply(msg.content, msg)
            else:
                reply = create_reply('Sorry, can not handle this for now', msg)
            return reply.render()
    else:
        return 'errno', 403



