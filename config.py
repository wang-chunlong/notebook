"""配置文件"""
# 内存 sqlite:///:memory: (or, sqlite://)
# 相对路径 sqlite:///relative/path/to/file.db
# 绝对路径 sqlite:////absolute/path/to/file.db
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = True
