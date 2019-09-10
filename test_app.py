# Test file
import app


def test_greet():
    assert app.greet_name() == 'Hi stranger!!!'


def test_hello_world():
    assert app.hello_world() == '<H2> HELLO WORLD </H2>'