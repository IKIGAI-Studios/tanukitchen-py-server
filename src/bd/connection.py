from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from decouple import config
import dns.resolver

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

def get_database():
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = config("MONGO_CONNECTION_LINK")
   DB_NAME = config("MONGO_DB_NAME")

   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   try:
      client = MongoClient(CONNECTION_STRING)

      client.admin.command('ping')
      print("Conectado correctamente al servidor de MongoDB!")
      return client[DB_NAME]
   
   except Exception as e:
      print(e)
   
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()

#get_database()