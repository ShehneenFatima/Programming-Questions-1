from itertools import combinations

def count_divisible_by_6(s):
    count = 0
    for length in range(1, len(s) + 1):
        for sub in combinations(s, length):
            num = int("".join(sub))
            if num % 6 == 0:
                count += 1
    return count

# Example usage
print(count_divisible_by_6("1234566"))  # Expected Output: 6
