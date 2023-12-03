def band_name_generator():
    city = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    return city + " " + pet_name

print("\nWelcome to the Band Name Generator")
band_name = band_name_generator()
print("Your band name could be " + band_name + "\n")
