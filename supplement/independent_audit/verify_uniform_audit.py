"""Exact supplemental checks for a mathematical audit; no remote mutations."""

from fractions import Fraction
import json
from pathlib import Path
import sympy as S


def verify_pade():
    y, z = S.symbols("y z")
    examples = {
        "period_doubling": ("01", "00", "0"),
        "cantor": ("000", "101", "1"),
        "thue_morse": ("01", "10", "0"),
    }
    results = {}
    for name, (a, b, word) in examples.items():
        while len(word) < 80:
            word = "".join((a, b)[int(bit)] for bit in word)
        ones, coefficients = 0, []
        for bit in word:
            coefficients.append(int(bit) * y**ones)
            ones += int(bit)
        matrix = S.Matrix([
            [int(n == i) for i in range(7)]
            + [coefficients[n - i] if n >= i else 0 for i in range(7)]
            for n in range(13)
        ])
        vector = [S.cancel(value) for value in matrix.nullspace()[0]]
        denominator = S.lcm([S.denom(value) for value in vector])
        vector = [S.cancel(denominator * value) for value in vector]
        common = S.gcd_list(vector)
        vector = [S.cancel(value / common) for value in vector]
        assert S.gcd_list(vector) == 1
        assert any(value != 0 for value in vector[7:])
        P = S.expand(sum(vector[i] * z**i for i in range(7)))
        Q = S.expand(sum(vector[7 + i] * z**i for i in range(7)))
        E = [S.expand(
            (vector[n] if n < 7 else 0)
            + sum(vector[7 + i] * coefficients[n - i]
                  for i in range(7) if n >= i)
        ) for n in range(40)]
        assert all(value == 0 for value in E[:13])
        first = next(i for i, value in enumerate(E) if value != 0)
        degree = max(S.degree(value, y) if value != 0 else 0 for value in vector)
        result = {
            "matrix_rank": matrix.rank(),
            "z_degree_limit": 6,
            "cancelled_orders": 13,
            "first_nonzero_order": first,
            "first_coefficient": str(E[first]),
            "y_degree_bound": int(degree),
            "P": str(P),
            "Q": str(Q),
        }
        results[name] = result
    return results


def verify_pseudo_trajectory(steps=2000):
    x = Fraction(-3)
    word, states = [], []
    B, ones = 0, 0
    for n in range(steps):
        states.append(x)
        if n > 0:
            assert Fraction(-5, 2) <= x < -1
            assert x.denominator == 2**n
            assert x.numerator % 2
        bit = int(x > -2)
        word.append(bit)
        B = 3**bit * B + bit * 2**n
        ones += bit
        x = x / 2 if bit == 0 else (3 * x + 1) / 2
        assert Fraction(-3) == Fraction(-B, 3**ones) + Fraction(2**(n + 1), 3**ones) * x
    assert word[0] == 0
    assert B % 2 == 0
    assert len(set(states)) == steps
    for n in range(1, steps - 4):
        if word[n] == 0:
            assert word[n + 1:n + 5] == [1] * 4
    return {
        "steps": steps,
        "initial_real_value": "-3",
        "first_instruction": word[0],
        "first_60_instructions": "".join(map(str, word[:60])),
        "one_count": ones,
        "observed_density": str(Fraction(ones, steps)),
        "proven_density_lower_bound": "4/5",
        "first_12_states": [str(value) for value in states[:12]],
        "exact_affine_identity_checked_each_step": True,
        "invariant_interval_checked": True,
        "reduced_dyadic_denominators_checked": True,
        "four_ones_after_each_noninitial_zero_checked": True,
        "finite_inverse_constant_even": True,
        "does_not_classify_final_2_adic_value": True,
    }


if __name__ == "__main__":
    output = {"pade": verify_pade(), "pseudo_trajectory": verify_pseudo_trajectory()}
    path = Path(__file__).with_name("EXACT_CHECK_RESULTS.json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))
