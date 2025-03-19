from collections import Counter

def lone_sum(a, b, c):
    counts = Counter([a, b, c])
    return sum(num for num in counts if counts[num] == 1)

# Example usage
print(lone_sum(1, 2, 3))  # Output: 6
print(lone_sum(3, 2, 3))  # Output: 2
print(lone_sum(3, 3, 3))  # Output: 0
