from flask_wtf import FlaskForm 
from wtforms import IntegerField, DateTimeField, SubmitField, FileField, StringField
from wtforms.fields.html5 import EmailField

class RecordTraining(FlaskForm):
  date_skated = DateTimeField('Date Skated:')
  distance_skated = IntegerField('Distance skated (km):')
  time_spent = IntegerField('Time Spent:')
  video_uploaded = FileField('Video of Skating:')
  submit = SubmitField('Record Training!')

class RegisterTeam(FlaskForm):
  team_name = StringField('Team Name:')
  team_description = StringField('Team description:')
  rink_location = IntegerField('Coordinates of your skating rink')
  member_emails = EmailField('Enter your friend emails')
  submit = SubmitField('Register Team!')
  