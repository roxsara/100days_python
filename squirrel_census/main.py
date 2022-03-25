import pandas

data = pandas.read_csv("squirrel_census.csv")

# Go through the df, filter for the searched fur color and count the elements of that list
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# Build a dict with the required data: fur color and count
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

# Transform the dict into a df
df = pandas.DataFrame(data_dict)

# Save df to csv file
df.to_csv("squirrel_count.csv")