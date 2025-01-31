# **Web-Based SQLite Vegetable Inventory Management System**

This project is a **web-based inventory management system** built using **Flask** and **SQLite**. It allows users to **add, update, retrieve, delete, search, and clear vegetable inventory data** through a **web interface**. The application enables seamless interaction with the database via **HTML forms**, providing a **simple yet effective** CRUD (Create, Read, Update, Delete) functionality.

---

## **Features**
- 🌐 **Web-Based Application**: Developed using **Flask** for easy accessibility through a browser.
- 🗃 **SQLite Database Integration**: Stores vegetable names and their quantities.
- ✅ **CRUD Operations**:
  - **Create**: Add new vegetables and their quantities.
  - **Read**: Retrieve the quantity of a specific vegetable.
  - **Update**: Modify the quantity of an existing vegetable.
  - **Delete**: Remove vegetables from the database.
- 🔎 **Search Functionality**: Users can search for a specific vegetable by name.
- ❌ **Clear Database**: Allows users to delete all stored records with a single click.
- 🔒 **SQL Injection Prevention**: Uses **parameterized queries** to ensure safe database interactions.

---

## **How It Works**
1. **User accesses the web interface** via `http://127.0.0.1:5000/`.
2. **Inputs a vegetable name and quantity** to add or update in the database.
3. **Performs actions** through the web interface:
   - **Add/Update**: Saves or updates the vegetable quantity.
   - **Search**: Finds and displays a vegetable's quantity.
   - **Delete**: Removes a vegetable from the database.
   - **Show All**: Lists all stored vegetables and their quantities.
   - **Clear All**: Deletes all records from the database.
4. **Updated results** are displayed in the web interface.

---
