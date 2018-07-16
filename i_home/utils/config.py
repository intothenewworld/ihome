
import redis
from utils.settings import SQLALCHEMY_DATABASE_URI
from flask_session import Session


class Config():

    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host='119.23.52.108', port='6379',
                                password='yl92939192')
    SESSION_KEY_PREFIX = 's_aj_'

