import sys
from nt_core import run_core
from nt_combi import run_combi
from nt_omni import run_omni

def get_user_numbers() -> list[int]:
    """Prompts and validates integer inputs from the user."""
    while True:
        user_input = input("Input your Numbers: ").strip()
        if not user_input:
            print("Error: Input cannot be empty. Try again.\n")
            continue
        try:
            numbers = [int(n) for n in user_input.split()]
            if len(numbers) < 2:
                print("Error: Please enter at least two integers.\n")
                continue
            return numbers
        except ValueError:
            print("Error: Invalid input. Please enter space-separated integers only.\n")

def main():
    while True:
        print("\n==========================================")
        print("    NUMBER THEORY ASSESSMENT ENGINE       ")
        print("==========================================")
        print("Select Model Version:")
        print("  [1] NT-Core  (Fast built-in GCD & LCM)")
        print("  [2] NT-Combi (GCD, LCM & Linear Combination)")
        print("  [3] NT-Omni  (Full Step-by-Step Proof & Derivation)")
        print("  [4] Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            print("\n--- Running NT-Core ---")
            numbers = get_user_numbers()
            run_core(numbers)
        elif choice == "2":
            print("\n--- Running NT-Combi ---")
            numbers = get_user_numbers()
            run_combi(numbers)
        elif choice == "3":
            print("\n--- Running NT-Omni ---")
            numbers = get_user_numbers()
            run_omni(numbers)
        elif choice == "4":
            print("\nExiting engine. Good luck with your assessment!")
            sys.exit(0)
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()