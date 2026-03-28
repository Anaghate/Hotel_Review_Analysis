from pymongo import MongoClient
from config import Config
import certifi
import os
import ssl

print("MONGO_URI present:", bool(os.getenv("MONGO_URI")))
print("DB_NAME:", os.getenv("DB_NAME"))
print("OpenSSL version:", ssl.OPENSSL_VERSION)

client = MongoClient(
    Config.MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)

try:
    client.admin.command("ping")
    print("MongoDB ping successful")
except Exception as e:
    print("MongoDB ping failed:", str(e))
    raise

db = client[Config.DB_NAME]

hotels_collection = db["hotels"]
reviews_collection = db["reviews"]