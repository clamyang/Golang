from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, world!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/project/')
def projects():
    return 'The project page'
