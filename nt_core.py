import math


def run_core(numbers: list[int]) -> None:
    """Computes GCD and LCM directly using Python's standard math library."""
    if len(numbers) < 2:
        print("Error: Please provide at least two numbers.")
        return

    gcd_val = math.gcd(*numbers)
    lcm_val = math.lcm(*numbers)

    print(f"\nThe GCD is: {gcd_val}")
    print(f"The LCM is: {lcm_val}")


if __name__ == "__main__":
    user_input = input("Input your Numbers: ")
    try:
        nums = [int(n.strip()) for n in user_input.split()]
        run_core(nums)
    except ValueError:
        print("Error: Invalid input. Please enter space-separated integers.")