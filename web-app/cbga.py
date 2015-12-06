'''
CBGA Analytics Center Web App

AUTHOR: Suhas, <github.com/jargnar>
LICENSE: MIT
'''
from flask import Flask, render_template, send_from_directory
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/outlook')
def outlook():
    return render_template('outlook.html')


@app.route('/trend')
def trend():
    return render_template('trend.html')


@app.route('/data/<path:path>')
def send_data(path):
    return send_from_directory('data', path)

if __name__ == '__main__':
    app.run(debug=True)
