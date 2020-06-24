import os
from datetime import datetime
import json 
from random import choice, randint
import crud
import model
import server




# def create_db():
#     os.system('dropdb travel-diary')
#     os.system('createdb travel-diary')
#     model.db.create_all()


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

    model.db.session.commit()


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

    model.db.session.commit()



def entry():

    all_users = crud.get_users()
    all_cities = crud.get_cities()

    for n in range(100):
        user = choice(all_users)
        blog = "entry to be updated"
        title = "title to be updated"
        city = choice(all_cities)

        entry = crud.create_entry(user, blog, city, title)
    model.db.session.commit()

def rating():

    all_users = crud.get_users()
    all_entries = crud.get_entries()

    for n in range(100):

        liker = choice(all_users)
        entry = choice(all_entries)

        crud.create_rating(liker, entry)
    model.db.session.commit()

# def photo():

#     all_users = crud.get_users()
#     all_entries = crud.get_entries()
#     all_cities = crud.get_cities()

#     for n in range(100):

#         user = choice(all_users)
#         entry = choice(all_entries)
#         photo_url = "www.somepath.com"
#         city = choice(all_cities)

#         photo = crud.create_photo(user, entry, photo_url, city)
#     model.db.session.commit()
    




# create_db()
model.connect_to_db(server.app)

city()
user()
entry()
rating()
# photo()



