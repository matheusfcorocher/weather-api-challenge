from pymongo import MongoClient

def connect_to_database(port=27017):
    # Connect to MongoDB
    client = MongoClient("mongo", port)
    db = client["mydatabase"]
    collection = db["mycollection"]