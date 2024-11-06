"""
This is a simulation problem that determines if a robot returns to its starting position.
The robot can move in 4 directions:
- R: Right (increases horizontal position by 1)
- L: Left (decreases horizontal position by 1) 
- U: Up (increases vertical position by 1)
- D: Down (decreases vertical position by 1)

The function returns True if the robot ends up at the origin (0,0) after all moves.
False otherwise.

Time complexity: O(n) where n is the length of the moves string
Space complexity: O(1) since we only store 2 integers
"""


def judgeCircle(moves: str) -> bool:
    horizontal_position = 0
    vertical_position = 0

    for move in moves:
        if move == "R":
            horizontal_position += 1
        elif move == "L":
            horizontal_position -= 1
        elif move == "U":
            vertical_position += 1
        elif move == "D":
            vertical_position -= 1
            
    return horizontal_position == 0 and vertical_position == 0

print(judgeCircle("RRUDURLLDDURR"))
print(judgeCircle("RRLLUUDD"))