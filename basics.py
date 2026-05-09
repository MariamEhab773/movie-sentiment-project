import pandas as pd
# 1. Import our new heavy machinery!
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

# 2. Load and clean our data (just like we did last time)
df = pd.read_csv("movie_reviews.csv")
df["clean_review"] = df["review"].str.lower()
df["clean_review"] = df["review"].str.replace(",","")
df["clean_review"] = df["review"].str.replace("!","")
df["clean_review"] = df["review"].str.replace(".","")

# 3. Create our Assistant (The Vectorizer)
# max_tokens=100 means we only want to remember the top 100 most common words.
# output_mode="int" means we want integer numbers back.
vectorizer = TextVectorization(max_tokens=100, output_mode="int")

# 4. "Adapt": Tell the assistant to read our dataset and build the phonebook!
vectorizer.adapt(df["clean_review"])

# 5. Let's look at the phonebook it built.
vocab = vectorizer.get_vocabulary()
print("--- The AI Phonebook ---")
print(vocab)

# 6. The Magic Translation! Let's translate a sentence into numbers.
test_sentence = "i loved this movie"
numbers = vectorizer(test_sentence)

print("\n--- Translation ---")
print(f"Original: {test_sentence}")
print(f"AI Numbers: {numbers}")