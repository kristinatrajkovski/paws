from flask import Flask, render_template
from data import users

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', title="Home Page")

@app.route("/profile/<string:user_id>")
def profile(user_id):
    person=users[user_id]
    return render_template('profile.html', title="Profile", person=person)

@app.route("/missing")
def missing():
    return render_template('missing.html', title="Missing Dog")

@app.route("/found")
def found():
    return render_template('found.html', title="Report Found Dog")

@app.route("/adoption")
def adoption():
    return render_template('putfora.html', title="Put Dog Up for Adoption")

@app.route("/adopt")
def adopt():
    return render_template('adopt.html', title="Put Dog Up for Adoption")
