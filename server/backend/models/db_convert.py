from brands_obj import BRANDS
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
        try:
            # Create a MongoDB client instance
            mongo_client = pymongo.MongoClient(MONGO_URI)

            # Access the database and collection
            db = mongo_client.get_database("brands")  
            collection = db.get_collection("brands") 

            brand_data = self.to_dict()

            # Insert the document into the collection
            result = collection.insert_one(brand_data)

            # Close the client to release resources
            mongo_client.close()

            return result.inserted_id
        except pymongo.errors.ServerSelectionTimeoutError as e:
            # Handle connection failure and print an error message
            print("Failed to connect to MongoDB: ", e)




try:
    # Create a MongoDB client instance
    mongo_client = pymongo.MongoClient(MONGO_URI)

    # Attempt to connect to MongoDB
    mongo_client.server_info()  # This will trigger a connection attempt

    # If successful, print a success message
    print("Successfully connected to MongoDB.")
except pymongo.errors.ServerSelectionTimeoutError as e:
    # Handle connection failure and print an error message
    print("Failed to connect to MongoDB: ", e)

""" print(BRANDS) """



# Function to insert brands into the database
def insert_brands():
    for brand_data in BRANDS:
        # Create a new Brand object
        brand = Brand(
            name=brand_data["name"],
            description=brand_data.get("description", ""),  
            image=brand_data.get("image", "")  
        )
        
        # Save the brand to the database
        brand.save()

if __name__ == "__main__":
    insert_brands()
    print("Brands inserted successfully.")
