from flask import Flask, request, session
import pytest

app = Flask(__name__)


@app.before_request
def before_request():
    print('before request')
    return 'use this function instead of hello'


@app.route('/request/hello')
def hello():
    print('during view')
    return 'hello world'


@app.teardown_request
def show_teardown(exception):
    print('teardown request')

with app.test_request_context():
    print('during with block')
