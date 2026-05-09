import pandas as pd

# 1. We use pd.read_csv() to load our external file into a DataFrame
df = pd.read_csv("movie_reviews.csv")

# 2. When dealing with thousands of rows, we don't want to print them all!
# The .head() command tells Pandas to only print the first 5 rows so we can take a peek.
print("--- Peeking at our Dataset ---")
print(df.head())

# 3. We can also ask Pandas how many rows and columns are in the file using .shape
print("\n--- Dataset Size ---")
print("Rows and Columns:", df.shape)