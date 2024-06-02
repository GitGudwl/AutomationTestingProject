# features/helpers/json_helper.py

import json

class JsonHelper:
    @staticmethod
    def load_json_from_file(file_path):
        with open(file_path) as f:
            data = json.load(f)
        return data
    
    @staticmethod
    def save_json_to_file(data, file_path):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
