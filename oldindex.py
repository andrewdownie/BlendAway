#!/usr/bin/python3
from flask import Flask, jsonify, render_template, request
app = Flask(__name__, static_url_path='')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
     return app.send_static_file('index.html')
#    return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True)