#!/usr/bin/env python3
"""Produce finite Padé witnesses; requires SymPy, never imported by checker.py."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix

Y = sp.Symbol('y')
CASES = [
    ('thue_morse', ['01', '10'], '0'),
    ('period_doubling', ['01', '00'], '0'),
    ('cantor', ['000', '101'], '1'),
    ('delta_plus_one', ['001', '110'], '0'),
    ('delta_minus_two', ['0111', '1000'], '0'),
    ('delta_plus_two', ['0001', '1110'], '0'),
]

def make_case(name: str, images: list[str], start: str) -> dict:
    word = start
    while len(word) < 128:
        word = ''.join(images[int(c)] for c in word)
    word = word[:128]
    s = 0
    f = []
    for b in word:
        f.append(Y**s if b == '1' else sp.S.Zero)
        s += int(b)
    # Eliminate coefficients z^7,...,z^12; P cancels degrees 0,...,6.
    rows = [[f[n-j] for j in range(7)] for n in range(7, 13)]
    basis = DomainMatrix.from_list_sympy(6, 7, rows).to_field().nullspace().to_Matrix()
    q = [sp.cancel(x) for x in list(basis.row(0))]
    p = [-sum(q[j]*f[n-j] for j in range(n+1)) for n in range(7)]
    denominator = sp.lcm([sp.denom(sp.cancel(x)) for x in p+q])
    values = [sp.Poly(sp.cancel(x*denominator), Y, domain=sp.QQ) for x in p+q]
    common = values[0]
    for value in values[1:]:
        common = sp.gcd(common, value)
    values = [v.exquo(common) for v in values]
    scale = sp.ilcm(*[int(c.q) for v in values for c in v.all_coeffs()])
    values = [sp.Poly(v.as_expr()*scale, Y, domain=sp.ZZ) for v in values]
    content = sp.igcd(*[int(c) for v in values for c in v.all_coeffs()])
    values = [sp.Poly(v.as_expr()/content, Y, domain=sp.ZZ) for v in values]
    first = next(v for v in values if not v.is_zero)
    if first.LC() < 0:
        values = [-v for v in values]
    pp, qq = values[:7], values[7:]
    coeffs = []
    for n in range(len(word)):
        e = pp[n].as_expr() if n < 7 else sp.S.Zero
        e += sum(qq[j].as_expr()*f[n-j] for j in range(min(n, 6)+1))
        coeffs.append(sp.Poly(e, Y, domain=sp.ZZ))
    order = next(n for n, e in enumerate(coeffs) if not e.is_zero)
    if order < 13:
        raise RuntimeError('Padé construction did not attain the required order')
    def encode(v: sp.Poly) -> list[int]:
        return list(reversed([int(c) for c in v.all_coeffs()]))
    return {'name': name, 'images': images, 'start': start, 'prefix': word,
            'P': [encode(v) for v in pp], 'Q': [encode(v) for v in qq],
            'first_nonzero': order, 'first_coefficient': encode(coeffs[order])}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = {'schema': 1, 'degree_z': 6, 'required_order': 13,
            'scope': 'Finite polynomial witnesses only; not a proof of irrationality.',
            'cases': [make_case(*case) for case in CASES]}
    args.output.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
    print(f'generated {len(data["cases"])} finite witnesses')

if __name__ == '__main__':
    main()
