from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.logger.debug('debug')
    app.logger.warning('warning')
    app.logger.error('error')
