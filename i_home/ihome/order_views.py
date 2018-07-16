
from datetime import datetime

from flask import Blueprint, request, jsonify, session, render_template

from utils import status_code
from ihome.models import Order, House

order_blueprint = Blueprint('order', __name__)


@order_blueprint.route('/order/', methods=['POST'])
def order():
    """
    从booking.html通过post请求获取house_id, start_time, end_time,
    创建订单对象保存订单，最后返回立刻下单之后的一个订单详情数据的接口
    :return:
    """

    order_dict = request.form

    house_id = order_dict.get('house_id')
    start_time = datetime.strptime(order_dict.get('start_date'), '%Y-%m-%d')
    end_time = datetime.strptime(order_dict.get('end_date'), '%Y-%m-%d')

    if not all([house_id, start_time, end_time]):
        return jsonify(status_code.PARAMS_ERROR)

    if start_time > end_time:
        return jsonify(status_code)

    house = House.query.get(house_id)

    order = Order()
    order.user_id = session['user_id']
    order.house_id = house_id
    order.begin_date = start_time
    order.end_date = end_time
    order.house_price = house.price
    order.days = (end_time - start_time).days + 1
    order.amount = order.days * house.price

    try:
        order.add_update()
        return jsonify(code=status_code.OK,
                       order=order.to_dict())
    except:
        return jsonify(status_code.DATABASE_ERROR)


@order_blueprint.route('/order/', methods=['GET'])
def orders():

    return render_template('orders.html')


@order_blueprint.route('/show_order/', methods=['GET'])
def show_order():
    """获取该用户所有订单信息的接口"""
    orders = Order.query.filter(Order.user_id==session['user_id'])

    order_list = []
    for order in orders:
        order_list.append(order.to_dict())

    return jsonify(order_list=order_list,
                   code=status_code.OK)


@order_blueprint.route('/lorders/', methods=['GET'])
def client_lorders():

    return render_template('lorders.html')


@order_blueprint.route('/fd/', methods=['GET'])
def lorders_fd():

    houses = House.query.filter(House.user_id==session['user_id'])
    houses_ids = [house.id for house in houses]

    orders = Order.query.filter(Order.house_id.in_(houses_ids)).order_by(Order.id.desc())

    olist = [order.to_dict() for order in orders]

    # 第二种方式
    # house = houses = House.query.filter(House.user_id==session['user_id'])
    # order_list = []
    # for house in houses:
    #     pass

    return jsonify(olist=olist, code=status_code.OK)


@order_blueprint.route('/lorders/<int:id>/', methods=['PATCH'])
def order_status(id):

    status = request.form.get('status')

    order = Order.query.get(id)

    order.status = status

    if status == 'REJECTED':
        comment = request.form.get('comment')
        order.comment = comment

    try:
        order.add_update()
        return jsonify(code=status_code.OK)
    except:
        return jsonify(status_code.DATABASE_ERROR)

