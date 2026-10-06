Irrationality of Collatz Parity Inverses for Block Codings of Binary Uniform Fixed Points
Supplementary material and reproduction guide

Author: Lee HaJin
Draft and supplement prepared: 2026-10-06
Research repository: hajin5305/collatz-research
Pinned commit: f751b9102355c516434ed9d0882bf4eb8608d95b
(English translation of korean/supplement_README_ko.txt; the procedure is unchanged.)

1. Purpose

This supplement reproduces, in exact integer and rational arithmetic, the finite block identities and the
explicit Padé-type certificates mentioned in the manuscript. The general irrationality conclusion of the
main theorem (Theorem BU) rests on the written proof in the manuscript. Six finite certificates and passing
checks must not be read as a proof for all substitutions, nor as a proof of the Collatz conjecture.

Original location of the main theorem:
  docs/research_records/2026-10-02/binary_uniform_pade/THEORY_KO.md
  Theorem BU and Sections 0-9

The theorem classifies when Phi(kappa(t)) is rational, for a one-sided fixed point t of a binary q-uniform
substitution (q >= 2) and nonempty binary output blocks U, V: exactly when t is ultimately periodic or
UV = VU. Primitivity of the substitution and equal length or equal number of ones of the blocks are not
required. The theorem does not cover all automatic words or general non-uniform substitutions.

2. Files and their origin

binary_uniform_pade/
  generate.py
    Generates the six finite Padé certificates by SymPy linear algebra.
    Identical to the original package file; the --output argument is required.
  checker.py
    A separate checker that does not import the generator. It checks the certificates and the finite
    identities with the standard library and Fraction arithmetic. Control prefixes are generated from the
    base-q expansion of positions, which differs from the generator's iterated substitution.
  test_checker.py
    The original 14 regression tests, covering valid cases and rejection of tampered input.
  certificates.json
    The six Padé certificates at the pinned commit.
  RESULTS.json
    The original expected results for these certificates and finite identities.

Original directory of the five files above:
  docs/research_records/2026-10-02/binary_uniform_pade/

independent_audit/
  verify_uniform_audit.py
    A separate implementation that reconstructs the Padé pairs for period-doubling, Cantor and Thue-Morse.
    It also runs the separate real pseudo-trajectory diagnostic described in Section 6.
    It has no output-file option: it writes EXACT_CHECK_RESULTS.json in its own directory, so always run
    it in a temporary copy.
  EXACT_CHECK_RESULTS.json
    The original expected results of the independent implementation.

Original directory of the two files above:
  docs/research_records/2026-10-04/literature_value_audit/uniform_review/

requirements.txt
  Installation requirement (SymPy 1.14.0) for the generator and the independent Padé check.
  checker.py and test_checker.py use only the standard library.
SOURCE_MANIFEST.json
  Repository paths and SHA-256 hashes of the seven copied original files.
  When the bundle was assembled, every file was confirmed byte-identical to the original at the pinned commit.
validation_summary.json
  Summary of the reproduction actually completed on 2026-10-06: environment, scope and agreement of results.
  The recorded execution paths are those of the preparation environment; use the relative commands below.
literature_search_log.json
  Record of the literature searches made while preparing the draft. It is neither a proof of a mathematical
  statement nor a complete survey of the literature.
literature_review.txt
  Scope of the review of related work, conditions of application, and priority of the full theorem.
  (Named literature_review_ko.txt in the first archived bundle; the content is unchanged.)
README.txt
  This guide.

3. Environment and confirmed results

Environment actually used while preparing the draft:
  Python 3.12.14
  SymPy 1.14.0

In a temporary copy of the original package the following were completed:
  - the 14 existing unit tests pass
  - generate.py regenerates the six Padé certificates
  - checker.py passes in normal mode
  - checker.py passes in -O (optimized) mode
  - verify_uniform_audit.py passes in normal mode
  - all four comparisons (original certificates; normal and optimized checker results; independent results)
    agree in JSON types and values

Exact finite scope:
  - finite block numerators and inverse-affine data: 254 binary words
  - 2-adic valuation at the first mismatch: 10,795 pairs of words
  - affine commutator identity and the commuting exception: 900 ordered pairs
    (this number includes commuting pairs, whose commutator is zero)
  - substitution coefficient identities: 1,200 cases
  - finite series identities for scaled blocks: 144 cases
    (the end terms of the finite series are kept in the check)
  - Padé certificates: 6
  - integer height gap: 2^13 - 3^8 = 1631 > 0

Names of the six control cases:
  thue_morse, period_doubling, cantor,
  delta_plus_one, delta_minus_two, delta_plus_two

Every certificate has z-degree at most 6 and cancels the 13 coefficients of z^0 through z^12. The first
nonzero term has degree 14 for Cantor and 13 for the other five. This is a finite check of concrete
approximants. The existence of an approximant for each general substitution and the nonvanishing of the
actual moving evaluations are proved separately in the manuscript.

