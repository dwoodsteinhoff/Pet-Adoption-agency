from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

spot = Pet(name = 'Spot',
            species ='Dog',
            photo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlKA8qZNqhtgBFY9FgufCDwuPjoi0XNABHQA&s',
            age = 4,
            notes = 'He loves to cuddle!')

db.session.add(spot)
db.session.commit()