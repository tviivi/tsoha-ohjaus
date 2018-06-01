from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2, max=5, message="testierror-viesti")])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False