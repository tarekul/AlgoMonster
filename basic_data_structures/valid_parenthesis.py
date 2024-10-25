def valid_parenthesis(s):
    stack = []
    parenthesis_map = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if parenthesis_map[char] != top:
                return False
    return not stack

print(valid_parenthesis("(){}[]"))