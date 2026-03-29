from pymongo import MongoClient
from config import Config
import certifi

client = MongoClient(
    Config.MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)

db = client[Config.DB_NAME]

hotels_collection = db["hotels"]
reviews_collection = db["reviews"]