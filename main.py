from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"
    
@app.route('/about')
def welcome():
  return "Welcome to my Flask site, &copy;2018"
@app.route('/login')
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
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it