from flask import Flask
from flask import request, make_response, render_template

app = Flask(__name__)

@app.route('/cookie/', methods=['GET'])
@app.route('/cookie/<username>', methods=['POST'])
def cookie(username=None):
    if request.method == 'POST':
        resp = make_response("SAVE")
        resp.set_cookie('username', username)
        return resp
    else:
        username = request.cookies.get('username', '')
        return make_response("LOAD:" + username)


if __name__ == '__main__':
    with app.test_client() as c:
        print c.post('cookie/TEST').data
        print c.get('cookie/').data
