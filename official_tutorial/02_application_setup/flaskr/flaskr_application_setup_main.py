import sqlite3

from flask import Flask

DEBUG = True
DATA_BASE = '/tmp/flaskr.db'
SECRET_KEY = 'DEVELOPMENT_KEY'
USER_NAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()