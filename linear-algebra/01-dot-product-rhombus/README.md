# 01 — Dot product & the diagonals of a rhombus

## Problem
1. Prove that the diagonals of a rhombus are perpendicular, and verify it
numerically.

2. Implement the dot product from scratch in dimension n.

## Vision — the intuition
A rhombus is symmetric about its diagonals. If you fold it along one of them,
the other diagonal folds exactly onto itself — which can only happen if the two
diagonals meet at a right angle.

## Rigor — the proof

**Claim.** The diagonals of a rhombus are perpendicular.

**Setup.** Let $\vec a$ and $\vec b$ be the two sides of the rhombus starting
from the same vertex. Both diagonals can be written using only $\vec a$ and $\vec b$:

- $\vec d_1 = \vec a + \vec b$ — joins the start vertex to the opposite one
- $\vec d_2 = \vec b - \vec a$ — joins the two remaining vertices

Two vectors are orthogonal if and only if their dot product is zero.

**Proof.** Expanding by distributivity:

$$\vec d_1 \cdot \vec d_2 = (\vec a + \vec b)\cdot(\vec b - \vec a)
= \vec a\cdot\vec b - \vec a\cdot\vec a + \vec b\cdot\vec b - \vec b\cdot\vec a$$

By symmetry of the dot product ($\vec u\cdot\vec v = \vec v\cdot\vec u$), the two
cross terms cancel: $\vec a\cdot\vec b - \vec b\cdot\vec a = 0$. Hence

$$\vec d_1 \cdot \vec d_2 = \vec b\cdot\vec b - \vec a\cdot\vec a
= \lVert\vec b\rVert^2 - \lVert\vec a\rVert^2.$$

In a rhombus all sides have equal length, so $\lVert\vec a\rVert = \lVert\vec b\rVert$, giving

$$\vec d_1 \cdot \vec d_2 = 0 \quad\Longrightarrow\quad \vec d_1 \perp \vec d_2. \qquad\blacksquare$$

> This proof uses no coordinates and holds in any dimension $n$.

## Code — the judge
`dot.py` implements the dot product from scratch (pure Python, no libraries),
working in any dimension `n`. To test the rhombus proof, it builds a random
rhombus in dimension 5 — two random sides forced to equal length by
normalization — then computes the dot product of the two diagonals,
`dot(a + b, b - a)`.

Most of the time, the result is not exactly `0`; it comes out around `1e-16`. This is not a flaw
in the proof — it is floating-point rounding. A 64-bit float stores only about
15–16 significant digits, and, more fundamentally, the machine works in binary:
most real numbers (even simple ones like `0.1`) have no exact finite binary
representation, so they are rounded the moment they are stored. These tiny
errors accumulate and land near, but not exactly on, zero.

The rule that follows: never test floating-point values with `== 0`. Use
`abs(x) < epsilon` instead — the same rule that governs the stopping criterion
of gradient descent.

## Takeaway
A geometric truth proven without coordinates holds in every dimension.