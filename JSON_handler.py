import json


class JSONHandler:
    def get_JSON_data(self, filename):  # Data import from JSON file
        try:  # Open JSON file if possiple and return file
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        # If JSON file is not found or there is a DecodeError -> raise Error and return empty list
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"texts": []}
        return data

    def get_texts_data(self, filename, choice): # User chooses between the options to display the data
        texts = self.get_JSON_data(filename=filename)
        if not texts:
            print("No texts available!")
        if choice == 1: # If choice == 1 get all Data (ID, title, content) of all sample texts
            print("=== All texts ==")
            for text in texts['texts']:  # If Data available print Data
                        print(f"ID: {text['id']}")
                        print(f"Title: {text['title']}")
                        print(f"Content: {text['content']}")
                        print("=" * 20)
        elif choice == 2: # If choice == 2 get only ID and title of all sample texts
            print("=== Text titles ===")
            for text in texts['texts']:  # If Data available print Data
                print(f"Title {text['id']}: {text['title']}")
                print("=" * 20)
        elif choice == 3: # If choice == 3 get only ID and content of all sample texts
            print("=== Text content ===")
            for text in texts['texts']:  # If Data available print Data
                print(f"Content: {text['id']}: {text['content']}")
                print("=" * 20)
        else:
            print("You have to choose either 1, 2 or 3.")

    def get_individual_text_by_id(self, filename, id):  # Get one Individual Text including ID, title and content using ID
        texts = self.get_JSON_data(filename=filename)
        if not texts:  # If no Data available
            print("No texts available!")
        print("=" * 20)
        print(f"You have chosen text {id}.")
        print(f"ID: {texts['texts'][id - 1]['id']}")
        print(f"Title: {texts['texts'][id - 1]['title']}")
        print(f"Content: {texts['texts'][id - 1]['content']}")
        print("=" * 20)
        text_id = texts['texts'][id - 1]['id']
        text_title = texts['texts'][id - 1]['title']
        text_content = texts['texts'][id - 1]['content']
        return text_id, text_title, text_content


#json_hanlder = JSONHandler()
#json_hanlder.get_texts_data(filename="sample_texts.json", choice=3)
