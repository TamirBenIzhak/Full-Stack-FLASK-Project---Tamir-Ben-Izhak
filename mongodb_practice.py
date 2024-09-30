import pymongo

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#Insert a record in the "customers" collection:
# mydict = {"name": "John", "address": "Highway 37"}
# result = mycol.insert_one(mydict)

#print(result.inserted_id)


# mylist = [
#  { "name": "Amy", "address": "Apple st 652"},
#  { "name": "Hannah", "address": "Mountain 21"},
#  { "name": "Michael", "address": "Valley 345"},
#  { "name": "Sandy", "address": "Ocean blvd 2"},
#  { "name": "Betty", "address": "Green Grass 1"},
#  { "name": "Richard", "address": "Sky st 331"},
#  { "name": "Susan", "address": "One way 98"},
#  { "name": "Vicky", "address": "Yellow Garden 2"},
#  { "name": "Ben", "address": "Park Lane 38"},
#  { "name": "William", "address": "Central st 954"},
#  { "name": "Chuck", "address": "Main Road 989"},
#  { "name": "Viola", "address": "Sideway 1633"}
# ]

# # Insert multiple documents into the "customers" collection:
# result = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(result.inserted_ids)

# reslut = mycol.find_one()
# print(reslut)

# for document in mycol.find():
# result = mycol.find()

# result = mycol.find({}, {"_id": 0, "name": 1, })


# query = {"address": "Park Lane 38"}

# query = {"address": {"$gt":"S"}}


# result= mycol.find(query).sort({"name": -1})

#update the document with the address Valley 345 to sherlock holmes address:
# mycol.update_one({"address": "Valley 345"}, {"$set": {"address": "Baker Street 221B"}})

#update all customers with aaddress starting with S set name to be Minne

# myquery = {"name": "Betty", "address": "Green Grass 1"}
# newvalues = {"$set": {"name": "Arya Stark", "address": "Winterfell"}}
# mycol.update_many(myquery, newvalues)

#drop the collection
mycol.drop()

#drop the database
myclient.drop_database("mydatabase")

for document in mycol.find():
    print(document)

