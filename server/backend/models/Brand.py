
# reference existing db connection from settings.py
from django.db import connections

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
        mongo_db = connections['default']
        brand_data = self.to_dict()
        result = mongo_db.brands_collection.insert_one(brand_data)
        return result.inserted_id

    # Other methods...
