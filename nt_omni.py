import math


def run_single_euclidean(a: int, b: int, show_steps: bool = True) -> tuple[int, list, int, int]:
    """Runs Euclidean algorithm and backward substitution for two numbers."""
    abs_a, abs_b = max(abs(a), abs(b)), min(abs(a), abs(b))
    
    steps = []
    temp_a, temp_b = abs_a, abs_b
    while temp_b != 0:
        q = temp_a // temp_b
        r = temp_a % temp_b
        steps.append((temp_a, temp_b, q, r))
        temp_a, temp_b = temp_b, r

    if len(steps) == 1 and steps[0][3] == 0:
        gcd_val = abs_b
    else:
        gcd_val = steps[-2][3]

    if show_steps:
        for step_a, step_b, q, r in steps:
            print(f"{step_a} = {q}({step_b}) + {r}")

    # Backward substitution for Bézout coefficients of (abs_a, abs_b)
    nz_steps = [s for s in steps if s[3] != 0]
    if not nz_steps:
        x_final, y_final = 0, 1
    else:
        last_step = nz_steps[-1]
        terms = [[1, last_step[0]], [-last_step[2], last_step[1]]]

        for i in range(len(nz_steps) - 2, -1, -1):
            sub_step = nz_steps[i]
            sub_val, sub_a, sub_b, sub_q = sub_step[3], sub_step[0], sub_step[1], sub_step[2]

            expanded_terms = []
            for c, v in terms:
                if v == sub_val:
                    expanded_terms.append([c, sub_a])
                    expanded_terms.append([-c * sub_q, sub_b])
                else:
                    expanded_terms.append([c, v])

            combined_dict = {}
            for c, v in expanded_terms:
                combined_dict[v] = combined_dict.get(v, 0) + c

            terms = [[c, v] for v, c in combined_dict.items() if c != 0]

        x_final = sum(c for c, v in terms if v == abs_a)
        y_final = sum(c for c, v in terms if v == abs_b)

    if abs(a) < abs(b):
        x_final, y_final = y_final, x_final

    return gcd_val, steps, x_final, y_final


def solve_number_theory(numbers: list[int]) -> None:
    """Generates step-by-step Euclidean and LCM derivations for n >= 2 numbers."""
    n = len(numbers)
    
    # -------------------------------------------------------------
    # 1. GCD SOLUTION
    # -------------------------------------------------------------
    print("\nGCD Solution:")
    
    if n == 2:
        gcd_val, steps, x, y = run_single_euclidean(numbers[0], numbers[1], show_steps=True)
        print(f"\nTherefore, GCD({numbers[0]}, {numbers[1]}) = {gcd_val}\n")
        final_gcd = gcd_val
    else:
        current_gcd = numbers[0]
        for i in range(1, n):
            next_num = numbers[i]
            print(f"--- Step {i}: Finding GCD({current_gcd}, {next_num}) ---")
            gcd_val, steps, x, y = run_single_euclidean(current_gcd, next_num, show_steps=True)
            print(f"Sub-GCD: GCD({current_gcd}, {next_num}) = {gcd_val}\n")
            current_gcd = gcd_val
        
        final_gcd = current_gcd
        num_str = ", ".join(map(str, numbers))
        print(f"Therefore, GCD({num_str}) = {final_gcd}\n")

    assert final_gcd == math.gcd(*numbers), "GCD calculation mismatch!"

    # -------------------------------------------------------------
    # 2. LINEAR COMBINATION SOLUTION (Exclusively for n == 2)
    # -------------------------------------------------------------
    if n == 2:
        print("Linear Combination Solution:")
        a, b = max(abs(numbers[0]), abs(numbers[1])), min(abs(numbers[0]), abs(numbers[1]))
        gcd_val, steps, x_final, y_final = run_single_euclidean(a, b, show_steps=False)
        
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

            print(f"\nTherefore:\n{gcd_val} = {a}({x_final}) + {b}({y_final})\n")

    # -------------------------------------------------------------
    # 3. LCM SOLUTION
    # -------------------------------------------------------------
    print("LCM Solution:")
    
    if n == 2:
        current_lcm = (abs(numbers[0] * numbers[1])) // final_gcd
        print(f"LCM({numbers[0]}, {numbers[1]}) = ({abs(numbers[0])} * {abs(numbers[1])}) / {final_gcd} = {current_lcm}")
    else:
        current_lcm = abs(numbers[0])
        for i in range(1, n):
            next_num = abs(numbers[i])
            sub_gcd = math.gcd(current_lcm, next_num)
            next_lcm = (current_lcm * next_num) // sub_gcd
            print(f"Step {i}: LCM({current_lcm}, {next_num}) = ({current_lcm} * {next_num}) / {sub_gcd} = {next_lcm}")
            current_lcm = next_lcm

    assert current_lcm == math.lcm(*numbers), "LCM calculation mismatch!"
    print(f"\nThe overall LCM is: {current_lcm}")


def run_omni(numbers: list[int]) -> None:
    """Executes step-by-step derivation for 2 or more numbers."""
    if len(numbers) < 2:
        print("Error: Please provide at least two numbers.")
        return
    solve_number_theory(numbers)


if __name__ == "__main__":
    user_input = input("Input your Numbers: ")
    try:
        nums = [int(n.strip()) for n in user_input.split()]
        run_omni(nums)
    except ValueError:
        print("Error: Invalid input. Please enter space-separated integers.")