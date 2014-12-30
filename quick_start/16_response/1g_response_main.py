from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response("""{"a":1}""")
    resp.headers['X-Something'] = 'A Value';
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

