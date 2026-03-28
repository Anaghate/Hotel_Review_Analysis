from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]

hotels_collection = db["hotels"]
reviews_collection = db["reviews"]