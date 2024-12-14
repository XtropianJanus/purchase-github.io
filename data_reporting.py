# Data Reporting Module

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  

# Connection string to MongoDB Atlas
connection_string = os.getenv('MONGODB_CONNECTION_STRING')

# Create a MongoClient to the running MongoDB instance
client = MongoClient(connection_string)

# Access the database
db = client['direct_purchase_system']  # Replace with your actual database name

def generate_report(report_type):
    # Logic to generate different types of reports
    print(f"Generating report of type: {report_type}")
    pass

# Example function to get data from a collection
def get_data_from_collection(collection_name):
    collection = db[collection_name]  # Access the specified collection
    data = collection.find()  # Retrieve all documents in the collection
    return list(data)  # Convert cursor to a list

# Example usage
if __name__ == "__main__":
    ingredients_data = get_data_from_collection('ingredients')  # Replace with your collection name
    for ingredient in ingredients_data:
        print(ingredient)
