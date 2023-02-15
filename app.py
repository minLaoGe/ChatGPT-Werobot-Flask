import datetime
from flask import Flask
from controller import first_module, second_module
from werobot.contrib.flask import make_view #使用make_view依赖到flask项目
from controller.robot import robot
from utils.globalConst import _const
from urllib.parse import quote_plus as urlquote
import logging



app = Flask(__name__)
const = _const()


# port=str(const.MYSQL_PORT)
# dbstr= f'mysql+pymysql://{const.MYSQL_USERNAME}:{urlquote(const.MYSQL_PASSWORD)}@{const.MYSQL_HOST}:{port}/{const.MYSQL_DB}?charset=utf8'
#
#
# app.config['SQLALCHEMY_DATABASE_URI'] = dbstr
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_POOL_SIZE'] = const.MYSQL_MAX_CACHE


app.register_blueprint(first_module.blueprint)
app.register_blueprint(second_module.blueprint)
app.add_url_rule(rule='/api/wx/weixin',        # WeRoBot挂载地址
                 endpoint='werobot',             # Flask的endpoint
                 view_func=make_view(robot),#robot是robot文件
                 methods=['GET', 'POST'])


if __name__ == '__main__':
    print('The following routes are available:')
    for rule in app.url_map.iter_rules():
        print(rule)

    app.debug = True
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M')
    loggerName = ('flask' +str(nowTime)).replace(" ","").replace(":",'')+'.log'
    # loggerName = 'abc.log'
    handler = logging.FileHandler('logs/'+loggerName, encoding='UTF-8')
    handler.setLevel(logging.DEBUG)  # 设置日志记录最低级别为DEBUG，低于DEBUG级别的日志记录会被忽略，不设置setLevel()则默认为NOTSET级别。
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0",port=3000,debug=True)

