# 1. We must 'import' pandas to tell Python we want to use the tool we just downloaded.
# We call it 'pd' for short so we don't have to type 'pandas' every time.
import pandas as pd

# 2. Let's create some fake movie review data. 
# Notice how we use a Dictionary, but this time the Values are Lists!
fake_data = {
    "Review": ["I loved this movie!", "It was terrible.", "Great acting!"],
    "Sentiment": ["Positive", "Negative", "Positive"]
}

# 3. We use Pandas (pd) to convert our dictionary into a DataFrame (spreadsheet)
# We usually name our DataFrame 'df' for short.
df = pd.DataFrame(fake_data)

# 4. Print the spreadsheet to the terminal
print("--- My First Pandas Spreadsheet ---")
print(df)