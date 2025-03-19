Count Vowels in a String & Return in Reverse Order
def count_vowels_reverse(s):
    vowels = "aeiouAEIOU"
    extracted_vowels = [char for char in s if char in vowels]
    return len(extracted_vowels), extracted_vowels[::-1]

# Example usage
string = "Hello World"
count, reversed_vowels = count_vowels_reverse(string)
print("Vowel Count:", count)
print("Reversed Vowels:", reversed_vowels)

