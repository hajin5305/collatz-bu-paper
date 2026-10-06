# Supplementary materials and reproduction guide

Author: **Lee HaJin**. Source commit: `f751b9102355c516434ed9d0882bf4eb8608d95b` in `hajin5305/collatz-research`.

This package reproduces finite block identities and six explicit Padé certificates using exact integer and rational arithmetic. The general irrationality conclusion rests on the manuscript's written proof. These finite checks do not prove every instance of the theorem or the general Collatz conjecture.

## Files

| Path | Purpose |
| --- | --- |
| `binary_uniform_pade/generate.py` | SymPy certificate generator; `--output` is required |
| `binary_uniform_pade/checker.py` | Separate standard-library checker using exact fractions |
| `binary_uniform_pade/test_checker.py` | 14 existing regression and tampering tests |
| `binary_uniform_pade/certificates.json` | Six reference certificates |
| `binary_uniform_pade/RESULTS.json` | Expected finite-check results |
| `independent_audit/verify_uniform_audit.py` | Separate reconstruction of three Padé examples |
| `independent_audit/EXACT_CHECK_RESULTS.json` | Expected independent results |
| `SOURCE_MANIFEST.json` | Original source paths and SHA-256 hashes |
| `validation_summary.json` | Recorded execution scope, counts and comparisons |
| `requirements.txt` | SymPy 1.14.0 requirement |
| `literature_review.txt` | Literature triage and scope of related work |
| `literature_search_log.json` | Record of the literature searches |

The original Korean version of this guide is preserved as [`korean/supplement_README_ko.txt`](../korean/supplement_README_ko.txt). This file is the English entry point.

## Run in a temporary copy

The independent audit writes `EXACT_CHECK_RESULTS.json` beside its script. Preserve expected data and work in a disposable copy. From the repository root:

```sh
audit_dir=$(mktemp -d)
cp -R supplement "$audit_dir/supplement"
cd "$audit_dir/supplement"
python -m pip install -r requirements.txt
cd binary_uniform_pade
python -B -m unittest -v test_checker
python -B generate.py --output regenerated.json
python -B checker.py --certificate regenerated.json --report regenerated_results.json
python -B -O checker.py --certificate regenerated.json --report optimized_results.json
cd ../independent_audit
cp EXACT_CHECK_RESULTS.json EXPECTED_EXACT_CHECK_RESULTS.json
python -B verify_uniform_audit.py
cd ..
```

Verify every exit code. Then compare JSON values and types, not merely formatted strings:

```python
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
    ('binary_uniform_pade/certificates.json', 'binary_uniform_pade/regenerated.json'),
    ('binary_uniform_pade/RESULTS.json', 'binary_uniform_pade/regenerated_results.json'),
    ('binary_uniform_pade/RESULTS.json', 'binary_uniform_pade/optimized_results.json'),
    ('independent_audit/EXPECTED_EXACT_CHECK_RESULTS.json', 'independent_audit/EXACT_CHECK_RESULTS.json'),
]
for expected, actual in pairs:
    a = json.loads(Path(expected).read_text())
    b = json.loads(Path(actual).read_text())
    if not typed_equal(a, b):
        raise SystemExit(f'FAIL: {expected} versus {actual}')
    print(f'PASS: {expected} versus {actual}')
```

The checker is tested in normal and `-O` modes. The independent audit uses assertions: run it in normal mode. Its separate 2,000-step real pseudo-trajectory diagnostic is not an ordinary integer parity orbit, is not an input to the BU theorem, and does not determine rationality of a limiting 2-adic value.

Generative AI assisted preparation and review. Independent code implementations and AI readings do not constitute external human peer review or formal proof verification. Lee HaJin remains responsible for final author review.
