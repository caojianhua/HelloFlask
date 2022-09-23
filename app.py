import os, sys

# 项目根路径
APP_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, APP_ROOT_PATH)  # 将项目根路径临时加入环境变量，程序退出后失效

from config.setting import SERVER_PORT
from app import app, db

from api.user import user_ctrl
from api.file import file_ctrl

app.register_blueprint(user_ctrl, url_prefix="/user")
app.register_blueprint(file_ctrl, url_prefix="/file")

app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=SERVER_PORT, debug=True)
