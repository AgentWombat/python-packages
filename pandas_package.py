import pandas as pd

# The "DataFrame" object is the meat and potatoes of Pandas.
# It holds rows of data, each of which can have numerous coloumns. 
# "dtype" defines what kind of data is stored in the table. In addition to "int", it can also be "float" or "float32"
df = pd.DataFrame(data=[[1,2,3,4],[2,3,4,5], [90,80,70,60]], columns=["First", "Second", "Third", "Fourth"], dtype = "int")


print(df)

# We can access a single column:
print("--COLUMN--")
print(df["First"])

print("The second entree in the First column is", df['First'][1])

# To get a normal array out of a dataframe we can use the built-in "list" function.

df_second_column_list = list(df['Second'])

print("The second column has values", df_second_column_list)


# Where Pandas really shines is in its ability to parse and read data in CSV formats.
df = pd.read_csv("data.csv")
print(df)

# This is all for which I really use Pandas. After reading a csv file, I will
# convert it into either a Python or Numpy array.