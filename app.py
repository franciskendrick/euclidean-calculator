import io
import contextlib
import streamlit as st

from nt_core import run_core
from nt_combi import run_combi
from nt_omni import run_omni

# Page Configuration
st.set_page_config(page_title="Euclidean Calculator", page_icon="💯", layout="centered")

st.title("Euclidean Calculator")
st.write("Select a model, enter your integers, and derive step-by-step solutions.")

st.divider()

# 1. Model Selection (Buttons / Segmented Control)
st.subheader("1. Select Model")
model_choice = st.segmented_control(
    "Choose evaluation depth:",
    options=["Core", "Combi", "Omni"],
    default="Omni",
    selection_mode="single"
)

# Model Descriptions Mapping
model_descriptions = {
    "Core": "**Core**: Computes raw Greatest Common Divisor (GCD) and Least Common Multiple (LCM) using Python's C-optimized math engine.",
    "Combi": "**Combi**: Calculates GCD, LCM, and evaluates the Linear Combination: gcd(a, b) = a(x) + b(y).",
    "Omni": "**Omni**: Provides full chain-of-thought derivation, step-by-step Euclidean division tables, and line-by-line backward substitution proofs."
}

# Display dynamic description box based on selection
if model_choice in model_descriptions:
    st.info(model_descriptions[model_choice])
else:
    st.warning("Please select a model above.")

# 2. Input slot for numbers
st.subheader("2. Input Numbers")
user_input = st.text_input(
    "Enter space-separated integers:",
    value="",
    placeholder="ex. 1680 810"
)

# 3. Calculate button & 4. Output Display
st.divider()

if st.button("Calculate", type="primary", use_container_width=True):
    if not user_input.strip():
        st.error("Input cannot be empty. Please enter at least two numbers.")
    elif not model_choice:
        st.error("Please select a model before calculating.")
    else:
        try:
            # Parse inputs into a list of integers
            numbers = [int(n.strip()) for n in user_input.split()]
            
            if len(numbers) < 2:
                st.error("Please enter at least two space-separated integers.")
            else:
                # Capture print statements from calculator modules
                output_buffer = io.StringIO()
                with contextlib.redirect_stdout(output_buffer):
                    if model_choice == "Core":
                        run_core(numbers)
                    elif model_choice == "Combi":
                        run_combi(numbers)
                    elif model_choice == "Omni":
                        run_omni(numbers)
                
                result = output_buffer.getvalue()

                # Output shown below the button
                st.subheader("Output Result")
                st.code(result, language="text")

        except ValueError:
            st.error("Invalid input! Please enter space-separated integers only.")