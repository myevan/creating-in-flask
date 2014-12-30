# -*- coding:utf8 -*-
from flask import Flask
from flask import request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads' + secure_filename(f.filename))

if __name__ == '__main__':
    pass

    # TODO: 예제 작성