import math

user_input = input("Input your Numbers: ")
numbers = [int(num.strip()) for num in user_input.split(",")]  # convert the comma-separated string into a list of integers
result = math.gcd(*numbers)

print(f"The GCD is: {result}")