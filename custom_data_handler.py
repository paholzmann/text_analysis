import json
import os
from JSON_handler import JSONHandler

class CustomData:
    def __init__(self):
        self.json_handler = JSONHandler()

    def get_id(self, filename):
        get_json_data = self.json_handler.get_JSON_data(filename=filename)
        texts = get_json_data.get("texts", [])
        if not texts:
            new_id = 1
        else:
            new_id = get_json_data["texts"][-1]["id"] + 1
        return new_id

    def create_custom_data(self, filename):
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            get_json_data = self.json_handler.get_JSON_data(filename=filename) # Open file and get Data
        else:
            get_json_data = {"texts": []}
        custom_title = input("Enter the title of the text: ")
        custom_content = input("Enter the content of the text: ")
        new_data = {
            "id": self.get_id(filename=filename),
            "title": custom_title,
            "content": custom_content
        }
        get_json_data['texts'].append(new_data)
        
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(get_json_data, file, ensure_ascii=False, indent=4)
        print("=" * 20)
        print("You have sucessfully created new Data.")
