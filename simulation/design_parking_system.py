"""
This is a parking system that keeps track of available spots for different car sizes.
The car types are:
1 = big
2 = medium 
3 = small

The system initializes with a fixed number of spots for each size.
When adding a car, it checks if there is an available spot of that size.
If a spot is available, it decrements the count and returns True.
If no spot is available, it returns False.

Time complexity: O(1) for both initialization and adding cars
Space complexity: O(1) since we only store 4 integers
"""



class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.cnt = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.cnt[carType] == 0:
            return False
        else:
            self.cnt[carType] -= 1
            return True

garage = ParkingSystem(3,5,8)
print(garage.addCar(2))
print(garage.addCar(3))
print(garage.addCar(3))
print(garage.addCar(1))
print(garage.addCar(1))
print(garage.addCar(1))
print(garage.addCar(1))