#!/usr/bin/python3

from flask import Flask, request
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    name = request.args.get('name', '')
    return 'hello ' + name + '!'

if __name__ == '__main__':
    app.run()