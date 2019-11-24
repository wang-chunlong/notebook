"""蓝图"""
import os
from typing import List

from flask import Blueprint, render_template

from models import db, User, Photo

bp = Blueprint("bp", __name__)


@bp.route('/')
def hello_world():
    db.create_all()
    # user = User("张三","qqq@qq.com")
    # db.session.add(user)
    # db.session.commit()
    user: User = User.query.first()
    # filenamelist = list(os.walk("static/img"))
    # for name in filenamelist[0][2]:
    #     photo = Photo(os.path.join(os.path.abspath(filenamelist[0][0]), name), "QQ")
    #     db.session.add(photo)
    # db.session.commit()
    photo_list: List[Photo] = Photo.query.filter_by(label="QQ").all()
    img_list = [{
        "src": "/".join(img.photo_name.split(os.path.sep)[-3:]),
        "alt": img.photo_name.split(os.path.sep)[-1],
    } for img in photo_list]
    return render_template('index.html', title=user.username, img=img_list)