4. Running the full finite reproduction in a temporary copy

The commands below assume bash on Linux or macOS and start inside the unpacked supplement directory.
An environment where python3 is Python 3.12 is recommended (the reproduction above used 3.12.14).
Installing packages in a new virtual environment requires access to the package index.

The procedure copies the supplement into a temporary directory and runs there, so the original files are
not modified. BU_SOURCE_DIR and BU_REPLAY_DIR are used only for this reproduction.

  BU_SOURCE_DIR="$(pwd -P)"
  BU_REPLAY_DIR="$(mktemp -d "${TMPDIR:-/tmp}/collatz-bu-replay.XXXXXX")"
  cp -R "$BU_SOURCE_DIR"/. "$BU_REPLAY_DIR"/
  cd "$BU_REPLAY_DIR"
  python3 -m venv .venv
  . .venv/bin/activate
  python -m pip install -r requirements.txt
  python -B -c 'import sys, sympy; print(sys.version); print(sympy.__version__)'

  cd binary_uniform_pade
  python -B -m unittest -v
  python -B generate.py --output regenerated.json
  python -B checker.py --certificate regenerated.json --report regenerated_results.json
  python -B -O checker.py --certificate regenerated.json --report optimized_results.json

  cd ../independent_audit
  cp EXACT_CHECK_RESULTS.json EXPECTED_EXACT_CHECK_RESULTS.json
  python -B verify_uniform_audit.py
  cd ..

Check the exit status and output of every command. If a command fails, record the failure and do not report
the run as PASS. Agreement between recomputation and expected results is established only after the
comparison below.

The independent script writes EXACT_CHECK_RESULTS.json, so the expected values are saved as
EXPECTED_EXACT_CHECK_RESULTS.json just before running it. Both the copy and the recomputation happen only
inside the temporary directory.

5. Comparing the original expected values with the regenerated JSON

In the temporary supplement directory, after the commands above, run the following. It compares JSON types
and values recursively, not string formatting.

python -B - <<'PY'
import json
from pathlib import Path

def typed_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(typed_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(typed_equal(x, y) for x, y in zip(a, b))
    return a == b

pairs = [
    ('binary_uniform_pade/certificates.json',
     'binary_uniform_pade/regenerated.json'),
    ('binary_uniform_pade/RESULTS.json',
     'binary_uniform_pade/regenerated_results.json'),
    ('binary_uniform_pade/RESULTS.json',
     'binary_uniform_pade/optimized_results.json'),
    ('independent_audit/EXPECTED_EXACT_CHECK_RESULTS.json',
     'independent_audit/EXACT_CHECK_RESULTS.json'),
]
for expected, actual in pairs:
    a = json.loads(Path(expected).read_text(encoding='utf-8'))
    b = json.loads(Path(actual).read_text(encoding='utf-8'))
    if not typed_equal(a, b):
        raise SystemExit('FAIL: ' + expected + ' versus ' + actual)
    print('PASS: ' + expected + ' versus ' + actual)
print('PASS: all four typed JSON comparisons')
PY

A PASS printed by a checker means only that the stated finite checks passed. It does not mean the general
irrationality theorem, the full proofs of external sources, verification of the whole research repository,
or a passing remote CI. Keep the temporary directory while inspecting logs and results.

6. Optimized mode and the scope of the independent auxiliary diagnostic

checker.py raises explicit exceptions for its main checks and gives the same results in normal and -O mode.
This is not generalized to -O support of every other script. verify_uniform_audit.py uses assert, so run it
in normal mode as above; its -O run is not used as a verification method.

The output of verify_uniform_audit.py has two parts:
  pade:
    independent Padé computations for three cases (period-doubling, Cantor, Thue-Morse).
  pseudo_trajectory:
    an exact 2,000-step diagnostic of a separate pseudo-trajectory that starts at the rational -3 and
    chooses branches according to a real state.

The second part preserves an auxiliary diagnostic from the original literature review. It is not a claim
about the actual parity orbit of an ordinary integer and is not an input to the proof of Theorem BU. The
2,000-step check does not decide rationality or irrationality of the final 2-adic value, so it is not
included in the paper's tables.

7. Author, use of AI, and review status

The author of the paper and of this supplement is Lee HaJin. Generative AI was used in the research records
and in drafting; ChatGPT was also used for this reproduction and for re-reading the natural-language proof,
and Anthropic Claude was used for the English manuscript and translation. Independence in the sense of a
separate generator and checker, or of a separate AI review, must not be read as peer review by external
human experts or as formal verification with a proof assistant.

The manuscript has not yet been finally reviewed by the author. The author is responsible for the
correctness, citations, originality and public release of the submitted manuscript. External priority of the
full theorem BU is not established; the precedents for the Thue-Morse special family and for Padé and Mahler
methods are acknowledged. The scope of the literature search and the remaining comparison tasks are
described in literature_review.txt.
