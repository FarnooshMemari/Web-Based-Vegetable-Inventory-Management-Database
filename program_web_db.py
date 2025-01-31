from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Creates the SQLite database connection and cursor
def create_connection():
    """
    Creates a connection to the SQLite database and return the cursor object.
    """
    conn = sqlite3.connect('vegetable.db')
    c = conn.cursor()
    return conn, c

# Creates the vegetable table
def create_table():
    """
    Creates the vegetable table if it does not exist.
    """
    conn, c = create_connection()
    c.execute("CREATE TABLE IF NOT EXISTS vegetable (quantity INTEGER, name TEXT)")
    conn.commit() # Saves all the changes
    conn.close()

# Adds or updates a vegetable
def add_update_vegetable(name, quantity):
    """
    Adds a new vegetable or updates the quantity of an existing vegetable.
    Args:
        name (string): The name of the vegetable.
        quantity (integer): The quantity of the vegetable.
    """
    conn, c = create_connection()
    c.execute("SELECT * FROM vegetable WHERE name=?", (name,))
    found = c.fetchone() # Gets the first row from result
    if found:
        c.execute("UPDATE vegetable SET quantity=? WHERE name=?", (quantity, name))
    else:
        c.execute("INSERT INTO vegetable (quantity, name) VALUES (?, ?)", (quantity, name))
    conn.commit() # Saves all the changes
    conn.close()

# Shows all vegetables
def show_all_vegetables():
    """
    Retrieves all the vegetable entries from the database.
    Returns:
        list: list of tuples that represents all rows in the vegetable table.
    """
    conn, c = create_connection()
    c.execute("SELECT * FROM vegetable")
    rows = c.fetchall() # Gets all the rows
    conn.close()
    return rows

# Deletes a vegetable by name
def delete_vegetable(name):
    """
    Deletes a vegetable from the database by name.
    Args:
        name (string): The name of the vegetable to delete.
    """
    conn, c = create_connection()
    c.execute("DELETE FROM vegetable WHERE name=?", (name,))
    conn.commit() # Saves all the changes
    conn.close()

def search_vegetable(name):
    """
    Searches for a vegetable by name and return its quantity if it exists.
    Args:
        name (string): The name of the vegetable to search.
    Returns:
        integer or None: The quantity of the vegetable if found and None otherwise.
    """
    conn, c = create_connection()
    c.execute("SELECT quantity FROM vegetable WHERE name=?", (name,))
    row = c.fetchone() # Gets the first row from result
    conn.close()
    return row[0] if row else None

# Clears the table
def clear_table():
    """
    Deletes all the vegetable records from the database.
    """
    conn, c = create_connection()
    c.execute("DELETE FROM vegetable")
    conn.commit()
    conn.close()

# Home to show all vegetables and add/delete forms
@app.route('/', methods=['GET', 'POST'])
def index():
    search_message = None  # Initializes the search message

    if request.method == 'POST':
        # Adds/Updates submission
        if 'add_update' in request.form:
            name = request.form['name']
            quantity = request.form['quantity']
            if name and quantity.isdigit():
                add_update_vegetable(name, int(quantity))

        # Deletes submission
        elif 'delete' in request.form:
            name = request.form['name']
            delete_vegetable(name)

        # Searchs submission
        elif 'search' in request.form:
            search_name = request.form['search_name']
            search_result = search_vegetable(search_name)

            print(f"Search for: {search_name}, Result: {search_result}")

            if search_result is not None:
                search_message = f"{search_name} has a quantity of {search_result}."
            else:
                search_message = f"{search_name} not found in the database."

    # After any submission, renders the full page again
    vegetables = show_all_vegetables()

    return render_template('index.html', vegetables=vegetables, search_message=search_message)

# Clears all the table records
@app.route('/clear')
def clear():
    """
    Clears all vegetables from the database and redirect to the home page.
    """
    clear_table()
    return redirect(url_for('index'))

# Runs the application
if __name__ == '__main__':
    create_table()  # Ensures that the table is created when the app starts
    app.run(debug=True)