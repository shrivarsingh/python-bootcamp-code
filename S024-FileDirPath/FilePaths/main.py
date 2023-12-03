# Save a text file named "my_file.txt" on the Desktop
def create_file():
    with open("/Users/shriv/Desktop/my_file.txt", mode="w") as file:
        file.write("Hello.")
        print("File created")
create_file()

# Using windows style \ for windows PC
with open("C:\\Users\\shriv\\Desktop\\my_file.txt", mode="r") as file:
    contents = file.read()
    print(f"Forward slash: {contents}")

# Python can use / for windows as well
with open("/Users/shriv/Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(f"Back slash: {contents}")

# Going backwards relative to working directory = day-24-file-paths
with open("../../../../Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(f"Relative path: {contents}")
