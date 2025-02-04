from pymongo import MongoClient
from datetime import datetime

class MongoDB:
    def __init__(self):
        # Connect to MongoDB (adjust the connection string as needed)
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['game_db']
        self.collection = self.db['player_history']

    def save_game_data(self, data):
        """Save game data with timestamp"""
        data['timestamp'] = datetime.utcnow()
        return self.collection.insert_one(data)

    def get_all_data(self):
        """Retrieve all game data for training"""
        return list(self.collection.find({}, {'_id': 0}))