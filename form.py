from flask_wtf import FlaskForm
from wtforms import StringField,FloatField, BooleanField, IntegerField,IntegerRangeField, RadioField, SelectField, URLField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, AnyOf

possible_pets = ["Cat","Dog","Porcupine","Turtle","Lizard","Pig","Ferret","Fish"]

class PetForm(FlaskForm):
    """Form to make a new pet"""

    name = StringField("Pet Name", validators=[InputRequired(message="Please enter a valid pet name")])

    species = SelectField("Species", 
                          choices = [(pet, pet) for pet in possible_pets])
    
    photo_url = URLField("Photo URL",validators=[Optional()])

    age = IntegerField("Age of Pet", validators=[Optional(),NumberRange(min=0,max=30, message="Please enter an age between 0 and 30")])

    notes = StringField("Pet Notes", validators=[Optional()])

    available = BooleanField("Available?")