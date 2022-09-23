from app import db

from flask_admin.contrib.sqla import ModelView

class UserModelView(ModelView):
    column_searchable_list = ['name', 'email']
    page_size = 50


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %s %s>' % (self.name, self.email)