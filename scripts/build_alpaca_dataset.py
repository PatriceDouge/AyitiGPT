import json

def build_dataset(file_path, output_path):
    translations = []  # Initialize an empty list to hold the dictionaries

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            english_text = file.readline().strip()
            # Skip any empty lines for the English text
            while not english_text:
                english_text = file.readline().strip()
                if english_text == "":  # End of file reached
                    break

            creole_translation = file.readline().strip()
            # Skip any empty lines for the Creole translation, and ensure it's not the end of file
            while not creole_translation:
                creole_translation = file.readline().strip()
                if creole_translation == "":  # End of file or next English text reached
                    break

            # Check if we've reached the end of the file or a new pair
            if not english_text or not creole_translation:
                break

            # Construct a dictionary for the current pair
            translation_dict = {
                "instruction": "translate the following text from english to haitian creole",
                "input": english_text,
                "output": creole_translation
            }

            # Append the dictionary to the list
            translations.append(translation_dict)

    # Convert the list to a JSON string
    json_output = json.dumps(translations, indent=4)

    # Save the JSON string to a file
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_output)

def main():
    # Replace 'translations.txt' and 'output.json' with the actual paths
    build_dataset('../data/medical_domain_data_ht.txt', 'alpaca_ht.json')

if __name__ == '__main__':
    main()
