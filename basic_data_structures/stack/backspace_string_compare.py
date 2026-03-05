def backspace_string_compare(s, t):
    stack_s = []
    stack_t = []
    
    for char in s:
        if char == '#':
            if stack_s:
                stack_s.pop()
        else:
            stack_s.append(char)
    
    for char in t:
        if char == '#':
            if stack_t:
                stack_t.pop()
        else:
            stack_t.append(char)
    
    return stack_s == stack_t

if __name__ == "__main__":
    s = input()
    t = input()
    res = backspace_string_compare(s, t)
    print("true" if res else "false")

"""
Backspace String Compare
Given two strings s and t containing lowercase letters and backspace characters (represented by #), determine if they are equal after processing all backspaces. A backspace character deletes the previous character.

Input
s: a string containing lowercase letters and # characters
t: a string containing lowercase letters and # characters
Output
A boolean - true if the strings are equal after processing backspaces, false otherwise

Examples
Example 1:
Input: s = "ab#c", t = "ad#c"

Output: true

Explanation:

Process s: "ab#c" becomes "ac" (backspace removes 'b')
Process t: "ad#c" becomes "ac" (backspace removes 'd')
Both result in "ac", return true
Example 2:
Input: s = "ab##", t = "c#d#"

Output: true

Explanation:

Process s: "ab##" becomes "" (first # removes 'b', second # removes 'a')
Process t: "c#d#" becomes "" (first # removes 'c', second # removes 'd')
Both result in empty strings, return true
Example 3:
Input: s = "a#c", t = "b"

Output: false

Explanation:

Process s: "a#c" becomes "c" (backspace removes 'a')
Process t: "b" remains "b"
"c" and "b" are different, return false
"""