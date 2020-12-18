from flask import Flask, render_template, redirect, request, url_for

# Imports for Google Authentication
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
import json
import os
import sqlite3
from oauthlib.oauth2 import WebApplicationClient
import requests
from db import init_db_command
from user import User

# Google Auth Configuration
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

# Flask app setup
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

############# GOOGLE AUTH #############
# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# Naive database setup
try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
############# GOOGLE AUTH #############

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/user')
def userPage():
    return render_template('user.html')


@app.route('/registerTeam')
def registerTeam():
    return render_template('registerTeam.html')


@app.route('/recordTraining')
def recordTraining():
    return render_template('recordTraining.html')


@app.route('/team')
def teamPage():
    return render_template('teamPage.html')


@app.route('/worldStats')
def internationaPage():
    return render_template('internationaPage.html')


if __name__ == '__app__':
    app.run(
        host='0.0.0.0',
        port=8080)  # This line is required to run Flask on repl.it