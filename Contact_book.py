import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json

def sort_contacts(column):
    # Check the current sorting order and toggle it
    if column_sort_states[column]:
        contact_data.sort(key=lambda x: x[column], reverse=True)
        column_sort_states[column] = False
    else:
        contact_data.sort(key=lambda x: x[column])
        column_sort_states[column] = True
    
    update_sort_indicator(column)
    display_contacts()

def update_sort_indicator(column):
    for col in columns:
        heading = contact_list.heading(col)
        if column == col:
            heading["text"] = f"{col} ▲" if column_sort_states[col] else f"{col} ▼"
        else:
            heading["text"] = col

def display_contacts(filtered=None):
    # Clear existing data
    for item in contact_list.get_children():
        contact_list.delete(item)

    # Display filtered or all contacts
    contacts = filtered if filtered else contact_data
    for contact in contacts:
        contact_list.insert('', 'end', values=(contact['Name'], contact['Phone'], contact['Email'], contact['Address']))

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    # Check for non-empty values for email and address
    if name and phone:
        contact_data.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
        clear_entries()
        save_contacts()
        display_contacts()
    else:
        messagebox.showwarning("Warning", "Please enter at least Name and Phone.")

def delete_contact():
    selected_contact = contact_list.selection()

    if selected_contact:
        confirm = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
        if confirm:
            contact_index = contact_list.index(selected_contact[0])
            contact_data.pop(contact_index)
            save_contacts()
            clear_entries()
            display_contacts()
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

def update_contact():
    selected_contact = contact_list.selection()

    if selected_contact:
        contact_index = contact_list.index(selected_contact[0])
        updated_contact = (
            name_entry.get(),
            phone_entry.get(),
            email_entry.get(),
            address_entry.get()
        )

        contact_data[contact_index] = {'Name': updated_contact[0], 'Phone': updated_contact[1],
                                       'Email': updated_contact[2], 'Address': updated_contact[3]}
        save_contacts()
        clear_entries()
        display_contacts()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contacts():
    search_query = simpledialog.askstring("Search Contacts", "Enter a name or keyword to search for:")
    if search_query:
        # Use lower() to make the search case-insensitive
        filtered_contacts = [contact for contact in contact_data if search_query.lower() in contact['Name'].lower()]
        display_contacts(filtered_contacts)

def show_about():
    about_text = "Contact Book App\nVersion 1.0\n\nCreated by 'Anmol Yaseen'\n© 2023"
    messagebox.showinfo("About", about_text)

def show_user_guide():
    user_guide_text = """
    Contact Book App User Guide

    1. Adding a Contact:
        - Enter the contact details (Name, Phone, Email, Address).
        - Click the 'Add Contact' button to save the contact.

    2. Updating a Contact:
        - Select a contact from the list.
        - Modify the contact details in the input fields.
        - Click the 'Update Contact' button to save the changes.

    3. Deleting a Contact:
        - Select a contact from the list.
        - Click the 'Delete Contact' button to remove the contact.

    4. Sorting Contacts:
        - Click on the column headers (Name, Phone, Email, Address) to sort contacts in ascending order.
        - Click again to sort in descending order.

    5. About:
        - Click the 'About' button to view information about the app.

    6. Load Contacts:
        - Click the 'Load Contacts' button to load previously saved contacts.
    """
    messagebox.showinfo("User Guide", user_guide_text)

def save_contacts():
    try:
        with open('contacts.json', 'w') as file:
            json.dump(contact_data, file)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving contacts: {e}")

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading contacts: {e}")
        return []

# Create the main application window
app = tk.Tk()
app.title("Contact Book")

# Create a custom ttk style for buttons and frames
style = ttk.Style()
style.configure("TButton", padding=10)
style.configure("TFrame", background="#E5E5E5")

# Create a top menu bar
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load Contacts", command=load_contacts)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="User Guide", command=show_user_guide)
help_menu.add_command(label="About", command=show_about)

input_frame = ttk.Frame(app, style="TFrame")
input_frame.pack(padx=10, pady=10, fill="both", expand=True)

name_label = ttk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, sticky="w")

name_entry = ttk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

phone_label = ttk.Label(input_frame, text="Phone:")
phone_label.grid(row=1, column=0, sticky="w")

phone_entry = ttk.Entry(input_frame)
phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

email_label = ttk.Label(input_frame, text="Email:")
email_label.grid(row=2, column=0, sticky="w")

email_entry = ttk.Entry(input_frame)
email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

address_label = ttk.Label(input_frame, text="Address:")
address_label.grid(row=3, column=0, sticky="w")

address_entry = ttk.Entry(input_frame)
address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

button_frame = ttk.Frame(app, style="TFrame")
button_frame.pack(padx=10, pady=5)

add_button = ttk.Button(button_frame, text="Add Contact", command=add_contact, style="TButton")
add_button.pack(side="left", padx=5)

update_button = ttk.Button(button_frame, text="Update Contact", command=update_contact, style="TButton")
update_button.pack(side="left", padx=5)

search_button = ttk.Button(button_frame, text="Search Contacts", command=search_contacts, style="TButton")
search_button.pack(side="left", padx=5)

delete_button = ttk.Button(button_frame, text="Delete Contact", command=delete_contact, style="TButton")
delete_button.pack(side="left", padx=5)

# Create buttons for sorting
sort_asc_button = ttk.Button(button_frame, text="Sort Ascending", command=lambda: sort_contacts(sort_column))
sort_desc_button = ttk.Button(button_frame, text="Sort Descending", command=lambda: sort_contacts(sort_column))

# Pack the sort buttons
sort_asc_button.pack(side="left", padx=5)
sort_desc_button.pack(side="left", padx=5)

# Initially, set the sort column to 'Name'
sort_column = 'Name'

tree_frame = ttk.Frame(app, style="TFrame")
tree_frame.pack(padx=10, pady=10, fill="both", expand=True)

columns = ('Name', 'Phone', 'Email', 'Address')
contact_list = ttk.Treeview(tree_frame, columns=columns, show='headings')

for col in columns:
    contact_list.heading(col, text=col, command=lambda c=col: sort_contacts(c))
    contact_list.column(col, width=150)  # Adjust the column width as needed

vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=contact_list.yview)
vsb.pack(side="right", fill="y")

hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=contact_list.xview)
hsb.pack(side="bottom", fill="x")

contact_list.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
contact_list.pack(fill="both", expand=True)

# Load contact data and display
contact_data = load_contacts()
column_sort_states = {column: False for column in columns}
display_contacts()

# Start the main application loop
app.mainloop()
