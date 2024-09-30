from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Choose database type
DB_TYPE = os.getenv("DB_TYPE", "SQL")

# Import database functions based on DB_TYPE
if DB_TYPE == "SQL":
    from data_sql import (
        get_contacts, 
        find_by_number, 
        contact_exists, 
        search_contacts, 
        create_contact, 
        delete_contact, 
        update_contact
    )
else:
    from data_mongo import (
        get_contacts, 
        find_by_number, 
        check_contact_exists as contact_exists,  
        search_contacts, 
        create_contact, 
        delete_contact, 
        update_contact
    )

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('view_contacts'))

@app.route('/view_contacts')
def view_contacts():
    contacts = get_contacts()
    return render_template('view_contacts.html', contacts=contacts, DB_TYPE=DB_TYPE)


@app.route('/add_contact_form')
def add_contact_form():
    return render_template('add_contact_form.html', error=None)

@app.route('/add_contact', methods=['POST'])
def add_contact_route():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']
    photo = request.files['photo']
   
   
    if contact_exists(name, email):
        return render_template('add_contact_form.html', error=True)

    # Save the photo
    if photo:
        photo_filename = f"{name}.jpg"
        photo_path = os.path.join('static/images', photo_filename)
        photo.save(photo_path)
    else:
        photo_filename = 'default.jpg'

    # Create the contact
    create_contact(name, phone, email, gender, photo_filename)
    return redirect(url_for('view_contacts'))

@app.route('/delete_contact/<int:number>', methods=['POST'])
def delete_contact_route(number):
    delete_contact(number)  # Pass the number directly
    return redirect(url_for('view_contacts'))




@app.route('/search', methods=['POST'])
def search():
    search_name = request.form['search_name']
    search_results = search_contacts(search_name)
    return render_template('view_contacts.html', contacts=search_results)


@app.route('/editContact/<int:number>')
def editContact(number):
    contact = find_by_number(number)  # Find the contact by its number
    if not contact:
        return "Contact not found", 404
    return render_template('editContactForm.html', contact=contact)

@app.route('/saveUpdatedContact/<int:number>', methods=['POST'])
def saveUpdatedContact(number):
    name = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']

    update_contact(number, name, phone, email, gender)
    return redirect(url_for('view_contacts'))




if __name__ == '__main__':
    app.run(debug=True)
