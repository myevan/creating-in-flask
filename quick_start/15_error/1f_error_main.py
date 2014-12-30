from flask import Flask
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    abort(401)

    return "NEVER_EXECUTED"

@app.errorhandler(404)
def page_not_found(error):
    return 'PAGE_NOT_FOUND', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

