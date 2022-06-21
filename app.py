from operator import ge
from flask import Flask, abort, redirect, render_template, url_for, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import data

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "Kristina": generate_password_hash("HelloWorld,01"),
    "Landon": generate_password_hash("HelloWorld,01")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route("/")
@auth.login_required
def home():
    pets = data.get_pets()
    return render_template('home.html', title= "Home", pets=pets, user=auth.current_user())

@app.route("/profile/<string:user_id>")
@auth.login_required
def profile(user_id):
    return render_template('profile.html', title="Profile", user=auth.current_user())

@app.route("/missing")
@auth.login_required
def missing():
    return render_template('missing.html', title= "Search for Missing Animal")

@app.route("/found")
@auth.login_required
def found():
    return render_template('found.html', title= "Report a Found Animal")

@app.route("/putfora")  
@auth.login_required
def putfora():         
    return render_template('putfora.html', title= "Put Animal Up for Adoption")

@app.route("/adopt")
@auth.login_required
def adopt():
    return render_template('adopt.html', title= "Adopt/Purchase an Animal")

@app.route("/messages")
@auth.login_required
def messages():
    return render_template('messages.html', title="Messages")

@app.route("/logout")
def logout():
    return render_template('logout.html', title="Messages"), 401

# @app.route("/report", methods = ['POST'])
# @auth.login_required
# def report():
#     return request.form['']
