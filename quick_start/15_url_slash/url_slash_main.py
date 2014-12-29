from flask import Flask

app = Flask(__name__)

@app.route('/projects/')
def index():
    return "The project Page"

@app.route('/about')
def hello():
    return "The about Page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

