from sqlalchemy import  Column, String, DATETIME, DateTime
from datetime import datetime
from app import db

"""消息表"""

class Message(db.Model):
    id =  Column(String(300), primary_key=True)
    message_content =  Column(String())
    user_id =  Column(String(300))
    create_time=Column(DATETIME,default=datetime.utcnow)
    ip=Column(String(100))
    return_content=Column(String())
    def __repr__(self):
        return '<User %r>' % self.username

"""资源表"""
# class Access(db.Model):
#     user_role = Column(String(50), nullable=False)
#     authority = Column(String(50), nullable=False)
#
#     def __repr__(self):
#         return f"<Access user_role={self.user_role} authority={self.authority}>"


"""用户表"""
class User(db.Model):
    __tablename__ = "user"
    appid = Column(String(120), primary_key=True, comment='用户id，微信生成')
    username = Column(String(300), nullable=False, comment='用户名称')
    password = Column(String(255), nullable=False, comment='密码')
    enabled = Column(String(1), nullable=False, comment='是否禁用0否1是')
    create_time = Column(DateTime, default=datetime.utcnow, comment='创建时间')
    update_time = Column(DateTime, default=datetime.utcnow, comment='更新时间')

# """权限表"""
# class Authorities(db.Model):
#     __tablename__ = 'authorities'
#     appid = Column(String(120), primary_key=True)
#     authority = Column(String(50), nullable=False)
#     create_time = Column(DateTime, default=None)
#     update_time = Column(DateTime, default=None)
#     id = Column(String(300), nullable=False)