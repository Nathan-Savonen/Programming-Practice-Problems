
#Finding the length of the longest substring without repeating characters
def lengthOfLongestSubstring(self, s):
       #Initializing variables
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            #If we encounter a duplicate variable reduce the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            #Add the current letter to the set and increase max_length if possible
            char_set.add(s[right])
            max_length = max(max_length,right - left + 1)
        return max_length



print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3 (The substring is "abc")
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1 (The substring is "b")
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3 (The substring is "wke")
