# Contact Book Application

This Contact Book application is a simple yet effective GUI tool built using Tkinter in Python. It allows users to add, update, delete, and search contacts. Each contact consists of a name, phone number, email, and address. This README provides instructions on how to run and use the application.

## Features

- Add new contacts with name, phone, email, and address
- Update existing contacts
- Delete contacts
- Search for contacts by name
- Sort contacts by name, phone, email, or address
- Save contacts to a file
- Load contacts from a file

## Requirements

Before running the application, ensure you have Python installed on your system. This application has been tested with Python 3.8 and above.

## How to Run

1. Save the script to a file named `contact_book.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `contact_book.py` is saved.
4. Run the script with the command: `python contact_book.py`.

## Using the Application

### Main Interface

The main interface consists of input fields for the contact's details (Name, Phone, Email, Address), a list displaying all the contacts, and several buttons for different operations.

### Adding a Contact

1. Enter the contact's details in the corresponding fields.
2. Click the 'Add Contact' button.
3. The new contact will appear in the list.

### Updating a Contact

1. Select a contact from the list.
2. Modify the details in the input fields.
3. Click the 'Update Contact' button.

### Deleting a Contact

1. Select a contact from the list.
2. Click the 'Delete Contact' button.
3. Confirm the deletion.

### Searching for Contacts

1. Click the 'Search Contacts' button.
2. Enter a name or keyword in the prompt.
3. The list will update to show only matching contacts.

### Sorting Contacts

- Click on any column header (Name, Phone, Email, Address) to sort the contacts based on that column. Clicking again will toggle between ascending and descending order.

### Saving and Loading Contacts

- The application automatically saves contacts to `contacts.json` in the application's directory. Use the 'Load Contacts' option from the 'File' menu to load contacts from this file upon starting the application.

## About

The Contact Book App was created by Irfan Ullah Khan. It is intended for educational and small-scale personal use. For more information or to report issues, please refer to the contact information provided in the 'About' section of the application.
