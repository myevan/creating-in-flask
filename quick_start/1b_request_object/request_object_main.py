from flask import Flask
from flask import request, render_template

app = Flask(__name__)

def valid_login(username, password):
    return username == 'USERNAME' and password == 'PASSWORD'

def log_the_user_in(username):
    return 'LOG_ON:' + username

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None

    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username or password'

    search_word = request.args.get('key', '')
    return render_template('login.html', error=error)

if __name__ == '__main__':
    with app.test_request_context('/login', method='GET'):
        assert request.path == '/login'
        assert request.method == 'GET'

    with app.test_request_context('/login', method='POST'):
        assert request.path == '/login'
        assert request.method == 'POST'
