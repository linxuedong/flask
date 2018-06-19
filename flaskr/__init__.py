# __inti__.py 的两个用途：
# 1. It will contain the application factory
# 2. 告诉 Python `flaskr` 文件夹时 Package

import os

from flask import Flask
from . import blog

def create_app(test_config=None):
    # 创建 flask 实例
    app = Flask(__name__, instance_relative_config=True)
    # __name__ 为当前 module 的名字
    # instance_relative_config 告诉 app configuration 文件是相对于 instance 文件夹


    # 设置 app 的默认配置
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # SECRET_KEY 用于 保护数据安全
    # 在 development 时，为了方便设置为 'dev'
    # 在部署时 应该设置为 random value

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
        # 重写 config.py 文件的配置
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
        # 确认 app.instance_path 存在
        # Flask 不自动创建 instance folder，
        # 但是 Flask 会在 instance 文件夹中创建 SQLite database 文件
    except OSError:
        print('已经创建 instance 文件夹')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    with app.app_context():
        db.init_db()
        print('make some change')

    return app


def get_db():
    if 'db' not in g:
        g.db = connect_to_database()

    return g.db

@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
