"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = sorted([float(value) for value in input().split(",")])
        median = ((numbers[len(numbers) // 2] + numbers[(len(numbers) // 2) - 1])) / 2 if len(numbers) % 2 == 0 else numbers[(len(numbers) // 2)]
        if (len(numbers) % 2 == 0):
            print((numbers[len(numbers) // 2], numbers[(len(numbers) // 2) + 1]))
        print(median)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
