# Collatz BU paper and reproducibility materials

**Author: Lee HaJin**  
**Current manuscript: English revision v0.2 - October 6, 2026**

*Irrationality of Collatz parity inverses for block codings of binary uniform fixed points*

This repository contains an English research manuscript and exact finite verification materials. The manuscript is a draft pending the author's final review. Priority for the full theorem has not been established; the paper acknowledges earlier Thue-Morse results and Padé/Mahler methods.

## English manuscript

| File | Contents |
| --- | --- |
| [PDF](english/collatz_bu_en.pdf) | Typeset manuscript, 9 pages |
| [Word](english/collatz_bu_en.docx) | Editable English manuscript |
| [LaTeX](english/collatz_bu_en.tex) | Authoritative source |
| [Source archive](english/collatz_bu_en_sources.zip) | English manuscript, documentation and supplementary files |
| [Revision notes](english/README.md) | Corrections and build instructions |
| [Reproduction guide](supplement/README.md) | Scope, commands and source provenance |

The theorem classifies when the 2-adic Collatz parity inverse of a binary block coding of a binary uniform substitution fixed point is rational: precisely when the control word is ultimately periodic or the two output blocks commute. It does not assert a solution of the general Collatz conjecture.

## Build and verification

```sh
cd english
pdflatex -interaction=nonstopmode -halt-on-error collatz_bu_en.tex
pdflatex -interaction=nonstopmode -halt-on-error collatz_bu_en.tex
sha256sum -c SHA256SUMS
```

The English source uses standard TeX Live packages and does not require the Korean fonts. PDF numbering is authoritative. Word references and equation numbers are static and must be updated after structural edits.

The supplementary checker uses Python's standard library. Generating certificates and running the independent reconstruction require SymPy 1.14.0. See the [English reproduction guide](supplement/README.md). Finite computations supplement the written proof; they are not external peer review or proof-assistant verification.

## Provenance and archived drafts

The supplementary research files are pinned to `hajin5305/collatz-research` commit `f751b9102355c516434ed9d0882bf4eb8608d95b`. The theorem identifier is `RED-BINARY-UNIFORM-PADE-IRRATIONALITY`; the source record is `docs/research_records/2026-10-02/binary_uniform_pade/THEORY_KO.md`. The [source manifest](supplement/SOURCE_MANIFEST.json) records the original paths and hashes.

The Korean v0.1 PDF, Word, LaTeX and source archive at the repository root are preserved as historical drafts. Root `SHA256SUMS` covers those original materials; `english/SHA256SUMS` covers the revised English package. Korean audit notes remain historical source records, with an English guide provided for reproduction.

This repository is private. [Zenodo record 23186729](https://zenodo.org/records/23186729) is the earlier Korean draft deposit; it should not be cited as a public deposit of this English revision or its supplementary package.

## Generative AI disclosure

Generative AI assisted research, drafting, code preparation, proof criticism and editing. The Korean draft and this revision used OpenAI ChatGPT. The preceding English manuscript reports Anthropic Claude assistance. No AI system is an author. Lee HaJin is the sole author and is responsible for final review of mathematical correctness, citations, originality and disclosure before submission. See the manuscript's full disclosure.
