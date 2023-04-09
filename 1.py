import random

# Generate a list of 10 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(10)]

# Find the maximum value in the list
max_value = max(numbers)

print(f"The maximum value is {max_value}")
print(f"The list of random numbers is {numbers}")