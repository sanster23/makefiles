"""
    Simple python hello world application written using Flask
    for the demonstration of usage of Makefiles.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return '<H2> HELLO WORLD </H2>'


@app.route('/hi', methods=['GET'])
def greet_name():
    return 'Hi stranger!!!'

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5555)

    # import time
    #
    # def fact_tail(n, a):
    #     if n == 0:
    #         return a
    #
    #     return n*fact_tail(n-1, n*a)
    #
    # def fact(n):
    #     if n == 0:
    #         return 1
    #     return n*fact(n-1)
    # then = time.time()
    # fact(100)
    # now = time.time()
    # print(then, now, now - then)
    #
    # then1 = time.time()
    # fact_tail(100,1)
    # now1 = time.time()
    # print(then1, now1, now1 - then1)

    def my_exp(a,b):
        if b == 0:
            return 1
        elif b > 0:
            return a * my_exp(a,b - 1)
        elif b < 0:
            return (1/a) * my_exp(a, b + 1)

    import math
    print('from math: ', math.pow(2, -2))
    print('from my_exp', my_exp(2, -2))
