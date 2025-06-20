
class Analyzer:


    def analyzation_choice(self, text_id, text_title, text_content): # User chooses between analytic operations
        analyzation_choices = ['Count characters', 'Count words', 'Clean text', 'Average word length', 'Group words', 'Shortest word', 'Longest word',
                            'Remove stopwords', 'Sentence stats', 'Count unique words', 'Word frequency', 'Word length distribution', 'Extract keywords',
                            'Count syllables', 'Readability score']
        analyzation_index = 0
        for analyzation_choice in analyzation_choices:
            print(f"Analyzation {analyzation_index + 1}: {analyzation_choice}")
            analyzation_index += 1
        
        made_choice = False
        while not made_choice:
            try:
                choice = int(input("Please enter the analyzation you want to perform: "))
                if choice > len(analyzation_choices) or choice <= 0:
                    print("The number is out of range. Enter a valid number.")
                else:
                    made_choice = True
            except ValueError:
                print("Please enter a number.")

        if choice == 1:
            character_count = self.count_characters(text=text_content)
            print(f"The text is: {character_count} characters long.")
        elif choice == 2:
            word_count = self.count_words(text=text_content)
            print(f"The text is: {word_count} words long.")
        elif choice == 3:
            clean_text = self.clean_text(text=text_content)
            print(f"The text is cleaned from punctuation: {clean_text}.")
        elif choice == 4:
            avg_word_length = self.average_word_length(text=text_content)
            print(f"The average word length of the text is: {avg_word_length}.")
        elif choice == 5:
            word_list = self.group_words(text=text_content)
            print(f"The text in a word list: {word_list}.")
        elif choice == 6:
            shortest_word = self.shortest_word(text=text_content)
            print(f"The shortest word of the text is: {shortest_word}.")
        elif choice == 7:
            longest_word = self.longest_word(text=text_content)
            print(f"The longest word in the text is: {longest_word}.")
        elif choice == 8:
            remove_stopwords = self.remove_stopwords(text=text_content)
            print(f"The text without stopwords: {remove_stopwords}.")
        elif choice == 9:
            num_sentences, avg_sentence_length = self.sentence_stats(text=text_content)
            print(f"The number of sentences is: {num_sentences} and the average sentence length is: {avg_sentence_length}.")
        elif choice == 10:
            unique_words = self.count_unique_words(text=text_content)
            print(f"Unique words and how often they reacur in the text: {unique_words}.")
        elif choice == 11:
            word_frequency = self.word_frequency(text=text_content)
            print(f"How frequent is every word in the text: {word_frequency}.")
        elif choice == 12:
            word_length_distribution = self.word_length_distribution(text=text_content)
            print(f"What is the word length distribution in the text: {word_length_distribution}.")
        elif choice == 13:
            extract_keywords = self.extract_keywords(text=text_content)
            print(f"Keywords in the text: {extract_keywords}")
        elif choice == 14:
            count_syllables = self.count_syllables(text=text_content)
            print(f"Count the number of syllables in the text: {count_syllables}")
            print(f"")
        elif choice == 15:
            readability_score = self.readability_score(text=text_content)
            text_readability = ""
            if readability_score <= 30:
                text_readability = "Academic or legal documents"
            elif 30 < readability_score <= 50:
                text_readability = "Formal writing"
            elif 50 < readability_score <= 70:
                text_readability = "Plain English / newspapers"
            elif 70 < readability_score:
                text_readability = "Very Easy"
            print(f"The readability score of the text is: {readability_score} which means that the text is on {text_readability} levels.")


    def count_characters(self, text): # Counts the number of characters in the text
        characters = len(text)
        return characters
    
    def count_words(self, text): # Counts the number of words in the text
        words = len(text.split())
        return words

    def clean_text(self, text):  # Remove punctuation
        punctuation = ['.', ':', ';', ',', '!', '?', '(', ')', '"', "'"]
        cleaned_text = ""
        for character in text:
            if character not in punctuation:
                cleaned_text += character
        return cleaned_text
    
    def average_word_length(self, text): # Calculates the average word length in the text
        cleaned_text = self.clean_text(text=text)
        clean_text_count_words = self.count_words(text=cleaned_text)
        clean_text_count_characters = self.count_characters(text=cleaned_text)
        average_word_length = clean_text_count_characters / clean_text_count_words
        return average_word_length
        
    def group_words(self, text):
        cleaned_text = self.clean_text(text=text)
        words_in_cleaned_text = cleaned_text.split()
        word_list = []
        for word in words_in_cleaned_text:
            word_list.append(word)
        return word_list
    
    def shortest_word(self, text): # Find shortest word
        word_list = self.group_words(text=text)
        shortest_word = ""
        for word in word_list:
            if shortest_word == "":
                shortest_word = word
            else:
                if len(shortest_word) > len(word):
                    shortest_word = word

        return shortest_word
    
    def longest_word(self, text): # Find longest word
        word_list = self.group_words(text=text)
        longest_word = ""
        for word in word_list:
            if longest_word == "":
                longest_word = word
            else:
                if len(longest_word) < len(word):
                    longest_word = word
        return longest_word
    
    def remove_stopwords(self, text): # Remove stopwords
        stopwords = ['the', 'is', 'in', 'at', 'of', 'on', 'and', 'a', 'an', 'to', 'for', 'with', 'by', 'from', 'that', 'this', 'it', 'as', 'be',
                    'are', 'was', 'were', 'but', 'or', 'not', 'you', 'I', 'he', 'she', 'we', 'they', 'them', 'his', 'her', 'my', 'your', 'us',
                    'has', 'these']
        stopwords = [word.lower() for word in stopwords]
        cleaned_text = ""
        words_list = self.group_words(text=text)
        for word in words_list:
            if word.lower() not in stopwords:
                cleaned_text += word
                cleaned_text += " "
        return cleaned_text
    
    def sentence_stats(self, text): # Calculates the number of sentences and the average sentence length
        punctuation = ['.', '!', '?']
        number_of_sentences = 0
        word_count = 0
        words = text.split()
        for word in words:
            word_count += 1
            for symbol in punctuation:
                if symbol in word:
                    number_of_sentences += 1
                    break
        if number_of_sentences > 0:
            average_sentence_length = word_count / number_of_sentences
        else:
            average_sentence_length = 0
        return number_of_sentences, average_sentence_length
    
    def count_unique_words(self, text): # Find and calculate the number of unique words in the text
        words = self.group_words(text=text)
        words = [word.lower() for word in words]
        unique_words = set(words)
        unique_words_count = len(unique_words)
        return unique_words, unique_words_count

    def word_frequency(self, text): # Find how often a word reacures
        words = self.group_words(text=text)
        words = [word.lower() for word in words]
        word_frequency = {}
        for word in words:
            if word not in word_frequency:
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1
        word_frequency = sorted(word_frequency.items(), key=lambda x: x[1])
        return word_frequency
    
    def word_length_distribution(self, text): # Find how many words have which word length
        words = self.group_words(text=text)
        words = [word.lower() for word in words]
        word_length_distribution = {}
        for word in words:
            word_length = len(word)
            if word_length not in word_length_distribution:
                word_length_distribution[word_length] = 1
            else:
                word_length_distribution[word_length] += 1
        word_length_distribution = sorted(word_length_distribution.items(), key=lambda x: x[0])
        return word_length_distribution
    
    def extract_keywords(self, text): # Find the top 5 keywords in the text
        cleaned_text = self.clean_text(text=text)
        cleaned_text = self.remove_stopwords(text=cleaned_text)
        word_frequency = self.word_frequency(text=cleaned_text)
        top_n = 5
        keywords = [word for word, count in word_frequency[:top_n]]
        return keywords

    def count_syllables(self, text):  # Count Syllables
        word_list = self.group_words(text=text)
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        syllable_count = 0
        for word in word_list:
            syllable_in_word = 0
            previous_character_was_vowel = False
            for character in word:
                if character in vowels and not previous_character_was_vowel:
                    syllable_in_word += 1
                    previous_character_was_vowel = True
                else:
                    previous_character_was_vowel = False
            if word.endswith('e') and syllable_in_word > 1:
                syllable_in_word -= 1
            if syllable_in_word == 0:
                syllable_in_word = 1
            syllable_count += syllable_in_word
        return syllable_count
        
        
    def readability_score(self, text): # Readability score -> how easy is the text to read
        _, average_sentence_length = self.sentence_stats(text=text)
        syllable_count = self.count_syllables(text=text)
        number_words = len(self.group_words(text=text))
        syllable_per_word = syllable_count / number_words
        flesch_reading_ease = 206.835 - 1.015 * (average_sentence_length) - 84.6 * (syllable_per_word)
        return flesch_reading_ease
