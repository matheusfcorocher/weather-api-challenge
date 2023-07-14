from pymongo import MongoClient

class MongoConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, mongo_client, port=27017):
        if not hasattr(self, 'client'):
            self.client = mongo_client("mongo", port)

    def get_connection(self):
        return self.client
    
    def get_weather_db(self):
        return self.client["weather"]
    
    def __del__(self):
        self.client.close()


# Create an instance of the MongoDB connection
mongo_connection = MongoConnection(mongo_client = MongoClient)
