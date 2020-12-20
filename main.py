from flask import Flask, redirect, url_for, session,render_template, request
import random
from forms import RecordTraining, RegisterTeam
from user import *
import sqlite3
import google_auth 
from flask_login import UserMixin
from db import get_db
from radar_ice_rink import get_ice_rink_address, parce_rink_name

#from app import user_info

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static filesa
)
app.config['SECRET_KEY']='skatezy'



@app.route('/',methods=["GET"])  # '/' for the default page
def home():
  # TODO: FIX THIS
  #ip_address = "68.146.3.57"
  ip_address = request.environ['REMOTE_ADDR']
  #ip_address = request.remote_addr
 
  list_of_rinks = get_ice_rink_address("68.146.3.57")
  name_of_rinks = parce_rink_name(list_of_rinks)
  return render_template('login.html', ip_address=ip_address, name_of_rinks=name_of_rinks) 

  
@app.route('/login')
def login(): #if user is signed in then redirect to personal
  return render_template('googlelogin.html')
@app.route('/login', methods = ["POST"])
def logingData():
  name = request.form['userName1']
  email = request.form['email1']
  image = request.form['profilePic1']
  
  db = get_db()
  with sqlite3.connect("sqlite_db") as con:
    cur = con.cursor()
    cur.execute(
      "INSERT into user (name, email, image) VALUES (?, ?, ?)",
      (name, email, image))
    db.commit() 
  
  return render_template('internationalPage.html', form=form)

@app.route('/lol')
def lol():
  con = sqlite3.connect("sqlite_db")  
  con.row_factory = sqlite3.Row  
  cur = con.cursor()  
  cur.execute("select * from user")  
  rows = cur.fetchall()  
  for i in rows:
    print(i)
  return render_template("internationalPage.html",rows = rows) 
  #var googleProfile = googleUser.getBasicProfile()
  #var userName = googleProfile.getName()
  #var email = googleProfile.getEmail()
  #var profilePic = googleProfile.getImageUrl()
  

   
@app.route('/saveteam',methods=["POST"])
def saveteam():
  form = RegisterTeam()
  team_name = request.form['team_name']
  team_description = request.form['team_description']
  rink_location = request.form['rink_location']
  member_emails = request.form['member_emails']
  db = get_db()
  with sqlite3.connect("sqlite_db") as con:
    cur = con.cursor()
    cur.execute(
      "INSERT into registerTeam (team_name, team_description, rink_location, member_emails) VALUES (?, ?, ?, ?)",
      (team_name, team_description, rink_location, member_emails))
    db.commit()
  return render_template('registerTeam.html', form=form)



@app.route('/registerTeam')
def registerTeam():
  form = RegisterTeam()
  return render_template('registerTeam.html',form=form)

@app.route('/team')
def teampage():
  con = sqlite3.connect("sqlite_db")  
  con.row_factory = sqlite3.Row  
  cur = con.cursor()  
  cur.execute("select * from registerTeam")  
  rows = cur.fetchall()

  ip_address = request.environ['REMOTE_ADDR']
  #ip_address = request.remote_addr
 
  list_of_rinks = get_ice_rink_address("68.146.3.57")
  name_of_rinks = parce_rink_name(list_of_rinks)
  
  return render_template("team.html",rows = rows,ip_address=ip_address, name_of_rinks=name_of_rinks) 

@app.route('/recordTraining', methods=['GET', 'POST'])
def recordtraining():
  form = RecordTraining()
  #if form.is_submitted():
    #result = request.form
    #result is dictionary so we can get data 
    #return render_template('personal.html',result=result) 
  return render_template('recordTraining.html',form=form)
@app.route('/personal')
def personal():
  con = sqlite3.connect("sqlite_db")  
  con.row_factory = sqlite3.Row  
  cur = con.cursor()  
  cur.execute("select * from recordTraining")  
  rows = cur.fetchall()  

  ip_address = request.environ['REMOTE_ADDR']
  #ip_address = request.remote_addr
 
  list_of_rinks = get_ice_rink_address("68.146.3.57")
  name_of_rinks = parce_rink_name(list_of_rinks)
  return render_template("personal.html",rows = rows, ip_address=ip_address, name_of_rinks=name_of_rinks)   
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

@app.route('/base')
def base_html():
  return render_template('base.html')

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)

