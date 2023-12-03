student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# 1.
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

# 2.
word = input("Enter a word: ").upper()

# One line of code however the order is incorrect
# phonetic_code_words = [value for (key, value) in nato_dict.items() if key in list(word)]

# phonetic_code_words = []
# for letter in word:
#     if letter in nato_dict:
#         phonetic_code_words.append(nato_dict[letter])
#     else:
#         phonetic_code_words.append(letter)

phonetic_code_words = [nato_dict[letter] for letter in word]
print(phonetic_code_words)
for phonetic_code_word in phonetic_code_words:
    print(f"-> {phonetic_code_word[0]} for {phonetic_code_word}")
