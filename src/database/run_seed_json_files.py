import json
import os

from database_connection import mongo_connection
from seed_with_json_files import make_seed_mongo_database_with_json_files

db = mongo_connection.get_weather_db()
collection = db["data"]

seed_with_json_files = make_seed_mongo_database_with_json_files(
    directory_lister=os.listdir, 
    path_joiner=os.path.join, 
    json_loader=json.load
)

seed_with_json_files(collection, './data/seeds')