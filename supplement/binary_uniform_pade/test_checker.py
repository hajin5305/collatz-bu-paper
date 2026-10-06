"""Regression and rejection tests for the independent checker."""
import copy
import json
from fractions import Fraction
from pathlib import Path
import unittest
import checker

HERE = Path(__file__).resolve().parent

class ExactTests(unittest.TestCase):
    def test_affine_block_recurrence(self):
        self.assertEqual(checker.block_data('110'), (3, 2, 5))
        self.assertEqual(checker.block_data('110111'), (6, 5, 287))

    def test_inverse_center(self):
        self.assertEqual(checker.center('10'), Fraction(-1, 3))
        self.assertEqual(checker.slope('10'), Fraction(4, 3))

    def test_invalid_words_rejected(self):
        for w in ['', '012', 'a', 10, None]:
            with self.subTest(w=w), self.assertRaises(ValueError):
                checker.block_data(w)

    def test_uniform_prefix_independent_digit_formula(self):
        self.assertEqual(checker.fixed_prefix(['01', '00'], '0', 16),
                         '0100010101000100')

    def test_invalid_substitutions_rejected(self):
        for images, start in [(['0', '11'], '0'), (['1', '0'], '0'),
                              (['01', '00'], '1'), (['01', '0x'], '0')]:
            with self.subTest(images=images), self.assertRaises(ValueError):
                checker.fixed_prefix(images, start, 16)

    def test_exact_exponent_gap(self):
        self.assertEqual(2**13 - 3**8, 1631)
        self.assertLess(2**11, 3**7)  # degree five does not meet this bound.

    def test_commuting_blocks_give_zero_determinant(self):
        self.assertEqual(checker.determinant('10', '1010'), 0)
        self.assertNotEqual(checker.determinant('110', '111'), 0)

    def test_periodic_control_is_not_excluded(self):
        u, v = '0', '1'
        xi = checker.center(u + v) / (1 - checker.slope(u + v))
        self.assertEqual(xi, 2)
        z = checker.slope(u)
        y = checker.slope(v) / z
        h = ((1-z)*xi - checker.center(u)) / checker.determinant(u, v)
        self.assertEqual(h, z/(1-z*z*y))

    def test_saved_certificates(self):
        data = json.loads((HERE/'certificates.json').read_text())
        result = checker.check_certificates(data)
        self.assertEqual(result['pade_certificates'], 6)

    def test_corrupted_pade_coefficient_rejected(self):
        data = json.loads((HERE/'certificates.json').read_text())
        bad = copy.deepcopy(data)
        bad['cases'][0]['P'][0][0] += 1
        with self.assertRaises(ValueError):
            checker.check_certificates(bad)

    def test_nonprimitive_certificate_rejected(self):
        data = json.loads((HERE/'certificates.json').read_text())
        bad = copy.deepcopy(data)
        for key in ['P', 'Q']:
            bad['cases'][0][key] = [[-p[0]] +
                [p[i-1]-p[i] for i in range(1, len(p))] + [p[-1]]
                for p in bad['cases'][0][key]]
        with self.assertRaises(ValueError):
            checker.check_certificates(bad)

    def test_false_order_rejected(self):
        data = json.loads((HERE/'certificates.json').read_text())
        bad = copy.deepcopy(data)
        bad['cases'][0]['first_nonzero'] += 1
        with self.assertRaises(ValueError):
            checker.check_certificates(bad)

    def test_changed_control_rejected(self):
        data = json.loads((HERE/'certificates.json').read_text())
        bad = copy.deepcopy(data)
        bad['cases'][0]['prefix'] = '1' + bad['cases'][0]['prefix'][1:]
        with self.assertRaises(ValueError):
            checker.check_certificates(bad)

    def test_finite_invariant_audit(self):
        result = checker.audit_finite_identities()
        self.assertGreater(result['first_difference_pairs'], 1000)
        self.assertGreater(result['macro_identity_cases'], 100)
        self.assertGreater(result['count_identity_cases'], 100)

if __name__ == '__main__':
    unittest.main()
