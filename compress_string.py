from collections import defaultdict

def compress_string(s):
    n = len(s)
    dp = {0: ""}
    
    for i in range(1, n + 1):
        dp[i] = s[:i]  # Start with the full substring
        for j in range(i):
            segment = s[j:i]
            count = s[:j].count(segment) + 1
            compressed = f"{count}{segment}" if count > 1 else segment
            dp[i] = min(dp[i], dp[j] + compressed, key=len)
    
    return dp[n]

# Example usage
print(compress_string("ABCABCBC"))  # Expected Output: "2ABC1BC"
print(compress_string("FLFLAFLAFLAF"))  # Expected Output: "1FLF3LAF"
