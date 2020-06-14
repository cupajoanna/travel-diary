import os
from datetime import datetime
import json 
from random import choice, randint
import crud
import model
import server




def create_db():
    os.system('dropdb travel-diary')
    os.system('createdb travel-diary')
    model.db.create_all()




# Create cities, store them in list so we can use them
# to create pages


def city():

    with open('data/cities.json') as f:
         city_data = json.loads(f.read())

    cities_in_db = []

    for city in city_data:
        city_name, country_name, geo_lat, geo_lng = (city['city_name'], city['country_name'], city['geo_lat'], city['geo_lng'])
        # release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

        db_city = crud.create_city(city_name, country_name, geo_lat, geo_lng)

        cities_in_db.append(db_city)

    db.session.commit()
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime

    # TODO: create a movie here and append it to movies_in_db

def user():

    users_in_db = []
    all_cities = crud.get_cities()


    for n in range(1,100):
        print(n)
        email = f'user{n}@test.com'  # Voila! A unique email!
        password = 'test'
        username= f'user{n}'
        home_city = choice(all_cities)


        user = crud.create_user(email, password, username, home_city)
        users_in_db.append(user)

    db.session.commit()



def entry():

    all_users = crud.get_users()
    all_cities = crud.get_cities()

    for n in range(100):
        user = choice(all_users)
        blog = "hello world"
        city = choice(all_cities)

        entry = crud.create_entry(user, blog, city)
    db.session.commit()

def rating():

    all_users = crud.get_users()
    all_entries = crud.get_entries()

    for n in range(100):

        liker = choice(all_users)
        entry = choice(all_entries)

        crud.create_rating(liker, entry)
    db.session.commit()

def photo():

    all_users = crud.get_users()
    all_entries = crud.get_entries()
    all_cities = crud.get_cities()

    for n in range(100):

        user = choice(all_users)
        entry = choice(all_entries)
        photo_url = "www.somepath.com"
        city = choice(all_cities)

        photo = crud.create_photo(user, entry, photo_url, city)
    




# create_db()
model.connect_to_db(server.app)

# city()
# user()
# entry()
# rating()
photo()


    # __tablename__ = 'ratings'
    # rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # liker_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # # receiver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # entry_id = db.Column(db.Integer, db.ForeignKey('entries.entry_id'))
    # created_on = db.Column(db.DateTime, server_default=db.func.now())


