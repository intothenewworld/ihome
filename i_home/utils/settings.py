
import os
from utils.functions import get_db_uri

# 路径配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

templates_dir = os.path.join(BASE_DIR, 'templates')
static_dir = os.path.join(BASE_DIR, 'static')

# 上传路径配置
UPLOAD_DIRS = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload')

# 数据库配置
DATABASE = {
    'USER': 'root',             # 用户
    'PASSWORD': 'yl92939192',   # 密码
    'HOST': '127.0.0.1',        # 地址
    'PORT': '3306',             # 端口
    'DB': 'mysql',              # 数据库
    'DRIVER': 'pymysql',        # 驱动
    'NAME': 'flask_for_ihome',           # 数据库名称
}

SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)