from pymongo import MongoClient
from config import Config

client = MongoClient(
    Config.MONGO_URI,
    serverSelectionTimeoutMS=10000
)

# Force a connection check on startup
client.admin.command("ping")

db = client[Config.DB_NAME]

hotels_collection = db["hotels"]
reviews_collection = db["reviews"]