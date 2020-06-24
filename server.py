"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
import os
from pprint import pformat

from model import connect_to_db
import crud

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension

import cloudinary 
import cloudinary.uploader


app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# API_KEY = os.environ.get("CLOUDINARY_API_KEY")

cloudinary.config.update = ({
    'cloud_name':os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'api_key': os.environ.get('CLOUDINARY_API_KEY'),
    'api_secret': os.environ.get('CLOUDINARY_API_SECRET')
})


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')
    city_name = request.form.get('home_city')

    city = crud.get_city_by_name(city_name)
 

    user = crud.get_user_by_email(email)

    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password, username, city)
        flash('Account created! Please log in.')

    return redirect('/')

    
@app.route('/login', methods=['POST'])
def login():

    email = request.form.get('email')
    password_check = request.form.get('password')

    user = crud.get_user_by_email(email)

    if password_check == user.password:
        session['current_user'] = user.user_id
        flash('logged in!')
    else:
        flash('error')

    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():

    # session['current_user'] = None
    session.clear()
    flash('logged out!')

    return redirect('/')

"""Cities"""



@app.route('/cities')
def all_cities():
    """View all movies."""

    # user_id = session['current_user']
    cities = crud.get_cities()

    return render_template('all_cities.html', cities=cities)

@app.route("/map")
def view_map():

    user_id = session['current_user']
    user_cities = crud.get_user_cities(user_id)



    return render_template('map.html', 
                            user_cities=user_cities,
                            user_id=user_id

                         )

@app.route("/map-json")

def map_json():


    user_id = session['current_user']
    user_cities = crud.get_user_cities(user_id)
   

    city_list = []

    for city in user_cities:
        city_list.append({'user_id':  session['current_user'],
                 'city_id': city.city_id,
                 'city_name': city.city_name,
                 'user_lat': city.geo_lat,
                 'user_lng': city.geo_lng})

    return jsonify(city_list)


"""Users"""


@app.route('/users')
def all_users():

    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular movie."""

    user = crud.get_user_by_id(user_id)
    cities = crud.get_user_cities(user_id)
    return render_template('user_details.html', user=user, cities=cities)

"""Entries"""

@app.route('/entries')
def all_entries():

    entries = crud.get_entries()

    return render_template('all_entries.html', entries=entries)

@app.route('/entries/view_only/<entry_id>')
def view_only_entry(entry_id):

    if session.get('current_user'):

        entry = crud.get_entry_by_id(entry_id)
        city_id = entry.city_id

        city = crud.get_city_by_id(city_id)

        ratings = crud.get_entry_ratings(entry_id)

        total_ratings = 0

        for rating in ratings: 
            total_ratings += 1


        photo = crud.get_photo_by_entry(entry_id)
        # print("&"*100)
        # print(entry.title)

        return render_template('see_entry_only.html', entry=entry, city=city, photo = photo, total_ratings = total_ratings)


@app.route('/your_entries')
def your_entries():

    user_id = session['current_user']
    entries = crud.get_user_entries(user_id)

    return render_template('your_entries.html', entries=entries)



    # if session.get('current_user'):

    #     entries = crud.get_entries()

    # return redirect('/')

@app.route('/entries/<entry_id>')
def show_entry(entry_id):

    if session.get('current_user'):

        entry = crud.get_entry_by_id(entry_id)
        city_id = entry.city_id

        city = crud.get_city_by_id(city_id)

        print("*" * 50)
        print(entry)
        print(city)

        photo = crud.get_photo_by_entry(entry_id)

        ratings = crud.get_entry_ratings(entry_id)

        created_at_raw = entry.created_at

        created_at = str(created_at_raw)[0:10]

        total_ratings = 0

        for rating in ratings: 
            total_ratings += 1


        # print("&"*100)
        # print(entry.title)

        return render_template('entry_details.html', entry=entry, city=city, photo = photo, total_ratings = total_ratings, created_at = created_at)
    # return redirect('/')




@app.route('/create-entry/<city_name>')
def register_entry(city_name):

    user_id = session['current_user']
    user = crud.get_user_by_id(user_id)

    title = "title to be added"

    blog = "to be added"
    # city_name= request.args.get('city_name')
    city= crud.get_city_by_name(city_name)


    entry = crud.create_entry(user, blog, city, title)
    flash('Entry created!')

    # if city:
    #     entry = crud.create_entry(user, blog, city)
    #     flash('Entry created!')

    # else:
    #     flash('Sorry We have not incorporated that city yet!')

    return redirect('/entries/{}'.format(entry.entry_id))


@app.route('/route-to-entry/<city_id>')
def route_to_entry(city_id):

    if session.get('current_user'):

        city = crud.get_city_by_id(city_id)
        entry = crud.get_entry_by_city(city_id)
        entry_id = entry.entry_id

        print("*" * 50)
        print(entry)
        print(city_id)
        print(city)

        photo = crud.get_photo_by_entry(entry_id)

        ratings = crud.get_entry_ratings(entry_id)

        total_ratings = 0

        for rating in ratings: 
            total_ratings += 1


    return redirect('/entries/{}'.format(entry.entry_id))

    # return render_template('entry_details.html', entry=entry, city=city, photo = photo)




@app.route('/entries/<entry_id>/update', methods=['POST'])
def update_blog(entry_id):


    
    new_title = request.form.get('blog_title')

    new_entry = request.form.get('blog_entry')

    image_uploaded = request.files.get('image_upload')

    if image_uploaded:
        response = cloudinary.uploader.upload(image_uploaded)
        returned_url = response['url']


    city = crud.get_city_by_entry(entry_id)
    user = crud.get_user_by_entry(entry_id)

    ratings = crud.get_entry_ratings(entry_id)

    total_ratings = 0

    for rating in ratings: 
        total_ratings += 1


    crud.update_entry(new_entry, new_title, entry_id)
    flash('blog updated')
    entry = crud.get_entry_by_id(entry_id)

    if image_uploaded:
        photo = crud.create_photo(user, entry, returned_url, city)
        flash('photo created')


    return redirect('/entries/{}'.format(entry_id))


@app.route('/delete-photo', methods=['POST'])

def delete_photo():

    
    selected_photo_id= request.form.get("photo_id")

    crud.delete_photo(selected_photo_id)


    return "photo deleted"


@app.route('/entries/<entry_id>/like-entry', methods=['POST'])

def like_entry(entry_id):

    user_id = session['current_user']
    user = crud.get_user_by_id(user_id)

    # selected_rating_id = request.form.get("rating_id")

    # rating = crud.get_rating_by_rating_id(selected_rating_id)

    entry = crud.get_entry_by_id(entry_id)


    # selected_rating_id= request.form.get("rating_id")

    # num_likes= request.form.get("likes-counter")

    rating = crud.create_rating(user, entry)
    print(rating)
    print("@" * 100)

    ratings = crud.get_entry_ratings(entry_id)

    total_ratings = 0

    for rating in ratings: 
        total_ratings += 1


    return str(total_ratings)


    # entry_list = []

    # for entry in user_entries:
    #     entry_list.append({'user_id':  session['current_user'],
    #              'city_id': entry.city_id,
    #              'title': entry.title,
    #              'blog': entry.blog})

    # return jsonify(entry_list)


    # entries = crud.get_entries()


if __name__ == '__main__':
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host='0.0.0.0', debug=True)
