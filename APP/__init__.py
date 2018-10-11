from flask import Flask

# from APP.admin import admin as admin_blueprint
from APP.home import home as home_blueprint

from .config import DevConfig

from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect


app = Flask(__name__)
app.debug = True

app.config.from_object(DevConfig)

# app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(home_blueprint)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/farmfood?charset=utf8'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# csrf = CsrfProtect()
# csrf.init_app(app)
