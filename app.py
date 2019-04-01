"""
    Simple python hello world application written using Flask
    for the demonstration of usage of Makefiles.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return '<H2> HELLO WORLD </H2>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
