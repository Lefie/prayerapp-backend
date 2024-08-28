import certifi
import os 
from dotenv import load_dotenv
import pymongo

# load env variables 
load_dotenv()

# create a client and connect to the database 
client = pymongo.MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())

try:
    db = client[os.getenv('DB_NAME')]
    client.admin.command('ping')
    print('You successfully connected to MongoDB!')
except Exception as e:
    print(e)

