from flask import Flask
from flask import request

app = Flask(__name__)

if __name__ == '__main__':
    with app.test_request_context('/hello', method='POST'):
        assert request.path == '/hello'
        assert request.method == 'POST'