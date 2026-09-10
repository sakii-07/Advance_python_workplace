from pymongo import MongoClient

# server path
client = MongoClient("mongodb://localhost:27017/")

# database name
db = client["company"]

# collection name
collection = db["employees"]

employee = collection.find()
for emp in employee:
    print(emp)