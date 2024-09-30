import pymongo
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
myclient = pymongo.MongoClient(os.getenv("MONGO_URI"))
mydb = myclient[os.getenv("DB_NAME")]
my_collection = mydb["contacts"]

def get_next_number():
    last_contact = my_collection.find_one(sort=[("number", pymongo.DESCENDING)])
    if last_contact:
        return last_contact["number"] + 1
    else:
        return 1


def create_contact(name, phone, email, gender, photo):
    number = get_next_number()
    
    my_collection.insert_one({
        "number": number,  
        "name": name,
        "phone": phone,
        "email": email,
        "gender": gender,
        "photo": photo
    })

def get_contacts():
    # Ensure you retrieve the 'number' field along with others
    return list(my_collection.find({}, {"_id": 1, "number": 1, "name": 1, "phone": 1, "email": 1, "gender": 1, "photo": 1}))

def find_by_number(number):
    # Find by the custom 'number' field
    return my_collection.find_one({"number": number})

def check_contact_exists(name, email):
    query = {"$or": [{"name": name}, {"email": email}]}
    result = my_collection.find_one(query)
    return bool(result)

def search_contacts(search_name):
    query = {"name": {"$regex": search_name, "$options": "i"}}
    return list(my_collection.find(query))

def delete_contact(number):
    # Delete by the custom 'number' field
    my_collection.delete_one({"number": number})

def update_contact(number, name, phone, email, gender):
    # Update by the custom 'number' field
    my_collection.update_one(
        {"number": number},
        {"$set": {"name": name, "phone": phone, "email": email, "gender": gender}}
    )
