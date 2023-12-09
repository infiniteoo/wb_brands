
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
print(f'MONGI URI: {MONGO_URI}')


class Brand:
    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "image": self.image
        }

    def save(self):
        # Access the MongoDB database connection defined in settings.py
        mongo_db = "brands"
        brand_data = self.to_dict()
        result = mongo_db.brands_collection.insert_one(brand_data)
        return result.inserted_id

    @classmethod
    def get_all_brands(cls):
        try:
            # Create a MongoDB client instance
            mongo_client = pymongo.MongoClient(MONGO_URI)

            # Access the database and collection
            db = mongo_client.get_database("brands") 
            collection = db.get_collection("brands")  

            # Fetch all brands from the collection
            brands = list(collection.find({}))

            # Close the client to release resources
            mongo_client.close()

            return brands
        except pymongo.errors.ServerSelectionTimeoutError as e:
            # Handle connection failure and print an error message
            print("Failed to connect to MongoDB: ", e)
            return []
