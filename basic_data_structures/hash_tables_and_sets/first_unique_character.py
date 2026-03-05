def first_unique_character(s):
    char_count: dict[str, int] = {}
    
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    
    for i, c in enumerate(s):
        if char_count[c] == 1:
            return i
    
    return -1

if __name__ == "__main__":
    s = input()
    res = first_unique_character(s)
    print(res)
    
"""
First Unique Character
Given a string s, return the index of the first non-repeating character. If you can't find a non-repeating character, return -1.

Example 1
Input

s = "leetcode"
Output

0

Example 2
Input

s = "aaab"
Output

-1
"""