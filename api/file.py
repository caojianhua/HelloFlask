from flask import Blueprint, Flask, jsonify, request

file_ctrl = Blueprint('file_ctrl', __name__)


@file_ctrl.route("/list", methods=["GET"])
def get_all_users():
    return jsonify({"code": 0, "data": "file list", "msg": "查询成功"})


