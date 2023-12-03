# file = open("my_file.txt")  # save to a variable called file
# contents = file.read()
# print( contents)
# file.close()
# print(contents)

# # Using the with keyword we don't have to use close()
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# # Write to a file
# # Note default mode for the above is r for READ ONLY
# # Change mode to WRITE and use write()
# with open("my_file.txt", mode="w") as file:
#     file.write("New text")
# # Note this method will overwrite previous contents

# # Write to a file by appending
# # Change mode to APPEND and use write()
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")
# # Note this method is similar to a list and append()
# # Add a \n so we write to a new line instead of directly after previous contents

# if in WRITE mode and file doesn't exist a new file will be created
with open("file.txt", mode="w") as file:
    file.write("Text.")

#Reading Files

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#Writing to Files

with open("my_file.txt", mode="w") as file:
    file.write("New text.")
    
#Opening a File that doesn't exit in write mode will create it from scratch

with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("New text.")
