def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Sort the array
    strs.sort()
    
    # Compare the first and last strings in the sorted array
    first = strs[0]
    last = strs[-1]
    i = 0
    
    # Find the common prefix between the first and last string
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    
    return first[:i]


strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"

strings = ["dog", "racecar", "car"]
print(longest_common_prefix(strings))  # Output: ""

