#!/usr/bin/env python3
"""Standard-library-only finite audit. Does not import the Padé generator.

A PASS verifies polynomial witnesses and finite identities, not the universal
irrationality theorem. That theorem is proved separately in THEORY_KO.md.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
from typing import Sequence


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def block_data(word: str) -> tuple[int, int, int]:
    require(isinstance(word, str) and bool(word) and set(word) <= {'0', '1'},
            'expected a nonempty binary word')
    b = 0
    for j, bit in enumerate(word):
        b = 3**int(bit)*b + int(bit)*2**j
    return len(word), word.count('1'), b


def center(word: str) -> Fraction:
    _, a, b = block_data(word)
    return Fraction(-b, 3**a)


def slope(word: str) -> Fraction:
    n, a, _ = block_data(word)
    return Fraction(2**n, 3**a)


def determinant(u: str, v: str) -> Fraction:
    return center(v)*(1-slope(u)) - center(u)*(1-slope(v))


def valuation2(value: Fraction | int) -> int:
    x = Fraction(value)
    require(bool(x), 'zero has no finite valuation')
    def v(n: int) -> int:
        n = abs(n)
        return (n & -n).bit_length()-1
    return v(x.numerator)-v(x.denominator)


def fixed_prefix(images: Sequence[str], start: str, length: int) -> str:
    require(len(images) == 2, 'two images required')
    for word in images:
        block_data(word)
    q = len(images[0])
    require(q >= 2 and len(images[1]) == q, 'uniform length at least two required')
    require(start in ('0', '1') and images[int(start)][0] == start,
            'substitution must be prolongable at start')
    require(isinstance(length, int) and length >= 1, 'positive prefix length required')
    # Read the base-q digits of the position, not iterated word replacement.
    out = []
    for n in range(length):
        digits = []
        while n:
            digits.append(n % q)
            n //= q
        bit = start
        for digit in reversed(digits):
            bit = images[int(bit)][digit]
        out.append(bit)
    return ''.join(out)


def trim(poly: Sequence) -> list:
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [0]


def add(p: Sequence, q: Sequence) -> list:
    out = [0]*max(len(p), len(q))
    for i, a in enumerate(p):
        out[i] += a
    for i, a in enumerate(q):
        out[i] += a
    return trim(out)


def remainder(p: Sequence, q: Sequence) -> list[Fraction]:
    p, q = trim(list(map(Fraction, p))), trim(list(map(Fraction, q)))
    require(q != [0], 'polynomial division by zero')
    while p != [0] and len(p) >= len(q):
        shift, factor = len(p)-len(q), p[-1]/q[-1]
        for j, coefficient in enumerate(q):
            p[j+shift] -= factor*coefficient
        p = trim(p)
    return p


def gcd_polys(polys: Sequence[Sequence[int]]) -> list[Fraction]:
    g = [Fraction(0)]
    for poly in polys:
        p = trim(list(map(Fraction, poly)))
        while p != [0]:
            g, p = p, remainder(g, p)
    return [x/g[-1] for x in g] if g != [0] else g


def residual_coefficients(case: dict) -> list[list[int]]:
    prefix, p, q = case['prefix'], case['P'], case['Q']
    counts = [0]
    for bit in prefix:
        counts.append(counts[-1]+int(bit))
    out = []
    for n in range(len(prefix)):
        value = list(p[n]) if n < len(p) else [0]
        for j in range(min(n+1, len(q))):
            k = n-j
            if prefix[k] == '1':
                value = add(value, [0]*counts[k]+q[j])
        out.append(trim(value))
    return out


def check_certificates(data: dict) -> dict:
    require(data.get('schema') == 1 and data.get('degree_z') == 6 and
            data.get('required_order') == 13, 'wrong certificate parameters')
    cases = data.get('cases')
    require(isinstance(cases, list) and bool(cases), 'missing cases')
    names, orders = set(), {}
    for case in cases:
        name = case['name']
        require(name not in names, 'duplicate case')
        names.add(name)
        prefix = case['prefix']
        require(prefix == fixed_prefix(case['images'], case['start'], len(prefix)),
                f'{name}: prefix differs from digit recursion')
        for key in ('P', 'Q'):
            require(isinstance(case[key], list) and len(case[key]) == 7,
                    f'{name}: degree in z must be at most six')
            for poly in case[key]:
                require(isinstance(poly, list) and bool(poly) and
                        all(type(x) is int for x in poly), 'integer polynomial required')
        require(any(trim(p) != [0] for p in case['Q']), f'{name}: Q is zero')
        require(gcd_polys(case['P']+case['Q']) == [1],
                f'{name}: common polynomial content is not one')
        residuals = residual_coefficients(case)
        require(all(p == [0] for p in residuals[:13]), f'{name}: order below 13')
        nonzero = [n for n, p in enumerate(residuals) if p != [0]]
        require(bool(nonzero), f'{name}: no finite nonzero residual witness')
        first = nonzero[0]
        require(first == case['first_nonzero'] and
                residuals[first] == case['first_coefficient'],
                f'{name}: false first residual')
        # Finite demonstrations of specializations; not aperiodicity tests.
        for eta in [Fraction(1), Fraction(1, 3), Fraction(3),
                    Fraction(2), Fraction(1, 2)]:
            require(any(sum(c*eta**j for j, c in enumerate(p)) != 0
                        for p in residuals), f'{name}: missing specialization witness')
        orders[name] = first
    return {'pade_certificates': len(cases), 'first_nonzero_orders': orders}


def audit_finite_identities() -> dict:
    pair_count = word_count = 0
    for n in range(1, 8):
        words = [''.join(bits) for bits in product('01', repeat=n)]
        centers = {}
        for word in words:
            _, a, b = block_data(word)
            expected = sum(2**j * 3**word[j+1:].count('1')
                           for j, bit in enumerate(word) if bit == '1')
            require(b == expected and 0 <= b < 3**n, 'affine numerator mismatch')
            centers[word] = Fraction(-expected, 3**a)
            word_count += 1
        for u, v in combinations(words, 2):
            first = next(i for i in range(n) if u[i] != v[i])
            require(valuation2(centers[u]-centers[v]) == first,
                    'first-difference valuation failed')
            pair_count += 1
    small_words = [''.join(bits) for n in range(1, 5) for bits in product('01', repeat=n)]
    commutators = 0
    for u, v in product(small_words, repeat=2):
        det = determinant(u, v)
        require(det == center(v+u)-center(u+v), 'commutator sign mismatch')
        require((det == 0) == (u+v == v+u), 'commuting exception mismatch')
        commutators += 1
    codings = [('0', '1'), ('110', '111'), ('0', '11'),
               ('111', '0'), ('01', '10'), ('1110', '1')]
    count_cases = 0
    for length in (2, 3):
        words = [''.join(bits) for bits in product('01', repeat=length)]
        for images in product(words, repeat=2):
            a0, a1 = [w.count('1') for w in images]
            delta = a1-a0
            blocks = ['0', '1']
            for k in range(5):
                size = length**k
                expected0 = 0 if delta == length else a0*(size-delta**k)//(length-delta)
                require([b.count('1') for b in blocks] == [expected0, expected0+delta**k],
                        'substitution count formula failed')
                for u, v in codings[:3]:
                    coded = [''.join((u, v)[int(c)] for c in b) for b in blocks]
                    require(len(coded[1])-len(coded[0]) == (len(v)-len(u))*delta**k,
                            'length difference formula failed')
                    require(coded[1].count('1')-coded[0].count('1') ==
                            (v.count('1')-u.count('1'))*delta**k,
                            'odd-count difference formula failed')
                    count_cases += 1
                blocks = [''.join(images[int(c)] for c in b) for b in blocks]
    controls = [(['01', '10'], '0'), (['01', '00'], '0'), (['000', '101'], '1'),
                (['001', '110'], '0'), (['0111', '1000'], '0'), (['0001', '1110'], '0')]
    macro_cases = 0
    for images, start in controls:
        control = fixed_prefix(images, start, 12)
        blocks = ['0', '1']
        for k in range(4):
            for coding in codings:
                u, v = [''.join(coding[int(c)] for c in b) for b in blocks]
                z, lam1 = slope(u), slope(v)
                y = lam1/z
                c0, c1 = center(u), center(v)
                det = determinant(u, v)
                require(det != 0, 'noncommuting macro blocks lost injectivity')
                f = g = Fraction(0)
                weight = Fraction(1)
                for bit in control:
                    g += weight
                    if bit == '1':
                        f += weight
                    weight *= z if bit == '0' else lam1
                xi = center(''.join((u, v)[int(c)] for c in control))
                require(xi == c0*g+(c1-c0)*f, 'finite inverse regrouping failed')
                require((1-z)*g == 1-weight+z*(y-1)*f, 'finite boundary term failed')
                require(((1-z)*xi-c0*(1-weight))/det == f,
                        'finite rational representation failed')
                macro_cases += 1
            blocks = [''.join(images[int(c)] for c in b) for b in blocks]
    require(2**13 > 3**8 and 2**11 <= 3**7, 'integer height-gap test failed')
    return {'affine_words': word_count, 'first_difference_pairs': pair_count,
            'commutator_pairs': commutators, 'count_identity_cases': count_cases,
            'macro_identity_cases': macro_cases,
            'height_gap_integer': 2**13-3**8}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path,
                        default=Path(__file__).with_name('certificates.json'))
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text(encoding='utf-8'))
    result = {'status': 'PASS', 'scope': 'finite exact checks only',
              **check_certificates(data), **audit_finite_identities()}
    text = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.report:
        args.report.write_text(text, encoding='utf-8')
    print(text, end='')

if __name__ == '__main__':
    main()
