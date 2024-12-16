from flask import request, redirect, url_for, flash, render_template
from models import db, Restaurant

# view restaurants
def view_restaurants():    
    restaurants = Restaurant.query.all()
    return render_template('index.html', restaurants=restaurants)

# insert restaurants
def add_restaurant():
    if request.method == 'POST':
        r_id = request.form['r_id']
        r_name = request.form['r_name']
        a_id = request.form['a_id']

        new_restaurant = Restaurant(r_id=r_id, r_name=r_name, a_id=a_id)
        db.session.add(new_restaurant)
        db.session.commit()

        flash("Restaurant inserted successfully")
        return redirect(url_for('index'))

# update restaurants
def update_restaurant():
    if request.method == 'POST':
        r_id = request.form['r_id']
        restaurant = Restaurant.query.get(r_id)

        if restaurant:
            restaurant.r_name = request.form['r_name']
            restaurant.a_id = request.form['a_id']
            db.session.commit()
            flash("Restaurant updated successfully")
        else:
            flash("Restaurant not found")

        return redirect(url_for('index'))

# delete restaurants
def delete_restaurant(r_id):
    restaurant = Restaurant.query.get(r_id)

    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        flash("Restaurant deleted successfully")
    else:
        flash("Restaurant not found")

    return redirect(url_for('index'))


