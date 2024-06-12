import sqlite3

conn = sqlite3.connect('ice_cream.db')
cursor = conn.cursor()

# Functions for adding data
def add_seasonal_flavor(name, season):
    cursor.execute('INSERT INTO seasonal_flavors (name, season) VALUES (?, ?)', (name, season))
    conn.commit()

def add_ingredient(name, stock):
    cursor.execute('INSERT INTO ingredient_inventory (name, stock) VALUES (?, ?)', (name, stock))
    conn.commit()

def add_customer_suggestion(flavor, allergens):
    cursor.execute('INSERT INTO customer_suggestions (flavor, allergens) VALUES (?, ?)', (flavor, allergens))
    conn.commit()

def add_allergen(name):
    cursor.execute('INSERT INTO allergens (name) VALUES (?)', (name,))
    conn.commit()

def add_to_cart(flavor_id):
    cursor.execute('INSERT INTO user_cart (flavor_id) VALUES (?)', (flavor_id,))
    conn.commit()

# Functions for fetching data
def get_seasonal_flavors():
    cursor.execute('SELECT * FROM seasonal_flavors')
    return cursor.fetchall()

def get_ingredients():
    cursor.execute('SELECT * FROM ingredient_inventory')
    return cursor.fetchall()

def get_customer_suggestions():
    cursor.execute('SELECT * FROM customer_suggestions')
    return cursor.fetchall()

def get_allergens():
    cursor.execute('SELECT * FROM allergens')
    return cursor.fetchall()

def get_user_cart():
    cursor.execute('SELECT sf.name FROM user_cart AS uc INNER JOIN seasonal_flavors AS sf ON uc.flavor_id = sf.id')
    return cursor.fetchall()

# Close connection
def close_connection():
    conn.close()
 
