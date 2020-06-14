
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Replace this with your code!


def connect_to_db(flask_app, db_uri='postgresql:///travel-diary', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    home_city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))


    city = db.relationship('City', backref='users')

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username} email={self.email} home_city_id={self.home_city_id} created_at={self.created_at}>'


class Rating(db.Model):
    """A rating."""

    __tablename__ = 'ratings'
    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    liker_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # receiver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    entry_id = db.Column(db.Integer, db.ForeignKey('entries.entry_id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())


    entry = db.relationship('Entry', backref='ratings')
    liker = db.relationship('User', foreign_keys=[liker_id],  backref='ratings')
    # receiver = db.relationship('User', foreign_keys=[receiver_id], backref='ratings')

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} liker_id={self.liker_id} entry_id={self.entry_id} created_at={self.created_at}>'


class Entry(db.Model):
    """An entry."""

    __tablename__ = 'entries'

    entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))
    # title_name = db.Column(db.Text)
    blog = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


    user = db.relationship('User', backref='entries')
    city = db.relationship('City', backref='entries')
    # photos = db.relationship('Photo')

    def __repr__(self):
        return f'<Entry entry_id={self.entry_id} city_id={self.city_id} user_id={self.user_id} created_at={self.created_at}>'


class City(db.Model):
    """A city."""

    __tablename__ = 'cities'

    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_name = db.Column(db.String)
    country_name = db.Column(db.String)
    geo_lat = db.Column(db.Integer)
    geo_lng = db.Column(db.Integer)



    def __repr__(self):
        return f'<City city_id={self.city_id} city_name={self.city_name}>'

class Photo(db.Model):
    """A photo."""

    __tablename__ = 'photos'

    photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    entry_id = db.Column(db.Integer, db.ForeignKey('entries.entry_id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    photo_url = db.Column(db.String)

    user = db.relationship('User', backref='photos')
    city = db.relationship('City', backref='photos')
    entry = db.relationship('Entry', backref='photos')

    def __repr__(self):
        return f'<Photo photo_id={self.photo_id} entry_id={self.entry_id} city_id={self.city_id} user_id={self.user_id} created_at={self.created_at}>'




if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
