from modulefinder import Module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

import os


APP_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/db/app.db'.format(APP_ROOT_PATH)

app.config.from_object(__name__)

admin = Admin(app, name='microblog', template_mode='bootstrap3')

from app.models import User, UserModelView

admin.add_view(UserModelView(User, db.session))

