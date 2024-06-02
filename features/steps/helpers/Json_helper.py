# features/helpers/json_helper.py

import json
import random
import string

class JsonHelper:
    @staticmethod
    def load(file_path):
        with open(file_path) as f:
            data = json.load(f)
        return data
    
    @staticmethod
    def save(data, file_path):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
            
    @staticmethod
    def random_email(length):
        name = ''.join(random.choices(string.ascii_lowercase, k=length))
        return f"{name}@example.com"