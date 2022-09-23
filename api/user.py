from flask import Blueprint, jsonify, request

from app import db
from app.models import User

user_ctrl = Blueprint('user_ctrl', __name__)

@user_ctrl.route("/list", methods=["GET"])
def get_all_users():
    users = db.session.query(User).all()
    user_list = []
    for item in users:
        user_list.append({
            "id": item.id,
            "name": item.name,
            "email": item.email
        })
    return jsonify({
        "code": 0, 
        "data": user_list, 
        "msg": "查询成功"})


@user_ctrl.route("/create", methods=["GET"])
def create_new_users():
    user = User("name3", "email3")
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "code": 0, 
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }, 
        "msg": "创建成功"})
