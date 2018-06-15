from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2, max=15, message="The tasks name must be between 2 and 15 characters")])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False