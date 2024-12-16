from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from crud import view_restaurants, add_restaurant, update_restaurant, delete_restaurant

app = Flask(__name__)
#protect path and data base
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', "sqlite://" + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'restaurant_system.sqlite'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return view_restaurants()

@app.route('/add_restaurant', methods=['POST'])
def add():
    return add_restaurant()

@app.route('/update_restaurant', methods=['POST'])
def update():
    return update_restaurant()

@app.route('/delete_restaurant/<string:r_id>', methods=['GET', 'POST'])
def delete(r_id):
    return delete_restaurant(r_id)

@app.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        name = request.form['username']
        print(name)
        return redirect(url_for('welcome', username=name))
    
    return render_template('index.html')

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('home.html', username=username)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8080)

