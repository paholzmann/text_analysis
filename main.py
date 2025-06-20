import json
from JSON_handler import JSONHandler
from menu import Menu
from analyzer import Analyzer
from custom_data_handler import CustomData
from output_handler import OutputHandler

def main():
    running = True
    json_handler = JSONHandler()
    custom_data_handler = CustomData()
    menu = Menu()
    analyzer = Analyzer()
    output_handler = OutputHandler()
    sample_texts_filename = "sample_texts.json"
    custom_data_filename = "custom_data.json"
    while running:  # Loop of the App
        text_source = menu.show_text_source_menu() # Welcome Menu: User chooses between their own or sample data
        if text_source == 1: # If user wants to use own Data
            custom_data_handler.create_custom_data(filename=custom_data_filename)
            text_selection = menu.show_text_selection_menu()
            if text_selection == 1:
                json_handler.get_texts_data(filename=custom_data_filename, choice=text_selection)

            elif text_selection == 2:
                json_handler.get_texts_data(filename=custom_data_filename, choice=text_selection)

            elif text_selection == 3:
                json_handler.get_texts_data(filename=custom_data_filename, choice=text_selection)


            individual_text_id = menu.show_get_individual_text_by_id_menu(filename=custom_data_filename) # Show choose text by ID
            text_id, text_title, text_content = json_handler.get_individual_text_by_id(filename=custom_data_filename, id=individual_text_id) # Choose one text by index to analyze it
            
            analyzer.analyzation_choice(text_id=text_id, text_title=text_title, text_content=text_content)
            visualize_numeric_values = output_handler.visualize_numeric_values(text_content)
            visualize_word_length_distribution = output_handler.visualize_word_length_distribution(text_content)
            visualize_word_frequency = output_handler.visualize_word_frequency(text_content)
            word_cloud = output_handler.word_cloud(text_content)
            export_to_csv = output_handler.export_to_csv(text_title,text_content)



        elif text_source == 2: # If user wants to use sample Data
            text_selection = menu.show_text_selection_menu() # User chooses between the options to display data
            if text_selection == 1: # If choice == 1 show all Data (ID, title, content) of all sample texts
                json_handler.get_texts_data(filename=sample_texts_filename, choice=text_selection) # Display all Data

            elif text_selection == 2: # If choice == 2 show only ID and title of all sample texts
                json_handler.get_texts_data(filename=sample_texts_filename, choice=text_selection)

            elif text_selection == 3: # If choice == 3 show only ID and content of all sample texts
                json_handler.get_texts_data(filename=sample_texts_filename, choice=text_selection)

            individual_text_id = menu.show_get_individual_text_by_id_menu(filename=sample_texts_filename) # Show choose text by ID
            text_id, text_title, text_content = json_handler.get_individual_text_by_id(filename=sample_texts_filename, id=individual_text_id) # Choose one text by index to analyze it
            
            analyzer.analyzation_choice(text_id=text_id, text_title=text_title, text_content=text_content)
            
            visualize_numeric_values = output_handler.visualize_numeric_values(text_content)
            visualize_word_length_distribution = output_handler.visualize_word_length_distribution(text_content)
            visualize_word_frequency = output_handler.visualize_word_frequency(text_content)
            word_cloud = output_handler.word_cloud(text_content)
            export_to_csv = output_handler.export_to_csv(text_title,text_content)

if __name__ == '__main__':
    main()
