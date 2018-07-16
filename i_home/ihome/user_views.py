
import os
import re

from flask import Blueprint, render_template, request, jsonify, session

from ihome.models import db, User
from utils import status_code
from utils.settings import UPLOAD_DIRS
from utils.functions import is_login

user_blueprint = Blueprint('ihome', __name__)


@user_blueprint.route('/')
def hello_world():

    return 'Hello World!'


@user_blueprint.route('/createtable/')
def create_table():
    db.create_all()
    return 'success'


@user_blueprint.route('/regist/', methods=['GET', 'POST'])
def regist():
    """
    注册操作
    :return:
    """
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user_dict = request.form

        mobile = user_dict.get('mobile', None)
        password = user_dict.get('password', None)
        password2 = user_dict.get('password2', None)

        # 只要其中一个为空，就返回False, 只有都存在才会返回True
        if not all([mobile, password, password2]):
            return jsonify(status_code.USER_REGISTER_PARAMS_ERROR)

        # 对输入的电号码进行正则匹配，如果没匹配上就返回输入的电话号码规则不正确
        if not re.match(r'^1[34578]\d{9}$', mobile):
            return jsonify(status_code.USER_REGISTER_MOBLIE_ERROR)

        # 如果用户已经在数据库中存在，则返回用户已经存在
        if User.query.filter(User.phone==mobile).count():
            return jsonify(status_code.USER_REGISTER_MOBLIE_IS_EXSITS)

        # 判断两次密码是否一致， 不一致返回两次密码不一致
        if password != password2:
            return jsonify(status_code.USER_REGISTER_PASSWORD_ERROR)

        user = User()
        user.phone = mobile
        user.name = mobile
        user.password = password

        try:
            # add_upfate()调用models定义的方法进行提交到数据库
            user.add_update()
            return jsonify(status_code.SUCCESS)

        except Exception as e:
            print(e)
            return jsonify(status_code.DATABASE_ERROR)


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    """
    :return:get请求过来跳转登录界面, post请求过来返回用户是否成功登录信息的数据
    """
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_dict = request.form

        mobile = user_dict.get('mobile', None)
        password = user_dict.get('password', None)

        if not all([mobile, password]):
            return jsonify(status_code.PARAMS_ERROR)

        if not re.match(r'^1[34578]\d{9}$', mobile):
            return jsonify(status_code.USER_REGISTER_MOBLIE_ERROR)

        user = User.query.filter(User.phone==mobile).first()

        if user:
            if user.check_pwd(password):
                session['user_id'] = user.id
                return jsonify(status_code.SUCCESS)
            else:
                return jsonify(status_code.USER_LOGIN_PASSWORD_IS_ERROR)

        else:
            return jsonify(status_code.USER_NOT_EXSITS)


@user_blueprint.route('/my/', methods=['GET'])
@is_login
def my():
    return render_template('my.html')


@user_blueprint.route('/user/', methods=['GET'])
@is_login
def get_user():
    """
    获取当前登录用户数据返回给前端
    :return:
    """
    id = session['user_id']
    user = User.query.filter(User.id==id).first()
    return jsonify(user=user.to_basic_dict(), code='200')


@user_blueprint.route('/profile/', methods=['GET'])
@is_login
def profile():

    return render_template('profile.html')


@user_blueprint.route('/user/', methods=['PUT'])
@is_login
def user_profile():
    """上传照片文件的接口和改名字的接口"""

    user_dict = request.form
    file_dict = request.files

    if 'avatar' in file_dict:

        f1 = file_dict.get('avatar', None)

        if re.match(r'^images/.*$', f1.mimetype):
            return jsonify(status_code)

        url = os.path.join(UPLOAD_DIRS, f1.filename)
        f1.save(url)

        user = User.query.filter(User.id==session['user_id']).first()
        image_url = os.path.join('/static/upload', f1.filename)
        user.avatar = image_url
        try:
            user.add_update()
            return jsonify(code=status_code.OK, url=image_url)
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)

    elif 'name' in user_dict:
        name = user_dict.get('name')
        if User.query.filter(User.name==name).count():
            return jsonify(status_code.USERNAME_IS_EXSITS)
        id = session['user_id']
        user = User.query.filter(User.id==id).first()
        user.name = name
        try:
            user.add_update()
            return jsonify(status_code.SUCCESS)
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)


@user_blueprint.route('/auth/', methods=['GET'])
@is_login
def get_auth():
    return render_template('auth.html')


@user_blueprint.route('/auths/', methods=['GET'])
@is_login
def get_user_auth():

    user = User.query.get(session['user_id'])
    try:
        if user.id_card:
            return jsonify(code=status_code.OK,
                           id_name=user.id_name,
                           id_card=user.id_card)
        else:
            return jsonify(code=status_code.USER_IS_NOT_AUTH)
    except:
        return jsonify(status_code.PARAMS_ERROR)


@user_blueprint.route('/auths/', methods=['PUT'])
@is_login
def update_auth():
    user_dict = request.form
    id_name = user_dict.get('id_name')
    id_card = user_dict.get('id_card')

    if not all([id_name, id_card]):
        return jsonify(status_code.PARAMS_ERROR)

    if not re.match(r'^[1-9]\d{17}$', id_card):
        return jsonify(status_code.USER_AUTH_IS_ERROR)
    try:
        user= User.query.get(session['user_id'])
        user.id_card = id_card
        user.id_name = id_name

        user.add_update()
        return jsonify(status_code.SUCCESS)

    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)


# 退出
@user_blueprint.route('/logout/', methods=['DELETE'])
@is_login
def user_logut():
    session.clear()
    return jsonify(code=status_code.OK)














