# Restaurant Menu from Udacity Full Stack Nanodegree

## Preparation

You can install the followings either locally or in virtual machines, such as
venv, vagrant, etc.

 * Python 2.7
 * Flask
 * sqlalchemy

## How to Run

 1. `python chinesemenus.py` This will help establishing a database
 2. `python finalProject.py` This will run the server at `localhost:5000`
 3. Open `localhost:5000` from your browser and you'll see the index page.

 ![index](https://i.loli.net/2017/09/08/59b2151e3169c.png)

## Develop process

![develop process](https://i.loli.net/2017/09/08/59b29cf4b390a.png)

1. Mock-ups(stucture & sketch)

 * structure

 ![structure](https://i.loli.net/2017/09/08/59b29d45169f4.png)

 * sketch

 1. index

  ![index](https://i.loli.net/2017/09/08/59b29dde1a69d.png)

 2. menu

  ![menu](https://i.loli.net/2017/09/08/59b29df2e1b69.png)

 3. add restaurant or menu item

  ![add](https://i.loli.net/2017/09/08/59b29e04b5d4d.png)

 4. edit restaurant or menu item

  ![edit](https://i.loli.net/2017/09/08/59b29e169ac3c.png)

 5. delete restaurant or menu item

  ![delete](https://i.loli.net/2017/09/08/59b29e271a487.png)

2. Routing

For instance:

```python
@app.route('/')
@app.route('/restaurants')
def allRestaurants():
    return 'Successfully opening index page!'
```

3. Templates & Forms

 * html & form
 * build fake data in backend based on data structure

4. CRUD Functionality

Establish database.

5. API Endpoints

Return json data to let other developers play with it.

6. Styling & Message Flashing

 * CSS
 * flash messages to better interact with users
