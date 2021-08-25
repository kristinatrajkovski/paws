from flask import Flask, render_template
from data import users

app = Flask(__name__)

""" I removed the 'title=title' on the render_templates because they 
served no purpose """

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/profile/<string:user_id>")
def profile(user_id):
    person=users[user_id]
    return render_template('profile.html', person=person)

@app.route("/missing")
def missing():
    return render_template('missing.html')

@app.route("/found")
def found():
    return render_template('found.html')

@app.route("/adoption") #the fact that this is adoption and the 
def adoption():         #one below is adopt, could be confusing in the future
    return render_template('putfora.html')

@app.route("/adopt")
def adopt():
    return render_template('adopt.html')

@app.route("/messages")
def messages():
    return render_template('messages.html')
