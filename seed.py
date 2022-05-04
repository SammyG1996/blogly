# Below is a seed file I created to seed my database with information.

from models import Blogly, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Blogly.query.delete()

#Add users
samuel = Blogly(first_name = 'Samuel', 
                last_name = 'Gonzalez', 
                image_url = 'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

sara = Blogly(first_name = 'Sara', 
                last_name = 'Smith', 
                image_url = 'https://images.pexels.com/photos/4063856/pexels-photo-4063856.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

mike = Blogly(first_name = 'Mike', 
                last_name = 'Maletta', 
                image_url = 'https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

# Add new objects to session, so they'll persist
db.session.add(samuel)
db.session.add(sara)
db.session.add(mike)

# Commit--otherwise, this never gets saved!
db.session.commit()