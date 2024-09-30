# Project Name
A Flask project - for managing contacts in different databases.

## Table of Contents

- [Use](#about)
- [Installation](#installation)
- [Run](#run)
- [Access the application](#access_the_application:)
- [Contacts](#contact)



## About
Contact management system:
Using the following technologies:
* Flask
* Mysql Connector
* PyMongo
* DotEnv


## Installation

###### Python installation
```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
```

#### .venv creation (Optional)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### install dependencies
```bash
pip3 install -r requirements.txt
```

## Run
#### environment variables
This project requires the following environment variables to be set:
Create a .env file in the root of your project and add the following lines:
#### Required Variables:
- DB_HOST= The hostname of your MySQL database. default localhost
- DB_USER= The username for your MySQL database. default root
- DB_PASSWORD= The password for your MySQL database. default admin
- DB_NAME= The name of your MySQL database. default contacts_app
- DATABASE_TYPE= MYSQL or MONGO. default MYSQL
- DB_PORT= The port of your MySQL database. default 3306
- MONGO_URI= in case you are using mongodb default - mongodb://localhost:27017/


```bash
python3 app.py
```

## Access_the_application:
application should be available at port 5050
Route examples:
- http://localhost:5050/
- http://127.0.0.1:5050/view_contacts
- http://127.0.0.1:5050/editContactForm/{id}
- http://127.0.0.1:5050/add_contact_form/


