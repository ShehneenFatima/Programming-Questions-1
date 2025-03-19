def array123(arr):
    # Check if the sequence [1, 2, 3] appears in the list
    for i in range(len(arr) - 2):
        if arr[i] == 1 and arr[i + 1] == 2 and arr[i + 2] == 3:
            return True
    return False

# Example usage
print(array123([1, 1, 2, 3, 1]))  # Output: True
print(array123([1, 1, 2, 4, 1]))  # Output: False
print(array123([1, 1, 2, 1, 2, 3]))  # Output: True
