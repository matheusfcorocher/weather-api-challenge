import json
import os

from database_connection import mongo_connection

def make_seed_mongo_database_with_json_files(directory_lister, path_joiner, json_loader):

    def seed_mongo_database_with_json_files(db, seed_path, collection_name):
        seed_dir = seed_path
        collection = db[collection_name]

        # Delete all documents from the collection
        collection.delete_many({})
        
        for filename in directory_lister(seed_dir):
            if filename.endswith('.json'):
                with open(path_joiner(seed_dir, filename)) as file:
                    data = json_loader(file)
                    collection.insert_one(data)
    
    return seed_mongo_database_with_json_files

db = mongo_connection.get_weather_db()
seed_with_json_files = make_seed_mongo_database_with_json_files(
    directory_lister=os.listdir, 
    path_joiner=os.path.join, 
    json_loader=json.load
)
seed_with_json_files(db, './data/seeds', "weather")