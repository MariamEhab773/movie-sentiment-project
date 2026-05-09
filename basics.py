# 1. Our original review with punctuation
review = "I absolutely loved this movie, the acting was great!"

clean_review = review.lower()

clean_review = clean_review.replace(",","").replace("!","")

tokens = clean_review.split()

print("Cleaned Tokens: ", tokens)

stop_words = ['i', 'this', 'the', 'was']

important_words = []

for word in tokens:
    
    if word not in stop_words:
        important_words.append(word)
        
print("Original Tokens: ", tokens)
print("Important Words Only: ", important_words)