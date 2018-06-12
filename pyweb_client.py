# coding: utf-8

from flask import Flask
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'helloooooo'


@app.route('/nihao')
def nihao():
    return '你好'
