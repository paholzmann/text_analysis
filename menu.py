from JSON_handler import JSONHandler


class Menu:

    def show_text_source_menu(self): # Welcome Menu: User chooses between their own or sample data
        print("=" * 20)
        print("Welcome to the Text-Analyzer!")
        print("1: Use your own text")
        print("2: Use a sample text")
        while True: # While no valid input
            try: # Try to get a valid input
                text_source = int(input("Choose an option: ")) # User chooses between own or sample data 1 -> own data; 2 -> sample data
                if text_source in [1, 2]: # If choice is 1 or 2
                    return text_source
                else: # If choice is not 1 or 2 but a number
                    print("The number is out of range. Enter either 1 or 2.")
            except ValueError: # If choice is not 1 or 2 nor a number
                print("Please enter a number.")
            print("=" *20)
    
    def show_text_selection_menu(self): # Show sample Data
        print("1: Show ID, title and content")
        print("2: Show only title")
        print("3: Show only content")
        while True: # While no valid input
            try: # Try to get a valid input
                text_selection = int(input("Choose an option: ")) # User chooses between 1 -> show ID, title and content; 2 -> show only ID and title; 3 -> show only ID and content 
                if text_selection in [1, 2, 3]: # If choice is 1, 2 or 3
                    return text_selection
                else: # If choice is not 1, 2 or 3 but a number
                    print("The number is out of range. Enter either 1, 2 or 3.")
            except ValueError: # If choice is not 1, 2 or 3 nor a number
                print("Please enter a number.")
    
    def show_operations_menu(self): # Show possible operations the user can perform on data
        operations = ["Count characters", "Count words"]
        operation_index = 1
        for operation in operations:
            print(f"Operation {operation_index}: {operation}")
            operation_index += 1
        while True: # While no valid input
            try: # Try to get a valid input
                chosen_operation = int(input("Choose an option: "))
                if 1 <= chosen_operation <= len(operations): # If the choice is >= 1 and <= len(operations) -> choice is in index
                    return chosen_operation
                else: # If the choice is not >= 1 or <= len(operations) -> choice is out of index
                    print("The number is out of range.")
            except ValueError: # If choice is not in index nor a number
                print("Please enter a number.")

    def show_get_individual_text_by_id_menu(self, filename): # User decides which text to analyze with ID of text
        print("Which text do you want to analyze?")
        json_handler = JSONHandler()
        texts = json_handler.get_JSON_data(filename=filename)
        while True: # While no valid input
            try: # Try to get a valid input
                analyze_text_id = int(input("Please enter number of text: "))
                if 1 <= analyze_text_id <= len(texts['texts']): # If the choice is >= 1 and <= len(texts['texts']) -> choice is in index
                    return analyze_text_id
                else: # If the choice is not >= 1 or <= len(texts['texts']) -> choice is out of index
                    print("Please choose a valid index.")
            except ValueError: # If choice is not in index nor a number
                print("Please enter a number.")
