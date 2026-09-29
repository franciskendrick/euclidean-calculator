import math

def solve_number_theory(num1, num2):
    # Ensure a >= b for standard presentation
    a, b = max(abs(num1), abs(num2)), min(abs(num1), abs(num2))
    
    # 1. Track Euclidean Algorithm steps: (a, b, quotient, remainder)
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
        gcd_val = steps[-2][3]  # Last non-zero remainder

    # Formula for LCM
    lcm_val = (a * b) // gcd_val

    # Verification using math module (as requested)
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
        # Base Case: b divides a directly
        x_final, y_final = 0, 1
        print(f"{gcd_val} = {a}(0) + {b}(1)")
        print(f"\nTherefore:\n{gcd_val} = {a}(0) + {b}(1)\n")
    else:
        # General Case: Dynamic Backward Substitution
        last_step = nz_steps[-1]
        
        # Terms tracked as [coefficient, base_number]
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

        # Line 1: Express last non-zero remainder
        print(f"{gcd_val} = {format_terms(terms)}")

        # Step back through remainders iteratively
        for i in range(len(nz_steps) - 2, -1, -1):
            sub_step = nz_steps[i]
            sub_val, sub_a, sub_b, sub_q = sub_step[3], sub_step[0], sub_step[1], sub_step[2]

            # Line 2: Substitute remainder expression
            print(f"{gcd_val} = {format_sub(terms, sub_val, sub_a, sub_q, sub_b)}")

            # Expand terms
            expanded_terms = []
            for c, v in terms:
                if v == sub_val:
                    expanded_terms.append([c, sub_a])
                    expanded_terms.append([-c * sub_q, sub_b])
                else:
                    expanded_terms.append([c, v])
            
            # Line 3: Show expanded product
            print(f"{gcd_val} = {format_terms(expanded_terms)}")

            # Combine like terms
            combined_dict = {}
            for c, v in expanded_terms:
                combined_dict[v] = combined_dict.get(v, 0) + c
            
            terms = [[c, v] for v, c in combined_dict.items() if c != 0]
            
            # Line 4: Combined simplified line
            print(f"{gcd_val} = {format_terms(terms)}")

        # Extract final Bézout coefficients for a and b
        x_final = sum(c for c, v in terms if v == a)
        y_final = sum(c for c, v in terms if v == b)

        print(f"\nTherefore:\n{gcd_val} = {a}({x_final}) + {b}({y_final})\n")

    print(f"The LCM is: {lcm_val}")


if __name__ == "__main__":
    user_input = input("Input your Numbers: ")
    numbers = [int(num.strip()) for num in user_input.split()]

    if len(numbers) == 2:
        solve_number_theory(numbers[0], numbers[1])

    elif len(numbers) > 2:
        # Standard multi-number evaluation using built-in math module
        gcd_val = math.gcd(*numbers)
        lcm_val = math.lcm(*numbers)
        
        print(f"\nThe GCD is: {gcd_val}")
        print(f"The LCM is: {lcm_val}")
        
    else:
        print("Enter at least two numbers.")