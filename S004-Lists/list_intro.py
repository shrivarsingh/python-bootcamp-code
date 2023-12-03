# Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0]) # First item in list
print(states_of_america[-1]) # Last item in list

print(len(states_of_america))
print(states_of_america[len(states_of_america)-1])

states_of_america[1] = "Pencilvania" # Change a value
states_of_america.append("Angelaland") # Add data to end of list

print(states_of_america)

states_of_america.extend(["Python Island", "Jack Bauer Land"])

print(states_of_america)
