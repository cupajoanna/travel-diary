from model import db, User, Entry, Rating, City, Photo, connect_to_db


def create_user(email, password, username, city):
    """Create and return a new user."""

    user = User(email=email, password=password, username=username, city=city)

    db.session.add(user)


    return user

def get_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_cities(user_id):
    return db.session.query(City).join(Entry.city).filter(Entry.user_id == user_id).all()


def create_city(city_name, country_name, geo_lat, geo_lng):
    """Create and return a new movie."""

    city = City( 
                city_name= city_name, 
                country_name = country_name, 
                geo_lat = geo_lat,
                geo_lng = geo_lng)

    print(city)

    db.session.add(city)


    return city

def get_cities():
    """Return all movies."""

    return City.query.all()

def get_city_by_id(city_id):
    return City.query.get(city_id)

def get_city_by_name(city_name):
    return City.query.filter(city_name == city_name).first()


def create_entry(user, blog, city):
    """Create and return a new movie."""

    entry = Entry( 
                user= user, 
                blog = blog, 
                city=city)

    db.session.add(entry)


    return entry

def get_entries():

    return Entry.query.all()


def get_entry_by_id(entry_id):
    return Entry.query.get(entry_id)


def create_rating(liker, entry):
    """Create and return a new rating."""

    rating = Rating(liker=liker, entry=entry)

    db.session.add(rating)


    return rating


def create_photo(user, entry, photo_url, city):
    """Create and return a new rating."""

    photo = Photo(user=user, entry=entry, photo_url=photo_url, city=city)

    db.session.add(photo)
    db.session.commit()


    return photo




if __name__ == '__main__':
    from server import app
    connect_to_db(app)