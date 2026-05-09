# 1. Our Sentiment Dictionary (The "Brain")
word_scores = {
    "loved": 1,
    "great": 1,
    "terrible": -1,
    "bad": -1,
    "awesome": 1
}

# 2. The raw data
review = "I absolutely loved this movie, the acting was great!"

# 3. Preprocessing (Lowercasing and removing punctuation)
clean_review = review.lower().replace(",","").replace("!","")

# 4. Tokenization (Splitting into a list of words)
tokens = clean_review.split()

# 5. Set our starting score to zero
total_score = 0

# 6. The Loop (Our grading system)
for word in tokens:
    
    # Check if the word exists in our dictionary
    if word in word_scores:
        
        # Look up the score for that word
        score = word_scores[word]
        
        # Add it to our running total!
        total_score += score

# 7. Print the final results
print("Review:", review)
print("Final Sentiment Score:", total_score)

# Optional logic to determine the final verdict:
if total_score > 0:
    print("Verdict: Positive")
elif total_score < 0:
    print("Verdict: Negative")
else:
    print("Verdict: Neutral")
        