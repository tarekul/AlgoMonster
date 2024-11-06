"""
This is a classic FizzBuzz problem that prints:
- "FizzBuzz" if a number is divisible by both 3 and 5 (i.e. divisible by 15)
- "Fizz" if a number is divisible by 3
- "Buzz" if a number is divisible by 5
- The number itself if none of the above conditions are met

Time complexity: O(n) where n is the input number
Space complexity: O(n) to store the result array
"""


def fizzBuzz(n: int):
    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result

print(fizzBuzz(20))