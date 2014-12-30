import sqlite3

from flask import Flask
from flask import g

from contextlib import closing

DEBUG = True
DATABASE = '/tmp/flaskr.db'
SECRET_KEY = 'DEVELOPMENT_KEY'
USER_NAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    print('before_request')
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    print('teardown_request')
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return ''

if __name__ == '__main__':
    with app.test_client() as c:
        c.get('/')
