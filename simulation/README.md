### What are Simulation Problems?


Simulation problems in coding interviews involve creating a program that imitates the behavior of a system or a process. These problems require you to step through the problem scenario, maintaining the state and making decisions based on the given rules. 

In general the characteristics of a simulation problem will look like the following:


- **State Management**: Keeping track of the state of various elements in the system
- **Step-By-Step-Execution**: Iterating through each step of the process and updating the state based on the given rules.
- **Conditional Logic**: Making decisions based on the current state and conditions
- **Edge Cases Handling**: Carefully managing edge cases and unusual scenarios that can occur during the simulation.

To understand the general flow of simulation problesm we can take a look at the simple Design Parking System example.

### Problem Statement


Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size. Implement a class ParkingSystem:


- `ParkingSystem(int big, int medium, int small)` Initializes the object with the number of slots for each parking space.
- `bool addCar(int carType)` Checks whether there is a parking space available for the car of the given type (`1` for `big`, `2` for `medium`, and `3` for `small`). A car can only park in a space of its size. If there is space available, it parks in that slot and returns `true`. Otherwise, it returns `false`.

**Plan the Simulation**:


- State Management: 
	- Initialize the parking slots with the given number of slots for each car type (big, medium, small).
- Step-By-Step-Execution:
	- addCar function should update the number of slot available for carType
- Conditional Logic: 
	- On each `addCar` operation, check the type of car and the availability of the corresponding parking slot.
	- If a slot is available for the given car type, decrement the count of available slots and return `true`. This "simulates" the parking process for a car.
	- If no slots are available, return `false`.
