from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://localhost:27017")  # Assuming MongoDB is running locally
    return client["slack_data_mongo"]