def sort_by_frequency(s: str) -> str:
    sorted_s = sorted(s, key=lambda x: (-s.count(x), x))
    return "".join(sorted_s)

if __name__ == "__main__":
    s = input()
    res = sort_by_frequency(s)
    print(res)
    

"""
Sort Characters by Frequency
Problem Description
Given a string, return a new string with characters sorted by their frequency. Characters that appear more frequently should come first. When two characters have the same frequency, sort them alphabetically.

Input: A string containing any characters

Output: A string with characters sorted by frequency (descending), with ties broken alphabetically (ascending)

Examples:

Input: "tree"
Output: "eert"
Explanation: 'e' appears twice, 'r' and 't' appear once each.
             Result: "ee" + "rt" (alphabetically sorted)

Input: "cccaaa"
Output: "aaaccc"
Explanation: Both 'a' and 'c' appear 3 times.
             Since 'a' < 'c' alphabetically, 'a' comes first.

Input: "Aabb"
Output: "bbAa"
Explanation: 'b' appears twice, 'A' and 'a' appear once each.
             Result: "bb" + "Aa" (alphabetically sorted by character code)
"""