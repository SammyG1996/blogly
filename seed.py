# Below is a seed file I created to seed my database with information.

from turtle import title
from unicodedata import name
from models import Blogly, PostTag, Posts, Tags, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Blogly.query.delete()
Posts.query.delete()

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

# Add some posts
samuel1 = Posts(title='My First Post', 
            content='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
            user_id=1)

samuel2 = Posts(title='My Second Post', 
            content='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
            user_id=1)

samuel3 = Posts(title='My Third Post', 
            content='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
            user_id=1)

sara1 = Posts(title='My First Post', 
            content='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
            user_id=2)

sara2 = Posts(title='My Second Post', 
            content='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
            user_id=2)

sara3 = Posts(title='My Third Post', 
            content='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
            user_id=2)

mike1 = Posts(title='My First Post', 
            content='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
            user_id=3)

mike2 = Posts(title='My Second Post', 
            content='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
            user_id=3)

mike3 = Posts(title='My Third Post', 
            content='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
            user_id=3)


tag1 = Tags(name='live')

tag2 = Tags(name='laugh')

tag3 = Tags(name='love')


post_tag1 = PostTag(post_id=1, tags_id =2)

post_tag2 = PostTag(post_id=3, tags_id =1)

post_tag3 = PostTag(post_id=9, tags_id =3)







# Add new users to session, so they'll persist
db.session.add(samuel)
db.session.add(sara)
db.session.add(mike)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add new posts to session, so they'll persist
db.session.add(samuel1)
db.session.add(samuel2)
db.session.add(samuel3)

db.session.add(sara1)
db.session.add(sara2)
db.session.add(sara3)

db.session.add(mike1)
db.session.add(mike2)
db.session.add(mike3)

# Commit--otherwise, this never gets saved!
db.session.commit()

db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)

# Commit--otherwise, this never gets saved!
db.session.commit()

db.session.add(post_tag1)
db.session.add(post_tag2)
db.session.add(post_tag3)

# Commit--otherwise, this never gets saved!
db.session.commit()
