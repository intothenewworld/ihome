

from flask import Flask

from ihome.user_views import user_blueprint
from ihome.house_views import house_blueprint
from ihome.order_views import order_blueprint
from utils.settings import templates_dir, static_dir
from utils.functions import init_ext


def create_app(config):

    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)

    app.register_blueprint(blueprint=user_blueprint, url_prefix='/ihome')
    app.register_blueprint(blueprint=house_blueprint, url_prefix='/ihome')
    app.register_blueprint(blueprint=order_blueprint, url_prefix='/order')

    app.config.from_object(config)

    init_ext(app=app)

    return app