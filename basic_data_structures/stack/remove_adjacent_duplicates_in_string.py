def remove_adjacent_duplicates_in_string(s: list[str]) -> str:
    stack: list[str] = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)
    

if __name__ == "__main__":
    s = input()
    res = remove_adjacent_duplicates_in_string(s)
    print(res)
    
"""
Remove Adjacent Duplicates in String
Given a string s, repeatedly remove all adjacent duplicate characters until no more duplicates can be removed. Return the final string after all removals.

When you remove a pair of adjacent duplicates, the remaining characters on both sides may become adjacent and form new duplicates that also need to be removed.

Input
s: a string containing lowercase English letters
Output
A string with all adjacent duplicates removed

Examples
Example 1:
Input: s = "abbaca"

Output: "ca"

Explanation:

Remove "bb": "abbaca" becomes "aaca"
Remove "aa": "aaca" becomes "ca"
No more adjacent duplicates, return "ca"
Example 2:
Input: s = "azxxzy"

Output: "ay"

Explanation:

Remove "xx": "azxxzy" becomes "azzy"
Remove "zz": "azzy" becomes "ay"
No more adjacent duplicates, return "ay"
Example 3:
Input: s = "abcd"

Output: "abcd"

Explanation: No adjacent duplicate characters exist.
"""
