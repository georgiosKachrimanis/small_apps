import pandas as pd
from googletrans import Translator, LANGUAGES
import time

def cut_small_words(source_file:str, cell_name:str, destination_file:str):
    
    df =pd.read_excel(source_file)

    df = df[df[cell_name].str.len() >2]

    df.to_excel(destination_file, index=False)

    print("Process is complete!")

# This function is going to take for ever to run, so maybe it is easier to use the GoogleSheets to do the same thing faster + maybe you will not get a flag of DoS attack :p
def auto_translate(source_file:str, cell_name:str):
    # Load your Excel file into a DataFrame
    df =pd.read_excel(source_file, engine='openpyxl')
    
    # Initialize the Google Translate API
    translator = Translator()
    
    translations = []
    
    for word in df[cell_name]:
        try:
            translated_word = translator.translate(word, src='nl',dest='en').text
            translations.append(translated_word)
        except Exception as e:
            print(f"Error translating {word}: e")
            translations.append("No translation") # so the cell will not be left empty
        time.sleep(0.25) 

    df["English"] = translations
    
    df.to_excel(source_file, index=False, engine='openpyxl')
    
    print("Translation completed!")
    
    
# You can change the files you are going to use. 
source_file = 'day_31/nl.xlsx'
destination_file = "day_31/filtered_nl.xlsx"
cell_name = "Worden"

auto_translate(destination_file, cell_name)
