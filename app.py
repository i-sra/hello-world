from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello-world')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/<name>')
def name(name):
    return '<h1>Hello {}, World!</h1>'.format(name)
