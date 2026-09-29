import math

# Get input from user
user_input = input("Input your Numbers: ")
numbers = [int(num.strip()) for num in user_input.split()]

# Process the input
gcd_val = math.gcd(*numbers)
lcm_val = math.lcm(*numbers)

# Output GCD & LCM
print(f"\nThe GCD is: {gcd_val}")
print(f"The LCM is: {lcm_val}")