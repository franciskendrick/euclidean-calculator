# Euclidean Calculator

## Overview

**Euclidean Calculator** is a Python-based computational tool and interactive web application designed to evaluate number-theoretic properties for sets of integers. The application computes the Greatest Common Divisor (GCD) and Least Common Multiple (LCM), and provides mathematical proofs via linear combinations (Bézout's identity) and step-by-step Euclidean division.

You can access the interactive web interface here: **[Euclidean Calculator Web Application](https://euclidean-calculator.streamlit.app/)**

### Evaluation Models

The application is structured into three distinct execution models to serve different levels of mathematical depth:

* **Core (`nt_core.py`):** Optimized for direct computation. It calculates raw GCD and LCM values across multiple integers using Python's C-optimized standard `math` module (`math.gcd` and `math.lcm`).
* **Combi (`nt_combi.py`):** Focuses on structural relations. In addition to computing GCD and LCM, it evaluates Bézout's identity to express the GCD as a linear combination of two integers:

$$\gcd(a, b) = a(x) + b(y)$$


* **Omni (`nt_omni.py`):** Built for full algorithmic transparency and academic proof generation. It provides complete step-by-step Euclidean division tables, line-by-line backward substitution proofs to derive Bézout coefficients (for two numbers), and step-by-step associative LCM derivations across arbitrary $n \ge 2$ inputs.

## Context

This project was created as an assessment requirement for **Number Theory** at [De La Salle University - Dasmariñas](https://www.dlsud.edu.ph/).

The program demonstrates key foundational concepts in number theory and algorithm design:

* **The Division Algorithm & Euclidean Algorithm:** Computing GCD via successive division steps $a = qb + r$.
* **Extended Euclidean Algorithm & Bézout's Identity:** Reversing division steps through backward substitution to compute integer coefficients $x$ and $y$.
* **Fundamental Relation of GCD and LCM:** Deriving least common multiples through pairwise GCD reductions:

$$\text{LCM}(a, b) = \frac{\vert{}a \cdot b\vert{}}{\gcd(a, b)}$$


* **Associative Multi-Variable Reduction:** Iteratively finding the GCD and LCM for $n > 2$ integers via successive pairwise evaluations:

$$\gcd(a_1, a_2, \dots, a_n) = \gcd(\gcd(a_1, a_2), \dots, a_n)$$

## Requirements & Setup

### Prerequisites

* **Python Version:** Python 3.12 or higher
* **External Dependencies:** `streamlit` (required for web UI)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/franciskendrick/euclidean-calculator.git
cd euclidean-calculator
```

2. Install required packages:

```bash
pip install streamlit
```

### How to Run

* Terminal / CLI Mode

```bash
python main.py
```

* Streamlit Web Application Mode

```bash
streamlit run app.py
```