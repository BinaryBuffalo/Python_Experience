#   Author: Baked Binary
#   Creates 3 lists That all have great functions

import time #sleep function
#   Prints a list of a range of numbers from 1 to 10
numbers = list(range(1, 21))
print(f"Max -> {max(numbers)}")
print(f"Min -> {min(numbers)}")
print(f"Sum -> {sum(numbers)}")
time.sleep(3.0)
#   Prints digits in the list of numbers
for digit in numbers:
    print(digit)
    time.sleep(0.13)
# Creates a list named odds & prints a range of numbers
odds = range(3, 33, 3)
print(f"Max -> {max(odds)}")
print(f"Min -> {min(odds)}")
print(f"Sum -> {sum(odds)}")
time.sleep(3.0)
#prints the value in the list of odds
for value in odds:
    print(value)
    time.sleep(0.12)
print("Cubed List 1 -> 10")
#Takes a range of numbers too the power of 3 To find the cube 
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)
i = 0
for sovv in cubes:
    i += 1
    time.sleep(0.11)
    print(f"Cube #{i} -> ({sovv})")