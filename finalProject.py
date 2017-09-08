from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from database_orm import session
from database_setup import Restaurant, MenuItem

from sqlalchemy import distinct

courses = ['Entree', 'Appetizer', 'Dessert', 'Beverage']

@app.route('/')
@app.route('/restaurants')
def allRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('allrestaurants.html', restaurants = restaurants)

@app.route('/restaurants/add', methods=['GET', 'POST'])
def addRestaurant():
    if request.method == 'POST':
        if request.form['name']:
            newRestaurant = Restaurant(name = request.form['name'])
            session.add(newRestaurant)
            session.commit()
            flash('New restaurant added!')
            return redirect(url_for('allRestaurants'))
        else:
            return 'empty value.'
    else:
        return render_template('addrestaurant.html')

@app.route('/restaurants/<restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
            session.add(editedRestaurant)
            session.commit()
            flash('Restaurant has been renamed!')
            return redirect(url_for('allRestaurants'))
        else:
            return 'empty value.'
    else:
        return render_template('editrestaurant.html', restaurant = editedRestaurant)

@app.route('/restaurants/<restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    toBeDeleted = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        session.delete(toBeDeleted)
        session.commit()
        flash('Restaurant has been deleted!')
        return redirect(url_for('allRestaurants'))
    else:
        return render_template('deleterestaurant.html', restaurant = toBeDeleted)

@app.route('/restaurants/<restaurant_id>/menu')
def menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    if not items:
        flash('No item in this restaurant. Add one?')
    return render_template('menu.html', restaurant = restaurant, items = items)

@app.route('/restaurants/<restaurant_id>/menu/add', methods=['GET', 'POST'])
def addMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        if request.form['name'] and request.form['price'] and \
        request.form['course'] and request.form['description']:
            newItem = MenuItem(name = request.form['name'],\
                               price = request.form['price'],\
                               course = request.form['course'],\
                               description = request.form['description'],
                               restaurant_id = restaurant_id)
            session.add(newItem)
            session.commit()
            flash('A new item has been added!')
            return redirect(url_for('menu', restaurant_id = restaurant_id))
        else:
            return 'empty value.'
    else:
        # courses = session.query(distinct(MenuItem.course)).filter_by(restaurant_id = restaurant_id).all()
        return render_template('addmenuitem.html', restaurant = restaurant, courses = courses)

@app.route('/restaurants/<restaurant_id>/menu/<menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['name'] and request.form['price'] and \
        request.form['course'] and request.form['description']:
            editedItem.name = request.form['name']
            editedItem.price = request.form['price']
            editedItem.course = request.form['course']
            editedItem.description = request.form['description']
            session.add(editedItem)
            session.commit()
            flash('The item has been updated!')
            return redirect(url_for('menu', restaurant_id = restaurant_id))
        else:
            return 'empty value.'
    else:
        return render_template('editmenuitem.html', restaurant = restaurant, menu = editedItem, courses = courses)

@app.route('/restaurants/<restaurant_id>/menu/<menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    toBeDeleted = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        session.delete(toBeDeleted)
        session.commit()
        flash('The item has been deleted!')
        return redirect(url_for('menu', restaurant_id = restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant = restaurant, item = toBeDeleted)

# APIs
@app.route('/restaurants/JSON')
def allRestaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[i.serialize for i in restaurants])

@app.route('/restaurants/<restaurant_id>/menu/JSON')
def allMenuJSON(restaurant_id):
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return jsonify(Menu=[i.serialize for i in items])

@app.route('/restaurants/<restaurant_id>/menu/<menu_id>/JSON')
def itemInfoJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(restaurant_id = restaurant_id, id = menu_id).one()
    return jsonify(Item=item.serialize)

if __name__ == '__main__':
    app.secret_key = 'superdevkey'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
