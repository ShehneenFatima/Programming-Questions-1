
def merge_vowel_arrays(arr1, arr2):
    vowels = "aeiouAEIOU"
    vowels1 = [char for char in arr1 if char in vowels]
    vowels2 = [char for char in arr2 if char in vowels]
    return vowels1 + vowels2

# Example usage
arr1 = ['a', 'b', 'e', 'x', 'o']
arr2 = ['i', 'u', 'p', 'e']
result = merge_vowel_arrays(arr1, arr2)
print("Merged Vowel Array:", result)

