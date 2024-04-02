from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///pet_adoption_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)

@app.route('/')
def home_page():

    pets = Pet.query.all()

    return render_template('home.html', pets = pets)

@app.route('/add', methods=["GET","POST"])
def add_pet():

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url= photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add_pet.html', form=form)
    
@app.route('/<int:pet_id>', methods=["GET"])
def view_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet_details.html', pet = pet)

@app.route('/<int:pet_id>/edit', methods=["GET","POST"])
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f"/{pet.id}")
    
    else:
        return render_template("edit_pet.html", form = form, pet=pet)