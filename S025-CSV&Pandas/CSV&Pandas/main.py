# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # print(data)
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
# # Tedious to keep writing code above hence we use the help of Pandas

# When using a new library it's a good idea to take a look at documentation or getting started guide if available
import pandas

print()

data = pandas.read_csv("weather_data.csv")  # One step as opposed to open()
print(f"data:\n{data}\n")
print(f"data type:\n{type(data)}\n")
print(f"data[\"temp\"]:\n{data['temp']}\n")
print(f"data[\"temp\"] type:\n{type(data['temp'])}\n")

data_to_dict = data.to_dict()
print(f"data to dictionary:\n{data_to_dict}\n")

temp_list = data["temp"].to_list()
print(f"data[\"temp\"] to list:\n{temp_list}\n")

# average = sum(temp_list) / len(temp_list)
# print(f"Average temp:\n{average:.2f}\n")
# Use a method that comes with pandas
average = data["temp"].mean()
print(f"Average temp:\n{average:.2f}\n")

max_temp = data["temp"].max()
print(f"The max temp is:\n{max_temp}\n")

# Get Data in columns
data_conditions_key = data["condition"]  # Using key
print(f"Data conditions:\n{data_conditions_key}\n")
# Panda automatically saves each heading as an key(above) or an attribute(below) which can be accessed either ways
data_conditions_attribute = data.condition  # Using attribute
print(f"Data conditions:\n{data_conditions_attribute}\n")
# Both methods are correct or can be used
# key and attribute are both case sensitive

# Get data in row
monday_row = data[data.day == "Monday"]
print(f"Get Monday row:\n{monday_row}\n")

# Which data had the max temp
print(f"The highest temp will be on:\n{data[data.temp == data.temp.max()]}\n")

# Access column from row
monday = data[data.day == "Monday"]
monday_condition = monday.condition
print(f"Monday's condition will be:\n{monday_condition}\n")
# Monday temp in Fahrenheit
monday_temp_C = int(monday.temp)
monday_temp_F = (monday_temp_C * 9 / 5) + 32
print(f"Monday's temp will be:\n{monday_temp_C}°C\n{monday_temp_F}°F\n")

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
dict_data_frame = pandas.DataFrame(data_dict)
print(f"New Data frame created:\n{dict_data_frame}\n")
dict_data_frame.to_csv("new_data.csv")
