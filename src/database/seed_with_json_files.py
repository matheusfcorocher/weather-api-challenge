def make_seed_mongo_database_with_json_files(directory_lister, path_joiner, json_loader):

    def seed_mongo_database_with_json_files(mongo_collection, seed_path):
        seed_dir = seed_path

        # Delete all documents from the collection
        mongo_collection.delete_many({})
        
        for filename in directory_lister(seed_dir):
            if filename.endswith('.json'):
                with open(path_joiner(seed_dir, filename)) as file:
                    data = json_loader(file)
                    mongo_collection.insert_one(data)
    
    return seed_mongo_database_with_json_files

