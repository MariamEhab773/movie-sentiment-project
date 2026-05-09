# 1. Our original review with punctuation
review = "I absolutely loved this movie, the acting was great!"

clean_review = review.lower()

clean_review = clean_review.replace(",","").replace("!","")

tokens = clean_review.split()

print("Cleaned Tokens: ", tokens)