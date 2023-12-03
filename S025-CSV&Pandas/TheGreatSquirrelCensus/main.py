import pandas

print("\nThe Great Squirrel Census!\n")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(f"Squirrel Primary Colours:\n\tGrey\t=\t{gray_squirrels_count}\n\tRed\t\t=\t{cinnamon_squirrels_count}"
      f"\n\tBlack\t=\t{black_squirrels_count}\n")

data_dict_squirrel_count = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
print(f"Dictionary created:\n{data_dict_squirrel_count}\n")

data_frame_squirrel_count = pandas.DataFrame(data_dict_squirrel_count)
print(f"DataFrame created from dictionary:\n{data_frame_squirrel_count}\n\nSaving to \"squirrel_count.csv\"\n")
data_frame_squirrel_count.to_csv("squirrel_count.csv")

# Check data when we import saved csv from pandas
squirrel_count_csv = pandas.read_csv("squirrel_count.csv")
print(f"\"squirrel_count.csv\" file saved as:\n{squirrel_count_csv}")
