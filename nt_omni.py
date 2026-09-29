import math

def solve_number_theory(num1: int, num2: int) -> None:
    """Generates explicit step-by-step Euclidean algorithm division and backward substitution."""
    a, b = max(abs(num1), abs(num2)), min(abs(num1), abs(num2))
    
    # 1. Track Euclidean Algorithm steps
    steps = []
    temp_a, temp_b = a, b
    while temp_b != 0:
        q = temp_a // temp_b
        r = temp_a % temp_b
        steps.append((temp_a, temp_b, q, r))
        temp_a, temp_b = temp_b, r

    # Determine GCD value
    if len(steps) == 1 and steps[0][3] == 0:
        gcd_val = b
    else:
        gcd_val = steps[-2][3]

    lcm_val = (a * b) // gcd_val

    # Standard verification check
    assert gcd_val == math.gcd(a, b), "GCD calculation mismatch!"
    assert lcm_val == math.lcm(a, b), "LCM calculation mismatch!"

    # 2. Print GCD Solution
    print("\nGCD Solution:")
    for step_a, step_b, q, r in steps:
        print(f"{step_a} = {q}({step_b}) + {r}")
    print(f"\nTherefore, GCD({a}, {b}) = {gcd_val}\n")

    # 3. Print Linear Combination Solution
    print("Linear Combination Solution:")
    nz_steps = [s for s in steps if s[3] != 0]

    if not nz_steps:
        print(f"{gcd_val} = {a}(0) + {b}(1)")
        print(f"\nTherefore:\n{gcd_val} = {a}(0) + {b}(1)\n")
    else:
        last_step = nz_steps[-1]
        terms = [[1, last_step[0]], [-last_step[2], last_step[1]]]
        
        def format_terms(t_list):
            parts = []
            for idx, (c, v) in enumerate(t_list):
                if c == 0:
                    continue
                if idx == 0:
                    part = f"{v}" if c == 1 else (f"-{v}" if c == -1 else f"{c}({v})")
                else:
                    sign = "+" if c > 0 else "-"
                    abs_c = abs(c)
                    part = f"{sign} {v}" if abs_c == 1 else f"{sign} {abs_c}({v})"
                parts.append(part)
            return " ".join(parts)

        def format_sub(t_list, sub_val, sub_a, sub_q, sub_b):
            sub_expr = f"({sub_a} - {sub_q}({sub_b}))" if sub_q != 1 else f"({sub_a} - {sub_b})"
            parts = []
            for idx, (c, v) in enumerate(t_list):
                if v == sub_val:
                    sign = "+" if c > 0 else "-"
                    abs_c = abs(c)
                    prefix = f"{sign} " if idx > 0 else ("-" if c < 0 else "")
                    part = f"{prefix}{sub_expr}" if abs_c == 1 else f"{prefix}{abs_c}{sub_expr}"
                else:
                    if idx == 0:
                        part = f"{v}" if c == 1 else (f"-{v}" if c == -1 else f"{c}({v})")
                    else:
                        sign = "+" if c > 0 else "-"
                        abs_c = abs(c)
                        part = f"{sign} {v}" if abs_c == 1 else f"{sign} {abs_c}({v})"
                parts.append(part)
            return " ".join(parts)

        print(f"{gcd_val} = {format_terms(terms)}")

        for i in range(len(nz_steps) - 2, -1, -1):
            sub_step = nz_steps[i]
            sub_val, sub_a, sub_b, sub_q = sub_step[3], sub_step[0], sub_step[1], sub_step[2]

            print(f"{gcd_val} = {format_sub(terms, sub_val, sub_a, sub_q, sub_b)}")

            expanded_terms = []
            for c, v in terms:
                if v == sub_val:
                    expanded_terms.append([c, sub_a])
                    expanded_terms.append([-c * sub_q, sub_b])
                else:
                    expanded_terms.append([c, v])
            
            print(f"{gcd_val} = {format_terms(expanded_terms)}")

            combined_dict = {}
            for c, v in expanded_terms:
                combined_dict[v] = combined_dict.get(v, 0) + c
            
            terms = [[c, v] for v, c in combined_dict.items() if c != 0]
            print(f"{gcd_val} = {format_terms(terms)}")

        x_final = sum(c for c, v in terms if v == a)
        y_final = sum(c for c, v in terms if v == b)

        print(f"\nTherefore:\n{gcd_val} = {a}({x_final}) + {b}({y_final})\n")

    print(f"The LCM is: {lcm_val}")

def run_omni(numbers: list[int]) -> None:
    """Executes step-by-step derivation for 2 numbers or falls back to multi-number math."""
    if len(numbers) < 2:
        print("Error: Please provide at least two numbers.")
        return

    if len(numbers) == 2:
        solve_number_theory(numbers[0], numbers[1])
    else:
        gcd_val = math.gcd(*numbers)
        lcm_val = math.lcm(*numbers)
        print(f"\nThe GCD is: {gcd_val}")
        print(f"The LCM is: {lcm_val}")
        print("\n[Note: Full step-by-step derivation is formatted for exactly 2 numbers.]")

if __name__ == "__main__":
    user_input = input("Input your Numbers: ")
    try:
        nums = [int(n.strip()) for n in user_input.split()]
        run_omni(nums)
    except ValueError:
        print("Error: Invalid input. Please enter space-separated integers.")