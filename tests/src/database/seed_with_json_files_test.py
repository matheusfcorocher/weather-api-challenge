import json
import os
import sys

sys.path.append('./src/database')
from seed_with_json_files import make_seed_mongo_database_with_json_files

class Test_seed_with_json_files:
    """
        Description
        -----------
            This class contains tests cases to check seed_with_json_files class
            from seed_with_json_files.py.
    """
    
    def test_seeding_mongodb_with_json(self, tmpdir):
        """
            Description
            -----------
                When is given a mongo connection and seed
                with seed_with_json_files fn
            
            Expected Result
            ---------------
                returns True
        """
        
        # setup

        # Create a temporary directory and dummy JSON files for testing
        seed_dir = tmpdir.mkdir("seeds")
        file1 = seed_dir.join("data1.json")
        file1.write('{"name": "John"}')
        file2 = seed_dir.join("data2.json")
        file2.write('{"name": "Jane"}')

        # Get a reference to the database and collection
        class FakeMongo:
            def __init__(self):
                self.weather = []
            def count_documents(self, value):
                return len(self.weather)
            def delete_many(self, value):
                self.weather = []
            def insert_one(self, data):
                self.weather.append(data)

        collection = FakeMongo()

        # When
        # Seed the database with the JSON files
        seed_with_json_files = make_seed_mongo_database_with_json_files(
            directory_lister=os.listdir,
            path_joiner=os.path.join,
            json_loader=json.load
        )

        seed_with_json_files(collection, str(seed_dir))

        #Assertion
        # Check the documents in the collection
        assert collection.count_documents({}) == 2
