#Using Dynamic Programming to match two strings that involve regular expression
def isMatch(s: str, p: str) -> bool:
    # DP table where dp[i][j] means s[:i] matches p[:j]
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True  # Empty string matches with empty pattern

    # Initialize dp for patterns like a*, a*b*, a*b*c* matching with empty string
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if p[j - 2] == s[i - 1] or p[j - 2] == '.' else False)

    return dp[len(s)][len(p)]

# Test cases
print(isMatch("aa", "a"))        # Output: False
print(isMatch("aa", "a*"))       # Output: True
print(isMatch("ab", ".*"))       # Output: True
print(isMatch("aab", "c*a*b"))   # Output: True
print(isMatch("mississippi", "mis*is*p*.")) # Output: False
