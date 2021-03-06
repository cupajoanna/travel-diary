from model import db, User, Entry, Rating, City, Photo, Profile, connect_to_db

"""User functions"""

def create_user(email, password, username, city):

    user = User(email=email, password=password, username=username, city=city)

    db.session.add(user)
    db.session.commit()


    return user


def get_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_profile(user_id):
    return db.session.query(Profile).filter(Profile.user_id == user_id).first()


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def update_user(user, email, password, username, city):

    update_this = User.query.get(user.user_id)
    print(update_this)

    if email:
        update_this.email = email

    if password:
        update_this.password= password

    if username:
        update_this.username = username

    if city:
        update_this.city = city

    db.session.commit()

    return update_this





def create_profile(user, description, instagram, twitter, website, profile_photo ="https://picsum.photos/500/350?nocache"):
 
    profile = Profile(user=user, description=description, instagram=instagram, twitter=twitter, website=website, profile_photo=profile_photo)

    db.session.add(profile)
    db.session.commit()
    return profile


def update_profile(user, profile_photo, description, instagram, twitter, website):

    update_this = Profile.query.filter(Profile.user_id == user.user_id).first()
    print(update_this)

    if profile_photo:
        update_this.profile_photo = profile_photo

    if description:
        update_this.description= description

    if instagram:
        update_this.instagram = instagram

    if twitter:
        update_this.twitter = twitter

    if website:
        update_this.website = website


    db.session.commit()

    return update_this
    

"""City functions"""

def get_user_cities(user_id):
    return db.session.query(City).join(Entry.city).filter(Entry.user_id == user_id).all()

def get_user_entries(user_id):
    return db.session.query(Entry).join(Entry.city).filter(Entry.user_id == user_id).all()

def get_city_entries_ordered_by_ratings_count(city_id):
    return db.session.query(Entry, db.func.count(
        Rating.rating_id)).outerjoin(
            Rating).filter(Entry.city_id == city_id).group_by(
                    Entry.entry_id).order_by(db.func.count(
                            Rating.rating_id)).all()

def get_user_entries_ordered_by_ratings_count(user_id):
    return db.session.query(Entry, db.func.count(
        Rating.rating_id)).outerjoin(
            Rating).filter(Entry.user_id == user_id).group_by(
                    Entry.entry_id).order_by(db.func.count(
                            Rating.rating_id)).all()


def create_city(city_name, country_name, geo_lat, geo_lng):

    city = City( 
                city_name= city_name, 
                country_name = country_name, 
                geo_lat = geo_lat,
                geo_lng = geo_lng)

    print(city)

    db.session.add(city)
    db.session.commit()


    return city

def get_cities():

    return City.query.all()


def search_cities(term):

    return City.query.filter(City.city_name.like(f'%{term}%')).all()


def search_username(term):

    print(User.query.filter(User.username == term).all())
    return User.query.filter(User.username == term).all()
    


def search_email(term):

    print(User.query.filter(User.email == term).all())
    return User.query.filter(User.email == term).all()



def get_city_by_id(city_id):
    return City.query.get(city_id)

def get_city_by_name(city_name):

    print("*" * 100)
    print(city_name)
    return City.query.filter(City.city_name == city_name).first()

"""Entry Functions"""


def create_entry(user, blog, city, title):


    entry = Entry( 
                user= user, 
                blog = blog, 
                city=city,
                title=title)

    db.session.add(entry)
    db.session.commit()

    return entry

def get_entries():

    return Entry.query.all()

def get_all_entries_ordered_by_ratings_count():
    return db.session.query(Entry, db.func.count(
        Rating.rating_id)).outerjoin(
            Rating).group_by(Entry.entry_id).order_by(db.func.count(
                            Rating.rating_id)).all()




def get_entry_by_id(entry_id):
    return Entry.query.get(entry_id)


def get_entry_by_city(city_id):

    return Entry.query.filter(Entry.city_id == city_id).first()

def get_all_entries_by_city(city_id):

    return Entry.query.filter(Entry.city_id == city_id).all()


def update_entry(new_entry, new_title, entry_id):

    update_this = Entry.query.get(entry_id)
    print(update_this)

    if new_entry:

        update_this.blog = new_entry

    if new_title:
        update_this.title = new_title

    db.session.commit()

    return update_this
    

def get_city_by_entry(entry_id):
    return db.session.query(City).join(Entry.city).filter(Entry.entry_id == entry_id).first()

def get_user_by_entry(entry_id):
    return db.session.query(User).join(Entry.user).filter(Entry.entry_id == entry_id).first()


    

"""Rating Functions"""


def create_rating(liker, entry):

    rating = Rating(liker=liker, entry=entry)

    db.session.add(rating)
    db.session.commit()


    return rating

def get_rating_by_rating_id(rating_id):

    return Rating.query.filter(Rating.rating_id == rating_id).first()


def get_entry_ratings(entry_id):
    return Rating.query.filter(Rating.entry_id == entry_id).all()


"""Photo Functions"""



def create_photo(user, entry, photo_url, city):
 
    photo = Photo(user=user, entry=entry, photo_url=photo_url, city=city)

    db.session.add(photo)
    db.session.commit()
    return photo


def delete_photo(photo_id):

   Photo.query.filter(Photo.photo_id == photo_id).delete()

   db.session.commit()


def get_photo_by_entry(entry_id):
    return db.session.query(Photo).filter(Photo.entry_id == entry_id).all()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)