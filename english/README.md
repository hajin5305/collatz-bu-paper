# English manuscript (submission draft)

- `collatz_bu_en.tex` — journal-style manuscript (amsart), built with `pdflatex` (run twice).
- `collatz_bu_en.pdf` — compiled version (8 pages, TeX Live 2023, pdfTeX).

This is an English rewrite of the Korean draft `../collatz_bu_draft_ko.tex` (v0.1, kept unchanged).
The mathematics (definitions, lemmas, proof of the main theorem, examples) is the same; the changes are:

1. English text in `amsart` with MSC 2020 codes and keywords.
2. New Proposition 4.2: the series `F, G` satisfy a two-variable linear Mahler-type functional equation for
   the monomial map `τ(z,y) = (z^q y^{a_0}, y^δ)`, and the evaluation points form one `τ`-orbit. Section 1.1
   explains why the regularity hypotheses of Loxton–van der Poorten (1982, §2 and Theorem 1) fail for some
   members of the family (`δ ∈ {0, ±1}` or `δ < 0`; 2-adic place). The proof does not use this proposition.
   The functional equation and the orbit relation were checked on truncated series for five substitutions.
3. The contribution is stated relative to Allikvere (2026; Thue–Morse, equal-length blocks, transcendence) and
   Sharpe (2026; one specific substitution), without a novelty claim beyond the sources discussed.
4. Lemma 3.2 (two-word codes) cites Lothaire, *Combinatorics on Words*, Chapter 1, and keeps the short proof.
5. Repository-internal material (commit hashes, audit names, run environment) moved out of the main text into
   the Data availability statement; the finite checks are summarized in Section 8.
6. The generative-AI statement moved from the abstract to an Acknowledgments section at the end, naming both
   OpenAI ChatGPT and Anthropic Claude.

Items for the author to confirm before submission:

- affiliation / e-mail / ORCID (left blank on purpose);
- the AI statement wording matches the tools actually used;
- the Zenodo record and this repository are public, and the DOI to cite in the Data availability section
  (currently the record URL `https://zenodo.org/records/23186729` is cited);
- the target journal's own style and AI policy.
