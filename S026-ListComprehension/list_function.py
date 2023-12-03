weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

def convert_c_to_f(temp_c):
    """Takes in temp as degrees Celcius and converts it into degrees Farenheight and returns that value."""
    return round((temp_c * 9 / 5) +  32, 1)

weather_f = {day:convert_c_to_f(temp_c) for (day, temp_c) in weather_c.items()}

print(weather_f)
