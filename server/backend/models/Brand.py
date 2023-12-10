
from dotenv import load_dotenv
import os
import pymongo
from Colors import Colors

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
print(f'MONGI URI: {MONGO_URI}')


class Brand:
    def __init__(self, name, description, image, founding_year, founder, history, CEO, board_of_directors, number_of_employees, revenue_information, location, popular_brands_content):
        self.name = name
        self.description = description
        self.image = image
        self.founding_year = founding_year
        self.founder = founder
        self.history = history
        self.CEO = CEO
        self.board_of_directors = board_of_directors
        self.number_of_employees = number_of_employees
        self.revenue_information = revenue_information
        self.location = location
        self.popular_brands_content = popular_brands_content


    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "founding_year": self.founding_year,
            "founder": self.founder,
            "history": self.history,
            "CEO": self.CEO,
            "board_of_directors": self.board_of_directors,
            "number_of_employees": self.number_of_employees,
            "revenue_information": self.revenue_information,
            "location": self.location,
            "popular_brands_content": self.popular_brands_content

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
            print(f"{Colors.RED}Failed to connect to MongoDB: ", e, f"{Colors.RESET}")
          
    
    def __str__(self):
        return (f"Brand(Name: {self.name}, Image: {self.image}, Founding Year: {self.founding_year}, "
                f"Founder: {self.founder}, History: {self.history}, CEO: {self.CEO}, "
                f"Board of Directors: {self.board_of_directors}, Number of Employees: {self.number_of_employees}, "
                f"Revenue Information: {self.revenue_information}, Location: {self.location}, "
                f"Popular Brands Content: {self.popular_brands_content}, Description: {self.description})")

    def __repr__(self):
        return (f"Brand(name={self.name}, image={self.image}, founding_year={self.founding_year}, "
                f"founder={self.founder}, history={self.history}, CEO={self.CEO}, "
                f"board_of_directors={self.board_of_directors}, number_of_employees={self.number_of_employees}, "
                f"revenue_information={self.revenue_information}, location={self.location}, "
                f"popular_brands_content={self.popular_brands_content}, description={self.description})")
    
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
           
           
            print(f"{Colors.RED}Failed to connect to MongoDB: ", e, f"{Colors.RESET}")
            return []