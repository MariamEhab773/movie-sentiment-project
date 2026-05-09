# 1. We create a DICTIONARY using curly braces { }
# Key = The Word, Value = A sentiment score we make up!
# Positive words get a 1, negative get a -1, neutral get a 0.
word_scores = {
    "loved": 1,
    "great": 1,
    "terrible": -1,
    "movie": 0
}

# 2. Let's look up the score for a specific word. 
# We type the dictionary name, and put the Key in square brackets.
loved_score = word_scores["loved"]
terrible_score = word_scores["terrible"]

# 3. Print the results to the terminal
print("The score for 'loved' is:", loved_score)
print("The score for 'terrible' is:", terrible_score)