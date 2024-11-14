from pymongo import MongoClient
from app.config.config import Config

client = MongoClient(Config.MONGO_URI)
db = client.email_dispatcher
collection = db.all_messages

def save_to_mongodb(message_data):
    try:
        collection.insert_one(message_data)
    except Exception as e:
        print(f"MongoDB Error: {str(e)}")

