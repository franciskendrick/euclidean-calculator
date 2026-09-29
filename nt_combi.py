import math

def linear_combination_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Recursive Extended Euclidean Algorithm.
    Returns (gcd, x, y) satisfying Bézout's identity: gcd = a(x) + b(y).
    """
    if b == 0:
        return a, 1, 0
    
    gcd_val, x1, y1 = linear_combination_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_val, x, y

def run_combi(numbers: list[int]) -> None:
    """Calculates GCD, LCM, and prints the Bézout coefficient linear combination."""
    if len(numbers) < 2:
        print("Error: Please provide at least two numbers.")
        return

    if len(numbers) == 2:
        a, b = numbers[0], numbers[1]
        gcd_val, x, y = linear_combination_gcd(a, b)
        
        # Ensure GCD output is strictly positive for presentation
        if gcd_val < 0:
            gcd_val, x, y = -gcd_val, -x, -y
            
        lcm_val = abs(a * b) // gcd_val if gcd_val != 0 else 0

        print(f"\nThe GCD is: {gcd_val}")
        print(f"The LCM is: {lcm_val}")
        print("Linear Combination:")
        print(f"({a}, {b}) = {a}({x}) + {b}({y})")
        
    else:
        gcd_val = math.gcd(*numbers)
        lcm_val = math.lcm(*numbers)
        print(f"\nThe GCD is: {gcd_val}")
        print(f"The LCM is: {lcm_val}")
        print("\n[Note: Linear combination is formatted for exactly 2 numbers.]")

if __name__ == "__main__":
    user_input = input("Input your Numbers: ")
    try:
        nums = [int(n.strip()) for n in user_input.split()]
        run_combi(nums)
    except ValueError:
        print("Error: Invalid input. Please enter space-separated integers.")