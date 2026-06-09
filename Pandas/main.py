import pandas as pd

# Part 1 : Series

data = [100.1, True, 300, "A"]

series = pd.Series(data, index=["a", "b", "c", "d"])

print(series)
series.loc["a"] = 100
series.loc["b"] = 200
series.loc["d"] = 400
print(series)

# Part 2 : Dataframe

data_df = {
    "Name" : ["ABC", "PQR", "XYZ"],
    "Age" : [30, 35, 40],
    "Designation" : ["Developer", "HR", "Manager"]
}

df = pd.DataFrame(data_df)
print(df)
# print(df.loc[0])

# Part 3 : Aggregate functions

df = pd.read_csv("Smartphones_cleaned_dataset.csv")

print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count(numeric_only=True))

print("Mean : ", df["Price"].mean(numeric_only=True))
print("Sum : ", df.sum(numeric_only=True))
print("Min : ",df.min(numeric_only=True))
print("Max : ", df.max(numeric_only=True))
print("Count : ", df["has_5g"].count())