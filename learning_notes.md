# My NLP Learning Notes

## Python Basics
- **Variables:** Like labeled cardboard boxes for storing data. Example: `review = "Great movie!"`
- **Comments:** Lines starting with `#` are ignored by the computer. They are notes for humans.
- **Print:** The `print()` command shows data on the screen.

## Data Structures & Preprocessing
- **Lists:** Used to store multiple items in one variable using square brackets `[ ]`. Computers count starting at 0. (Example: `reviews[0]`)
- **Lowercasing:** We use `.lower()` to make all text lowercase. This is vital in NLP so the AI doesn't think "Great" and "great" are two entirely different words.

- **Tokenization:** Breaking a sentence into individual words (tokens) using `.split()`. 
- **Length:** We use `len()` to count how many items are in a List.

- **Punctuation Removal:** We use `.replace("old", "new")` to swap characters. We replaced punctuation with nothing `""` to remove it.

## Logic & Loops
- **For-Loops:** Like a conveyor belt. It goes through a list one item at a time (`for word in list:`).
- **If-Statements:** Like a bouncer. It checks a rule before letting the code continue (`if word not in stop_words:`).
- **Stop Words:** Common filler words (like "the", "is", "a") that we remove because they don't help the AI understand the meaning of the text.

## Data Structures
- **Dictionaries:** Store data in Key-Value pairs using `{ }`. We use them to map words to numerical sentiment scores (e.g., `"loved": 1`). AI needs numbers, not words!

## AI Systems
- **Rule-Based System:** An early form of AI where humans manually write the rules (like a dictionary of positive/negative words).

## Data Handling (Pandas)
- **Pandas:** A powerful Python library for handling data.
- **Importing:** We use `import pandas as pd` to bring the library into our script.
- **DataFrame (`df`):** The core of Pandas. It is basically an Excel spreadsheet inside Python, organizing data into rows and columns.
- **Loading Data:** `pd.read_csv("filename.csv")` loads a CSV file into a DataFrame.
- **Viewing Data:** `.head()` prints only the first 5 rows (great for huge datasets).
- **Dataset Size:** `.shape` outputs the number of (rows, columns).