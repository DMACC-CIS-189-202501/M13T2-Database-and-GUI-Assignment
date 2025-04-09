# TODO 1: Delete this line and put your docstring here

###
# NOTE: This assignment will not have an autograder
###


import cis189_database as db
import tkinter


# ------------------------ Start Function Defs Here

conn = None

def create_connection():
    global conn
    if conn == None:
        conn = db.create_connection("pythonsqlite.db")
    return conn

def initialize_tables():
    db.create_tables("pythonsqlite.db")

def get_person_first_name():
    user_input = fn_entry.get()
    return user_input

def get_person_last_name():
    user_input = ln_entry.get()
    return user_input

def insert_person():
    fn = get_person_first_name()
    ln = get_person_last_name()
    if fn not in [None, ""] and ln not in [None, ""]:
        person = (fn, ln)
        conn = create_connection()
        person_id = db.create_person(conn, person)
        person_insert_status_label.config(text=f"Updated Person with: {ln}, {fn} with an ID of {person_id}")
    else:
        person_insert_status_label.config(text=f"Error: First Name and/or Last name cannot be blank")

def view_person_table():
    conn = create_connection()
    with conn:  
        rows = db.select_all_persons(conn)
    table = ""
    #clear old view
    person_table_view.delete('1.0', tkinter.END)
    for row in rows:
        table = table + str(row) + "\n"
    person_table_view.insert(tkinter.END, table)

# TODO 4: Create a function that adds a Student based on the input fields

# TODO 6: Create a function that displays all student data

# ------------------------------- End Function Defs



# Ideally this would be main_gui_window = tkinter.Tk(), but that is a lot to type over and over;
# so we will use 'm'
m = tkinter.Tk()

create_tables_button = tkinter.Button(m, text="Initialize Tables", command=initialize_tables)
create_tables_button.grid(row=2)


person_section_label = tkinter.Label(m, text="--- Person Entry Section ---")
person_section_label.grid(row=6)
# Create a Field for First Name
fn_label = tkinter.Label(m, text="Enter a First Name")
fn_label.grid(row=7)
fn_entry = tkinter.Entry(m)
fn_entry.grid(row=8)
ln_label = tkinter.Label(m, text="Enter a Last Name")
ln_label.grid(row=9)
ln_entry = tkinter.Entry(m)
ln_entry.grid(row=10)
create_person_button = tkinter.Button(m, text="Create/Insert Person", command=insert_person)
create_person_button.grid(row=11)
person_insert_status_label = tkinter.Label(m, text="")
person_insert_status_label.grid(row=12)
person_table_label = tkinter.Label(m, text="Person Table")
person_table_label.grid(row=13)
person_table_view = tkinter.Text(m, height=30, width=50)
person_table_view.grid(row=14)
view_person_table_button = tkinter.Button(m, text="View Person Table", command=view_person_table)
view_person_table_button.grid(row=15)

student_section_label = tkinter.Label(m, text="--- Student Entry Section ---")
student_section_label.grid(row=25)
# TODO 2: Add inputs for a firstname, lastname, major, and startdate(text/string) for a student

# TODO 3: Add an "Add Student" button; create a command/function associated with it and place that up top/TODO 4
# Add a label under it to display what was inserted

# TODO 5: Add a text field to display student data

# TODO 7: Add an exit button

m.mainloop()