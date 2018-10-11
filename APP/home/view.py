from . import home
from flask import render_template, redirect, url_for, request, make_response
from ..models import User, Foods, CartFood
from flask_sqlalchemy import SQLAlchemy
from APP.database import db_session
from .form import SigninForm


@home.route('/')
@home.route('/index')  # URL路径
def index():
    foods = Foods.query.all()
    return render_template('index.html', foods=foods)  # 模板函数


@home.route('/about-us')
def about_us():
    return render_template('about-us.html')


@home.route('/cart')
def cart():
    food = CartFood.query.all()
    all_prices = 0
    for food_P in food:
        all_prices += float(food_P.prices)

    return render_template('cart.html', food=food, all_prices=all_prices)


@home.route('/checkout')
def checkout():
    food = CartFood.query.all()
    all_prices = 0
    for food_P in food:
        all_prices += float(food_P.prices)
        all_pricesT = all_prices + 5.00
    return render_template('checkout.html', food=food, all_prices=all_prices, all_pricesT=all_pricesT)


@home.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')


@home.route('/shop')
def shop(prices=None):
    foods = Foods.query.all()
    s = request.args.get('s')
    if s:
        foods = Foods.query.filter_by(name=s)
        return render_template('shop.html', foods=foods)
    else:
        return render_template('shop.html', foods=foods)


@home.route('/shop-list')
def shop_list():
    return render_template('shop-list.html')


@home.route('/main')
def main():
    return render_template('main.html')


@home.route('/addfood/', methods=['GET', 'POST'])
def addfood(name=None, prices=None, img=None):
    # ids = request.args.get('ids')
    name = request.args.get('name')
    prices = request.args.get('prices')
    img = request.args.get('img')
    # print(ids, name, prices)
    food = CartFood(name=name, prices=prices, img=img)

    db_session.add(food)
    db_session.commit()

    return redirect(url_for('home.cart', name=name, prices=prices, img=img))  # 重定向至Cart URL


@home.route('/removecart', methods=['GET', 'POST'])
def removecart(name=None):
    name = request.args.get('name')
    # print(name)

    cartfood = CartFood.query.filter_by(name=name).first()
    # print(cartfood)
    db_session.delete(cartfood)
    db_session.commit()

    return redirect(url_for('home.cart', name=name))


@home.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if request.method == 'GET':
        return render_template('signin.html', form=form)
    else:
        user = User.query.filter(User.name == form.name.data,
                                 User.password == form.password.data).first()
        if user:
            # login_user(user)
            return render_template('index.html')
        else:

            return render_template("signin.html", form=form)


@home.route('/shipping_details', methods=['GET', 'POST'])
def shipping_details():
    return render_template('shipping_details.html')
