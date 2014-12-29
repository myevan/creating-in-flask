from flask import Flask

from flask import request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'DO_THE_LOGIN'
    else:
        return 'SHOW_THE_LOGIN_FORM'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
