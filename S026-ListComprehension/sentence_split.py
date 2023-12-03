sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

words = sentence.split()
result = {word:len(word) for word in words}
for key in result:
    print(f"-> {key}: {result[key]}")
