from flask import Flask, render_template
from data import users

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', title= "Home")

@app.route("/profile/<string:user_id>")
def profile(user_id):
    person=users[user_id]
    return render_template('profile.html', person=person, title=person['Name'], user_id=user_id)

@app.route("/missing")
def missing():
    return render_template('missing.html', title= "Search for Missing Animal")

@app.route("/found")
def found():
    return render_template('found.html', title= "Report a Found Animal")

@app.route("/putfora")  
def putfora():         
    return render_template('putfora.html', title= "Put Animal Up for Adoption")

@app.route("/adopt")
def adopt():
    return render_template('adopt.html', title= "Adopt/Purchase an Animal")

@app.route("/messages")
def messages():
    return render_template('messages.html', title= "Messages")
