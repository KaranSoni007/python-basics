# Series :

- 1D labelled array that can hold any data type. It is like a single column in a spreadsheet.

# Dataframe :

- A 2D tabular data structure with rows and columns similar to an Excel spreadsheet.

# Commands for file imports :

- df = pd.read_csv("Name of file")
- df = pd.read_excel("Name of file")
- df = pd.read_json("Name of file")

# Aggregate functions :

- Reduces a set of values into a single summary value
- Used to summarize and analyze data
- Often used with the groupby() function

# Data Cleaning :

- The process of fixing/removing incomplete, incorrect or irrelevant data.

df = df.dropna()
df = df.fillna()
df = df.to_string()
df = df.drop_duplicates()