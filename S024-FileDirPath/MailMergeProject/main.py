# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

print("\nMail Merge Project Starting up.\n")

# Get names from txt file and save it in a list
names_list = []
with open("Input/Names/invited_names.txt", mode="r") as invited_names:
    for invited_name in invited_names.readlines():
        names_list.append(invited_name.strip())

# Get the contents from the starting letter and save it in a variable
with open("Input/Letters/starting_letter.docx", mode="r") as starting_letter:
    letter = starting_letter.read()

# Save each letter with a new name
for name in names_list:
    letter_to_name = letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.docx", mode="w") as letter_to_send:
        letter_to_send.write(letter_to_name)

print("Mail Merge Project completed all tasks.")
