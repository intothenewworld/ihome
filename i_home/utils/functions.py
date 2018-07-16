
from flask import session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

db = SQLAlchemy()
se = Session()


def get_db_uri(DATABASE):
    """
    配置链接数据库的字符串的样式：'mysql+pymysql://root:yl92939192@localhost:3306/flask4'
    :param DATABASE: 数据库参数(在settings.py文件)
    :return: 返回样式：'mysql+pymysql://root:yl92939192@localhost:3306/flask4'
    """

    user = DATABASE.get('USER')
    password = DATABASE.get('PASSWORD')
    host = DATABASE.get('HOST')
    port = DATABASE.get('PORT')
    name = DATABASE.get('NAME')
    db = DATABASE.get('DB')
    driver = DATABASE.get('DRIVER')

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver,
                                           user, password,
                                           host, port, name)


def init_ext(app):

    db.init_app(app=app)
    se.init_app(app=app)


import functools
def is_login(view_fun):
    @functools.wraps(view_fun)
    def decorator():
        try:
            # 验证用户是否登录
            # if session['user_id']
            if 'user_id' in session:
                return view_fun()
            else:
                return redirect('/ihome/login/')
        except:
            return redirect('/ihome/login/')
    return decorator