from flask import Flask, redirect, url_for, session,render_template, request
import random
from forms import RecordTraining
from user import *
import sqlite3
import google_auth 
from flask_login import UserMixin
from db import get_db
#from app import user_info


app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY']='skatezy'


@app.route('/')  # '/' for the default page
def home():
	return render_template(
		'login.html',  # Template file path, starting from the templates folder. 
	)

@app.route('/login')
def login(): #if user is signed in then redirect to personal
  return render_template('googlelogin.html')

@app.route('/personal')
def personal():
  con = sqlite3.connect("sqlite_db")  
  con.row_factory = sqlite3.Row  
  cur = con.cursor()  
  cur.execute("select * from recordTraining")  
  rows = cur.fetchall()  
  return render_template("personal.html",rows = rows)   
  #return render_template('personal.html')

@app.route('/saverecord',methods=["POST"])
def save_record():
  form = RecordTraining()
  date_skated=request.form['date_skated']
  distance_skated=request.form['distance_skated']
  time_spent=request.form['time_spent']
  db = get_db()
  with sqlite3.connect("sqlite_db") as con:
    cur = con.cursor()
    cur.execute(
      "INSERT into recordTraining (date_skated, distance_skated, time_spent) VALUES (?, ?, ?)",
      (date_skated, distance_skated, time_spent))
    db.commit()

  #video uploaded to be done later
  # method to save recordTraining
  return render_template('recordTraining.html',form=form) 

@app.route('/recordTraining', methods=['GET', 'POST'])
def recordtraining():
  form = RecordTraining()
  #if form.is_submitted():
    #result = request.form
    #result is dictionary so we can get data 
    #return render_template('personal.html',result=result) 
  return render_template('recordTraining.html',form=form)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)