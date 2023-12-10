from openai import OpenAI
from dotenv import load_dotenv
from brands_obj import BRANDS
import os
import pymongo
import json


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(f'OPENAI_API_KEY: {OPENAI_API_KEY}')
MONGO_URI = os.getenv("MONGO_URI")
print(f'MONGI URI: {MONGO_URI}')

client = OpenAI()

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
            print("Failed to connect to MongoDB: ", e)
    
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
            print("Failed to connect to MongoDB: ", e)
            return []




""" try:
    # Create a MongoDB client instance
    mongo_client = pymongo.MongoClient(MONGO_URI)

    # Attempt to connect to MongoDB
    mongo_client.server_info()  # This will trigger a connection attempt

    # If successful, print a success message
    print("Successfully connected to MongoDB.")
except pymongo.errors.ServerSelectionTimeoutError as e:
    # Handle connection failure and print an error message
    print("Failed to connect to MongoDB: ", e) """






# Function to insert brands into the database
def insert_brands():
    for brand_data in BRANDS:

        system_content = f"You are a knowledgeable assistant with comprehensive information about various companies and brands as well designed to output JSON.  For this and future requests we will be generating information about the company Warner Bros. Discovery and its subsidiary companies and brands.  This specific request will cover the subsidiary brand {brand_data['name']}.  We are building a database of information about the company and its brands so please provide detailed and accurate responses to the following questions, even if some details need to be estimated or inferred. If exact information is not available, offer the most likely or plausible details based on your extensive database of knowledge.  For the returned JSON data, please always use these specific keys: name, image, founding_year, founder, history, CEO, board_of_directors, number_of_employees, revenue_information, location, popular_brands_content, description."


        print(f"Querying OpenAI for {brand_data['name']} data...")
        # query openAI for the data
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            seed=42,
            messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"What year was {brand_data['name']} founded?"},
            {"role": "user", "content": f"Write a detailed biography of the history of {brand_data['name']}"},
            {"role": "user", "content": f"Who is the CEO of {brand_data['name']}?"},
            {"role": "user", "content": f"Who is on the board of directors for {brand_data['name']}?"},
            {"role": "user", "content": f"How many employees does {brand_data['name']} have?"},
            {"role": "user", "content": f"Can you provide any information about the company's revenue?"},
            {"role": "user", "content": f"Where is {brand_data['name']} located?"},
            {"role": "user", "content": f"What are some popular shows, or movies, podcasts or brands produced by {brand_data['name']}?"},
            {"role": "user", "content": f"Please write a brief description of {brand_data['name']}."},
            ],
        )

        for choice in response.choices:

            try:
                content = json.loads(choice.message.content)
            except json.JSONDecodeError:
                print(f"Failed to parse JSON content: {choice.message.content}")
                continue
               # Assuming 'content' is now a dictionary

            print(f"content: {content}")
       
            



            brand = Brand(
                name=brand_data.get("name", ""),
                image=brand_data.get("image", ""),
                founding_year=content.get("founded_year", ""),
                founder=content.get("founder", ""),
                history=content.get("biography", ""),
                CEO=content.get("CEO", ""),
                board_of_directors=content.get("board_of_directors", ""),
                number_of_employees=content.get("number_of_employees", ""),
                revenue_information=content.get("revenue_information", ""),
                description=content.get("description", ""),
                location=content.get("location", ""),
                popular_brands_content=content.get("popular_brands_content", [])
            )
            print(f"brand: {brand.__str__()}")
            
            # Save the brand to the database
            print(f"Saving {brand.name} to database...")

            # if brand already exists, skip it
            if Brand.get_all_brands() is not None:
                for existing_brand in Brand.get_all_brands():
                    if brand.name == existing_brand["name"]:
                        print(f"Brand {brand.name} already exists in database.  Skipping...")
                        break
                else:
                    print(f"Brand {brand.name} does not exist in database.  Saving...")
                    brand.save()
          
       








if __name__ == "__main__":
    insert_brands()
    print("All brands inserted successfully.")