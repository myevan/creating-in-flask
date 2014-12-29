from flask import Flask

from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "The project Page"

@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile():
    pass

if __name__ == '__main__':
    with app.test_request_context():
        print url_for('index')
        print url_for('login')
        print url_for('login', next='/')
        print url_for('profile', username='Jaru')
