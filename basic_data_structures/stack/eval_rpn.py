def eval_rpn(tokens: list[str]) -> int:
    stack = []
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
            else:
                raise ValueError("Invalid RPN expression: not enough operands")
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # '/'
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]

if __name__ == "__main__":
    tokens = [input() for _ in range(int(input()))]
    res = eval_rpn(tokens)
    print(res)


"""
Evaluate Reverse Polish Notation
Given an array of strings tokens representing a valid Reverse Polish Notation (RPN) expression, evaluate it and return the result.

In Reverse Polish Notation, operators come after their operands. For example, the expression (2 + 1) * 3 in standard notation becomes 2 1 + 3 * in RPN.

The valid operators are +, -, *, and /. Division between integers truncates toward zero.

Input
tokens: an array of strings, each representing either a number or an operator (+, -, *, /)
Output
An integer representing the result of evaluating the RPN expression

Examples
Example 1:
Input: tokens = ["2", "1", "+", "3", "*"]

Output: 9

Explanation:

This represents: (2 + 1) * 3
Step 1: 2 + 1 = 3
Step 2: 3 * 3 = 9
Result: 9
Example 2:
Input: tokens = ["4", "13", "5", "/", "+"]

Output: 6

Explanation:

This represents: 4 + (13 / 5)
Step 1: 13 / 5 = 2 (integer division)
Step 2: 4 + 2 = 6
Result: 6
Example 3:
Input: tokens = ["10", "6", "9", "3", "/", "-", "*", "17", "+", "5", "+"]

Output: 52

Explanation:

This represents: ((10 * (6 - (9 / 3))) + 17) + 5
Step 1: 9 / 3 = 3
Step 2: 6 - 3 = 3
Step 3: 10 * 3 = 30
Step 4: 30 + 17 = 47
Step 5: 47 + 5 = 52
"""