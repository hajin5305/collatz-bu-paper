# English manuscript - revision v0.2

Author: **Lee HaJin**. Date: **October 6, 2026**. Status: **draft for author review**.

The PDF and LaTeX are the primary English manuscript. A Word copy and a source archive accompany them.

## Corrections in this revision

- Made the repository's main README and reproduction guide English.
- Defined the negative valuation quantity before both nonvanishing cases, including the finite-orbit case, and stated the convention for the zero eigenvalue at exponent zero.
- Clarified the scope of the earlier Thue-Morse result: regrouping into `UV` and `VU` gives equal-length blocks even when the original output blocks have different lengths.
- Preserved the AI disclosure and added the draft status to the abstract.
- Corrected data availability: the private GitHub package and earlier Korean Zenodo deposit are identified separately. This revision does not claim a completed public English deposit.
- Pinned the Sharpe source citation and regenerated the PDF and editable Word manuscript.

The preceding English version adds a Mahler functional-equation proposition. The manuscript's irrationality argument does not depend on that proposition. No claim of external peer review, formal verification or established priority is made.

## Build

From this directory, run PDFLaTeX twice:

```sh
pdflatex -interaction=nonstopmode -halt-on-error collatz_bu_en.tex
pdflatex -interaction=nonstopmode -halt-on-error collatz_bu_en.tex
sha256sum -c SHA256SUMS
```

The revised PDF has 9 pages. PDF numbering is authoritative. Word section, theorem, equation and bibliography references are static. Rebuild the Word copy after any structural change.

The source archive contains the English source and rendered documents, this guide, and the supplementary files. The historical Korean audit records are preserved for provenance; use `supplement/README.md` for English reproduction instructions.

## Review still required

Before submission, the author should review the full proof, compare the cited literature and broader Mahler results directly, confirm priority and AI disclosure, and arrange a citable public deposit of the revised files. Successful finite checks do not establish the theorem for every substitution.
