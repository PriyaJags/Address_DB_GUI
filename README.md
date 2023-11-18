# Address_DB_GUI
GUI-based system for managing an address book, which includes storing and retrieving data.

## Features
This project aims to provide a user-friendly interface for storing names and addresses into a database and 
retrieving corresponding address for the name provided. It consists of two graphical user interfaces (GUIs) for separate functionalities.

### Address Storage GUI
- Allows users to input and store name and address information into the connected database.
- Validates input fields for name and address.Names can only be alphabetic with spaces allowed.
- Address fields can be alphanumeric with few other keys.
- Provides feedback on successful name and address storage.

### Data Retrieval GUI
- Enables users to search and retrieve all stored addresses for the given name.
- Displays retrieved data in a user-friendly format within the interface.

## Technologies Used
- Programming Language:Python, Tkinter
- Database: Postgres

## Requirements to run the script:
1) An IDE that supports python.
2) Tkinter package
3) psycopg2 -- a python driver for postgreSQL
4) Postgres server


## To execute the file:
1) Copy the script in any python IDE.
2) Create Database named customer with columns 'name' and 'address'.
3) Set up Postgres connection by editing lines from 5-10. 
4) Run the code

