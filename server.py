"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)

from model import connect_to_db
import crud

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

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
    """Create a new user."""

    email = request.form.get('email')
    password_check = request.form.get('password')

    user = crud.get_user_by_email(email)

    if password_check != user.password:
        session['current_user'] = user.user_id
        flash('logged in!')
    else:
        flash('error')

    return redirect('/')

@app.route('/cities')
def all_cities():
    """View all movies."""

    cities = crud.get_cities()

    return render_template('all_cities.html', cities=cities)

@app.route("/map")
def view_basic_map():

    print("*" * 100)

    user_id = session['current_user']
    user_cities = crud.get_user_cities(user_id)
    # user_lat = user_cities[0].geo_lat
    # user_lng = user_cities[0].geo_lng

    # print(user_id)
    # print(user_cities)
    # print(user_lng)
    # print(user_lat)



    return render_template('map.html', 
                            user_cities=user_cities,
                            user_id=user_id
                            # ,user_lat=user_lat,
                            # user_lng=user_lng
                         )

@app.route("/map-json")
def map_json():

    print("*" * 100)

    user_id = session['current_user']
    user_cities = crud.get_user_cities(user_id)
   

    city_list = []

    for city in user_cities:
        city_list.append({'user_id':  session['current_user'],
                 'city_id': city.city_id,
                 'city_name': city.city_name,
                 'user_lat': city.geo_lat,
                 'user_lng': city.geo_lng})


    # city_dict = { 'user_id':  session['current_user'],
    #              'city_id': user_cities[0].city_id,
    #              'city_name': user_cities[0].city_name,
    #              'user_lat': user_cities[0].geo_lat,
    #              'user_lng': user_cities[0].geo_lng
    #                     }

    return jsonify(city_list)


    """Demo of basic map-related code.

    - Programmatically adding markers, info windows, and event handlers to a
      Google Map
    - Showing polylines, directions, etc.
    - Geolocation with HTML5 navigator.geolocate API
    """





@app.route('/users')
def all_users():

    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular movie."""

    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user)




@app.route('/entries')
def all_entries():

    entries = crud.get_entries()

    return render_template('all_entries.html', entries=entries)

@app.route('/entries/<entry_id>')
def show_entry(entry_id):

    entry = crud.get_entry_by_id(entry_id)
    return render_template('entry_details.html', entry=entry)


@app.route('/create-entry')
def register_entry():

    user = session['current_user']
    blog = "to be added"
    city_name= request.args.get('city_name')
    city= crud.get_city_by_name(city_name)

    if city_id:
        crud.create_entry(user, blog, city)
        flash('Entry created!')
    else:
        flash('Sorry We have not incorporated that city yet!')

    return redirect('/entries/<entry_id>')


if __name__ == '__main__':
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host='0.0.0.0', debug=True)
