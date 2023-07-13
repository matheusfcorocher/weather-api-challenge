from pymongo import MongoClient

class MongoConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, port=27017):
        if not hasattr(self, 'client'):
            self.client = MongoClient("mongo", port)

    def get_connection(self):
        return self.client
    
    def get_weather_db(self):
        return self.client["weather"]


# Create an instance of the MongoDB connection
mongo_connection = MongoConnection()
