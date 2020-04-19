from flask import Flask
app = Flask(__name__)
#to use "flask run" set below environment variables
#export FLASK_APP=flaskblog.py -> No spaces extra
#export DEBUG_MODE=1 -> Auto load server changes

#to link multiple routes to same page
@app.route('/home')
@app.route('/')
def home():
    return '<h1>Hello, Anand!</h1>'


@app.route('/about')
def about_page():
    return "<h3>It's a About Page </h3>"

#to make it work with "python flaskblog.py" instead of "flask run" add below
if __name__=="__main__":
    app.run(debug=True)