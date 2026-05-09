import pandas as pd

# 1. Load the dataset
df = pd.read_csv("movie_reviews.csv")

# 2. We are going to create a BRAND NEW column in our spreadsheet called "clean_review".
# We do this by taking the original "review" column, and applying .str.lower() to all rows at once!
df["clean_review"] = df["review"].str.lower()

# 3. Now let's remove the punctuation from our new column.
# We add regex=False just to tell Pandas we are doing a simple, basic text replacement.
df["clean_review"] = df["clean_review"].str.replace(",","")
df["clean_review"] = df["clean_review"].str.replace("!","")
df["clean_review"] = df["clean_review"].str.replace(".","")

# 4. Let's look at our spreadsheet now! 
# We ask Pandas to show us just the original review and the clean review columns.
print("--- After Preprocessing ---")
print(df[["review", "clean_review"]].head())