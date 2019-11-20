
from typing import List

from flask import Flask, render_template

from models import Photo, User, db

app = Flask(__name__)
# 内存 sqlite:///:memory: (or, sqlite://)
# 相对路径 sqlite:///relative/path/to/file.db
# 绝对路径 sqlite:////absolute/path/to/file.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)


@app.route('/')
def hello_world():
    db.create_all()
    # user = User("张三","qqq@qq.com")
    # db.session.add(user)
    # db.session.commit()
    user: User = User.query.first()
    import os
    # filenamelist = list(os.walk("static/img"))
    # for name in filenamelist[0][2]:
    #     photo = Photo(os.path.join(os.path.abspath(filenamelist[0][0]), name), "QQ")
    #     db.session.add(photo)
    # db.session.commit()
    photo_list: List[Photo] = Photo.query.filter_by(label="QQ").all()
    photo_list = [{
        "src": "/".join(img.photo_name.split(os.path.sep)[-3:]),
        "alt": img.photo_name.split(os.path.sep)[-1],
    } for img in photo_list]
    return render_template('index.html', title=user.username, img=photo_list)


if __name__ == '__main__':
    app.run(debug=True)
