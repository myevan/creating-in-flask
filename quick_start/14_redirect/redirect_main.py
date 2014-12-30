from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))
    return "Index Page"

@app.route('/login')
def login():
    return "Login Page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

