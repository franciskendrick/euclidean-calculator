import math

def linear_combination_gcd(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = linear_combination_gcd(b, a % b)
    
    # Update coefficients using results of recursive call
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y


# Get input from user
user_input = input("Input your Numbers: ")
numbers = [int(num.strip()) for num in user_input.split()]

# Calculate the input
if len(numbers) == 2:
    a, b = numbers[0], numbers[1]
    gcd_val, x, y = linear_combination_gcd(a, b)
    lcm_val = abs(a * b) // gcd_val  # LCM formula using GCD

    print(f"\nThe GCD is: {gcd_val}")
    print(f"The LCM is: {lcm_val}")
    print(f"Linear Combination:")
    print(f"({a}, {b}) = {a}({x}) + {b}({y})")
    
elif len(numbers) > 2:
    gcd_val = math.gcd(*numbers)
    lcm_val = math.lcm(*numbers)
    
    print(f"\nThe GCD is: {gcd_val}")
    print(f"The LCM is: {lcm_val}")
    
else:
    print("Enter at least two numbers.")