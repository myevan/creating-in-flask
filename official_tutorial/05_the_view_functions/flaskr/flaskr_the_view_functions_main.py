import sqlite3
import json

from flask import Flask
from flask import g, session, abort, request, flash, redirect, url_for

from contextlib import closing

DEBUG = True
DATABASE = '/tmp/flaskr.db'
SECRET_KEY = 'DEVELOPMENT_KEY'
USERNAME = 'admin'
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
def show_entries():
    cur = g.db.execute('SELECT title, text FROM entries ORDER BY ID DESC')
    entries = [dict(title=title, text=text) for title, text in cur.fetchall()]
    return json.dumps(entries, indent=4)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    title = request.form['title']
    text = request.form['text']
    g.db.execute('INSERT INTO entries (title, text) values (?, ?)', [title, text])
    g.db.commit()

    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'INVALID_USERNAME'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'INVALID_PASSWORD'
        else:
            session['logged_in'] = True

            flash('You ware logged in')
            return redirect(url_for('show_entries'))

    return 'LOGIN_FORM:' + error

@app.route('/logout')
def logout():
    session.pop('logged_in', None)

    flash('You ware logged out')

    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    with app.test_client() as c:
        print(c.get('/').data)
        print(c.post('/login', data=dict(username='admin', password='default')).data)
        print(c.post('/add', data=dict(title='TITLE', text='TEXT')).data)
        print(c.get('/logout').data)
