import re

def longest_word(sen):
    words = re.findall(r'\b\w+\b', sen)  # Extract words
    return max(words, key=len)

# Example usage
print(longest_word("The quick brown fox."))  # Expected Output: "quick"
print(longest_word("I love programming in Python!"))  # Expected Output: "programming"
