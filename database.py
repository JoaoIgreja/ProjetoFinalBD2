from typing import Collection
import pymongo


class Database:
    def __init__(self, database, collection):
        self.connected = self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Database connected successfully!")
            return True
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return False


    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            print("Database reseted successfully!")
        except Exception as e:
            print(f"Error resetting the database: {e}")
