# Irrationality of Collatz Parity Inverses for Block Codings of Binary Uniform Fixed Points

**Author:** Lee HaJin
**Status:** research manuscript, not yet peer reviewed. English manuscript (journal style) and an earlier Korean draft (v0.1, 2026-10-06).

This repository contains the manuscript and the material needed to reproduce its finite exact checks.
The paper does **not** claim a solution of the Collatz conjecture, and the priority of the full theorem in the
literature has not been established.

## Main result

Let `Φ` be the inverse of the shortcut Collatz parity map (the inverse of the `3x+1` conjugacy map of
Bernstein and Lagarias). Let `t = σ(t)` be a one-sided fixed point of a binary `q`-uniform substitution
(`q ≥ 2`), and let `κ` be the block coding `0 ↦ U`, `1 ↦ V` with nonempty binary words `U, V`. Then

> `Φ(κ(t))` is rational **if and only if** `t` is ultimately periodic or `UV = VU`.

Primitivity of `σ`, equal block lengths and equal numbers of ones are not assumed. In the aperiodic,
noncommuting case no rational 2-adic integer, and in particular no positive integer, has the parity
sequence `κ(t)`.

## Documents

| File | Content |
|---|---|
| [english/collatz_bu_en.pdf](english/collatz_bu_en.pdf) | **English manuscript** (amsart, 8 pages) — the version intended for submission |
| [english/collatz_bu_en.tex](english/collatz_bu_en.tex) | LaTeX source of the English manuscript (`pdflatex`, run twice) |
| [english/README.md](english/README.md) | Changes relative to the Korean draft and items to confirm before submission |
| [collatz_bu_draft_ko.pdf](collatz_bu_draft_ko.pdf) | Earlier Korean draft v0.1 (12 pages) |
| [collatz_bu_draft_ko.tex](collatz_bu_draft_ko.tex) | LaTeX source of the Korean draft (`xelatex`, uses `fonts/`) |
| [collatz_bu_draft_ko.docx](collatz_bu_draft_ko.docx) | Editable Word version of the Korean draft |
| [collatz_bu_sources.zip](collatz_bu_sources.zip) | Original source bundle of the Korean draft (as first archived) |
| [PUBLICATION_NOTES.md](PUBLICATION_NOTES.md) | Why this result was selected, related work, and remaining tasks |
| [supplement/README.txt](supplement/README.txt) | Reproduction procedure and scope of the finite checks |
| [supplement/SOURCE_MANIFEST.json](supplement/SOURCE_MANIFEST.json) | Origin paths and SHA-256 of the seven copied research files |
| [supplement/literature_review.txt](supplement/literature_review.txt) | Literature triage used when preparing the manuscript |
| [korean/](korean/) | Original Korean versions of the explanatory notes (kept unchanged) |
| [SHA256SUMS](SHA256SUMS) | SHA-256 checksums of the files in this repository |

## Building the PDFs

English manuscript (TeX Live with `amsart`, `mathtools`, `enumitem`, `booktabs`, `hyperref`):

```bash
cd english
pdflatex collatz_bu_en.tex
pdflatex collatz_bu_en.tex
```

Korean draft (XeLaTeX; the Korean fonts are bundled in `fonts/`, licensed under [fonts/OFL.txt](fonts/OFL.txt)):

```bash
xelatex -interaction=nonstopmode -halt-on-error collatz_bu_draft_ko.tex
xelatex -interaction=nonstopmode -halt-on-error collatz_bu_draft_ko.tex
```

## Reproducing the finite checks

See [supplement/README.txt](supplement/README.txt). In short, from a temporary copy of `supplement/`:

```bash
cd binary_uniform_pade
python3 -B -m unittest -v                     # 14 regression tests (standard library only)
python3 -B checker.py --certificate certificates.json --report results.json
```

`checker.py` uses only the Python standard library; the certificate generator and the independent Padé
reconstruction require SymPy 1.14.0 (`supplement/requirements.txt`). The independent audit script writes
its result file next to itself, so run it in a temporary copy. Finite checks supplement the written proof;
they are not a formal verification and not peer review.

## Integrity

```bash
sha256sum -c SHA256SUMS
```

The supplementary code, certificates and expected results are byte-identical to the research repository
files listed in `supplement/SOURCE_MANIFEST.json`. The Korean draft and its source bundle are unchanged
from their first archived version; the explanatory notes were translated into English, and the Korean
originals are kept in [korean/](korean/).

## Provenance

- Research repository: `hajin5305/collatz-research`, commit `f751b9102355c516434ed9d0882bf4eb8608d95b`
- Result identifier there: `RED-BINARY-UNIFORM-PADE-IRRATIONALITY`
- Original write-up: `docs/research_records/2026-10-02/binary_uniform_pade/THEORY_KO.md`

The research repository was private when this material was prepared. The date of first record in that
repository is not a claim about the date of first discovery in the literature.

## Use of generative AI

Generative AI systems were used in the research and in preparing the manuscripts, including OpenAI ChatGPT
(Korean draft, literature search, proof drafting and review, verification code) and Anthropic Claude
(research repository sessions, proof re-check, English manuscript). No AI system is an author, and AI-based
checking is not a substitute for peer review. The author is responsible for the content, the correctness of
the proofs and the citations.
