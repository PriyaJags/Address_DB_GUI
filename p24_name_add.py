import tkinter as tk
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
        database="db",
        user="user",
        password="userpassword",
        host="host",
        port="1234"
        )
cur = conn.cursor()

# function to save name and address in database
def add_to_database():
    name = name_entry.get()  # Get text(name) from the Entry widget
    address = address_entry.get("1.0", "end-1c")  # Get text(address) from the Entry widget
    # checking for valid name entries
    if not name.replace(" ", "").isalpha():
        status_label.config(text="Invalid characters in name. Only letters and spaces allowed.")
        return
    # checking for valid address entries
    if not all(c.isalnum() or c in " ,-\n" for c in address.replace(" ", "")):
        status_label.config(
            text="Invalid characters in address. Only letters, numbers, spaces, commas, and hyphens allowed.")
        return

    # Insert the name and address into the customer database
    insert_query = "INSERT INTO customer (name, address) VALUES (%s, %s)"
    cur.execute(insert_query, (name, address))
    conn.commit()
    status_label.config(text="Name and address added to the database")

# function to retrieve address from database corresponding to the name provided
def retrieve_address():
    name = search_entry.get()  # enter name for which corresponding address from db would be fetched
    # checking for valid name entries which allows only letters and spaces
    if not name.replace(" ", "").isalpha():
        address_label.config(text="Invalid characters in name. Only letters and spaces allowed.")
        return
    # Retrieve address based on the given name
    select_query = "SELECT address FROM customer WHERE name = %s"
    cur.execute(select_query, (name,))
    results = cur.fetchall()  # fetching all addresses from db corresponding to the name provided
    if results:
        addresses = "\n".join([f"- {result[0]}" for result in results])
        address_label.config(text=f"Address for {name}:\n{addresses}")
    else:
        address_label.config(text="Address not found for this name")

# Tkinter GUI setup for adding name and address


add_window = tk.Tk()
add_window.title("Address Collection Form")
add_window.geometry("600x250")  # Set window size

name_label = tk.Label(add_window, text="Enter Name:",font=("Arial", 12))
name_label.pack()
name_entry = tk.Entry(add_window,font=("Arial", 12), width=20)
name_entry.pack()
address_label = tk.Label(add_window, text="Enter Address:",font=("Arial", 12))
address_label.pack()
address_entry = tk.Text(add_window, font=("Arial", 12), width=40, height=4)  # Multi-line Text widget for address
address_entry.pack()
add_button = tk.Button(add_window, text="Save", command=add_to_database,font=("Arial", 15),width = 10,height=2)
add_button.pack()
status_label = tk.Label(add_window, text="",font=("Arial", 12))
status_label.pack()

# Tkinter GUI setup for retrieving address based on name
retrieve_window = tk.Tk()
retrieve_window.title("Address Retrieval")
retrieve_window.geometry("600x250")
search_label = tk.Label(retrieve_window, text="Enter Name to Search:",font=("Arial", 12))
search_label.pack()
search_entry = tk.Entry(retrieve_window,font=("Arial", 12))
search_entry.pack()
search_button = tk.Button(retrieve_window, text="Search", command=retrieve_address,font=("Arial", 12),width=10,height=2)
search_button.pack()
address_label = tk.Label(retrieve_window, text="",font=("Arial", 12))
address_label.pack()

# Calculate screen width and height
screen_width = add_window.winfo_screenwidth()
print("screen_width :",screen_width)
screen_height = add_window.winfo_screenheight()
print("screen_height :",screen_height)

# Position windows side by side at the center
add_window.geometry(f"600x250+{int((screen_width - 1200) / 2)}+{int((screen_height - 250) / 2)}")
retrieve_window.geometry(f"600x250+{int((screen_width + 10) / 2)}+{int((screen_height - 250) / 2)}")

add_window.mainloop()