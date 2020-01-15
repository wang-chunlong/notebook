"""服务程序入口"""
from flask import Flask

from blueprints import bp
from models import db

app = Flask(__name__)
app.config.from_pyfile("config.py")
app.register_blueprint(bp)

db.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
