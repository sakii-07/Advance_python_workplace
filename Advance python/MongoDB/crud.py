from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["college"]

collection = db['teachers']

def InsertRecord():
    collection.insert_many(
        [
            {"_id":1001,
            "name":"sakshi",
            "age":21,
            "salary":30000
            },
            {
                "_id":1002,
                "name":"supriya",
                "age":30,
                "salary":50000
            }
        ]
    )
    print("Teacher added successfully")

def ShowAll():
    print(" Teachers ".center(50,"-"))

    teacher = collection.find()
    for t in teacher:
        print(t)

def UpdateTeacher():
    collection.update_one(
        {"name":"supriya"},
        {"$set":{"age":20}}
    )
    print("Teacher updated successfully")

def DeleteTeacher():
    collection.delete_one(
        {"name":"sakshi"}
    )

def InOperator():
    t = collection.find(
        {"name" : {"$in":["sakshi"]}}
    )
    for i in t:
        print(i)

def OrOperator():
    t = collection.find(
        {
        "$or" :[
            {"salary":50000},
            {"name":"sakshi"}
        ]
        }
    )
    for i in t:
        print(i)