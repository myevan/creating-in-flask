from flask import Flask

from flask import url_for

app = Flask(__name__)

if __name__ == '__main__':
    with app.test_request_context():
        print url_for('static', filename='style.css')
