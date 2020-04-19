from flask import Flask
app = Flask(__name__)
#export FLASK_APP=flaskblog.py -> No spaces extra
#export DEBUG_MODE=1 -> Auto load server changes

@app.route('/')
def hello_world():
    return '<h1>Hello, Anand!</h1>'

@app.route('/about')
def about_page():
    return "<h3>It's a About Page </h3>"