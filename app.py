
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/apple')
def hello_apple():
    return 'Hello Apple!'

@app.route('/banana')
def hello_banana():
    return 'Hello Banana'

if __name__ == '__main__':
    app.run()
