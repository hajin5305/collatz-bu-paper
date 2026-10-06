# Notes on choosing the result and preparing the manuscript

*English translation of [korean/publication_notes_ko.txt](korean/publication_notes_ko.txt) (written 2026-10-06).*
Author: Lee HaJin. Basis of assessment: research repository state at commit
`f751b9102355c516434ed9d0882bf4eb8608d95b`.

## Selection

`RED-BINARY-UNIFORM-PADE-IRRATIONALITY` (Theorem BU) was chosen as the first result to turn into a paper.
Candidates were shortlisted from the repository's result register and its latest audit records, and the
proofs and literature of the shortlisted results were then examined closely. This does not mean that every
proof in the repository was fully audited.

The theorem gives a necessary and sufficient condition for the Collatz parity inverse to be rational when
a one-sided fixed point `t` of a binary `q`-uniform substitution is coded by two nonempty binary blocks
`U, V`: either `t` is ultimately periodic or `UV = VU`.

Reasons for the choice:

1. It is an exact classification of a whole class, not a finite search or a single example.
2. It does not assume primitivity of the substitution, equal output lengths, or equal numbers of ones.
3. A self-contained written proof can be given, combining the inverse-affine structure of noncommuting
   blocks, the two growth scales of a binary uniform substitution, and a fixed Padé-type approximant
   together with nonvanishing of the actual evaluations and a height comparison.
4. The period-doubling and nonprimitive Cantor examples make the scope concrete.
5. The roles of the theorem and of the supporting computation can be separated cleanly, and the original
   code and finite certificates are available.

## Comparison with other candidates

- **`RED-RC-Q481`.** A sharp computer-assisted result: among actual positive rational Collatz cycles with a
  special partition into contracting blocks of equal length and equal exponent sum, whose least block-list
  period is nonconstant and contains a repeated block, the denominator is at least 481, and the bound is
  attained. It is the runner-up for a paper. However, not every cycle has such a partition, so omitting the
  hypotheses changes the meaning substantially, and external priority has not been checked.
- **Classification of length-5 cancelling pairs.** The computation leaving exactly two pairs could become a
  short note, but its scope is narrower and its difference from known results (such as exclusion of small
  integer cycles) must first be clarified.
- **Subcritical clock candidate.** The result for a window of length about `q(t) ≈ t^(3/5)` with specific
  constants is precise, but would require much motivation for an outside reader, and its priority is
  unchecked.
- **WQ (quasipolynomial weak rank).** The latest audit classifies it as a reformulation following from an
  existing theorem of Monks et al.; earlier "unchecked" records must not be used as a novelty assessment.
- **LOCAL-G31 and ER3.** A single finite-length certificate, or obligations that remain open, must not be
  confused with an infinite theorem; at present these are less suitable than BU as the core of a paper.

This comparison is not a score guaranteeing acceptance or novelty.

## Related work and wording about originality

The repository's latest audit still records the priority of the full BU theorem as unchecked/low. The
manuscript therefore treats it as unconfirmed and avoids words such as "first" or "new general principle".

- Bernstein–Lagarias (1996): the parity conjugacy map and the basic 2-adic setting.
- Bugeaud–Yao (2017): p-adic Padé approximation, Mahler-type values, Thue–Morse related results.
- Adamczewski–Bugeaud (2007): complexity of Hensel digit expansions. Parity bits are not the digits of the value.
- Allikvere (2026): unreviewed preprint; transcendence in the special case of Thue–Morse block codings.
- Sharpe (2026): unreviewed manuscript; exclusion of the parity sequence of one specific 3-uniform substitution.
- Ide (2019, arXiv v1): theorems on values of multivariable p-adic Mahler-type functions with conditions on
  the evaluation points. The existence of this work is distinguished from any claim that its conditions hold
  automatically for the whole BU class.
- Loxton–van der Poorten (1982): Mahler's method in several variables; the English manuscript explains why
  its regularity hypotheses fail for part of the family (Section 1.1 and Proposition 4.2).

Whether the full necessary-and-sufficient statement for the whole binary uniform class is a direct corollary
of an existing theorem still needs to be checked. A complete proof that it does *not* reduce to an existing
theorem is also not part of this work.

## Proof versus computation

The main theorem is proved in writing. The six Padé certificates and fourteen regression tests are finite
supporting checks. Affine identities, first-mismatch valuations, the commuting exceptions and commutators,
coefficient growth, and the scaled block identities were rechecked in exact arithmetic.

The coefficients of degrees 0 through 12 (thirteen coefficients) are cancelled, so `E` is divisible by
`z^13`. The Cantor certificate has first nonzero degree 14; the other five have 13. The 900 commutator test
pairs include commuting pairs; they are not 900 nonzero pairs.

That the actual evaluations `E(z_k, y_k)` are nonzero infinitely often must be proved separately from the
fact that the formal series `E` is nonzero; the manuscript does both. For nonzero evaluations, the
divisibility lower bound `13 L q^k` and the height upper bound `8 log_2(3) L q^k` contradict each other
because `2^13 = 8192 > 6561 = 3^8`.

The 2000-step real pseudo-trajectory computed by the independent auxiliary script is not an input to the
proof of BU and is not included in the paper's tables. An independent re-reading by an AI is not external
review.

## Before formal submission

1. The author should check the whole proof and all sources, and ask an outside researcher familiar with
   p-adic number theory or combinatorics on words to review the main theorem and the nonvanishing step.
2. Settle the exact relation between the full theorem and existing multivariable p-adic Mahler-type
   theorems, including recent unreviewed manuscripts, to fix the scope of the contribution.
3. Match the target journal's language and style, and add only author information that has been confirmed
   (affiliation, contact, ORCID).
4. Decide the public release of the code and certificates and an archived, citable copy.

The manuscript does not prove the Collatz conjecture. It does not claim that every integer orbit has the
substitution structure considered, that all automatic sequences are excluded, or that the whole class is
transcendental. Keeping these limits explicit makes the paper easier to evaluate.
