def third_and_last_largest(arr):
    unique_sorted = sorted(set(arr), reverse=True)  # Remove duplicates & sort
    third_largest = unique_sorted[2] if len(unique_sorted) >= 3 else None
    last_largest = unique_sorted[-1]
    return third_largest, last_largest

# Example usage
numbers = [10, 5, 8, 20, 15, 20, 25, 10]
third, last = third_and_last_largest(numbers)
print("Third Largest:", third)
print("Last Largest:", last)
