import json

def build_dataset(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file, open(output_path, 'w', encoding='utf-8') as jsonl_file:
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

            # Write the dictionary to the JSONL file, converting it to a JSON string with a newline character
            jsonl_file.write(json.dumps(translation_dict) + '\n')

def main():
    # Replace 'translations.txt' and 'output.json' with the actual paths
    build_dataset('../data/medical_domain_data_ht.txt', 'alpaca_ht.jsonl')

if __name__ == '__main__':
    main()
