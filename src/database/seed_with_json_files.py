import json
import os

from database_connection import mongo_connection

def seed_mongo_database_with_json_files(db, seed_path, collection_name):
    seed_dir = seed_path
    collection = db[collection_name]

    # Delete all documents from the collection
    collection.delete_many({})
    
    for filename in os.listdir(seed_dir):
        if filename.endswith('.json'):
            with open(os.path.join(seed_dir, filename)) as file:
                data = json.load(file)
                collection.insert_one(data)

db = mongo_connection.get_weather_db()
seed_mongo_database_with_json_files(db, './data/seeds', "weather")