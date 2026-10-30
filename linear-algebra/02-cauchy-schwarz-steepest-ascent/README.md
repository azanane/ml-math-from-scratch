# 02 — Cauchy–Schwarz & steepest ascent

## Problem
1. For a fixed nonzero vector $\vec v$, maximize the dot product
$\langle \vec v, \vec x \rangle$ over all unit vectors $\vec x$
($\lVert \vec x \rVert = 1$): find where the maximum is reached and its value.

2. Verify the result numerically.

## Vision — the intuition
$\langle \vec v, \vec x \rangle$ measures how much $\vec v$ and $\vec x$ point in the same direction. And $\vec x$ is a unit vector. So $\langle \vec v, \vec x \rangle$ is maximal if $\vec x$ is $\vec v$ normalized.

## Rigor — the proof

**Claim.** For a fixed nonzero vector $\vec v \in \mathbb{R}^n$, the function
$f(\vec x) = \langle \vec v, \vec x \rangle$ on the unit sphere
($\lVert \vec x \rVert = 1$) reaches its maximum value $\lVert \vec v \rVert$,
attained at $\vec x = \dfrac{\vec v}{\lVert \vec v \rVert}$.

**Upper bound.** By the Cauchy–Schwarz inequality,
$$\langle \vec v, \vec x \rangle \le |\langle \vec v, \vec x \rangle|
\le \lVert \vec v \rVert \, \lVert \vec x \rVert .$$
On the unit sphere $\lVert \vec x \rVert = 1$, so $\langle \vec v, \vec x \rangle \le \lVert \vec v \rVert$:
no point of the sphere makes $f$ exceed $\lVert \vec v \rVert$.

**The bound is attained.** Equality in Cauchy–Schwarz holds if and only if
$\vec x$ and $\vec v$ are colinear. The unit vector pointing the same way as
$\vec v$ is $\vec x = \dfrac{\vec v}{\lVert \vec v \rVert}$. Checking it:
$$f\!\left(\frac{\vec v}{\lVert \vec v \rVert}\right)
= \left\langle \vec v, \frac{\vec v}{\lVert \vec v \rVert} \right\rangle
= \frac{\langle \vec v, \vec v \rangle}{\lVert \vec v \rVert}
= \frac{\lVert \vec v \rVert^{2}}{\lVert \vec v \rVert}
= \lVert \vec v \rVert .$$
The bound is reached, so the maximum is exactly $\lVert \vec v \rVert$. $\qquad\blacksquare$

> The opposite unit vector $-\dfrac{\vec v}{\lVert \vec v \rVert}$ gives the minimum, $-\lVert \vec v \rVert$.

## Code — the judge
[`verify.py`](./verify.py) tests both halves of the claim, using the from-scratch primitives in
[`vectorops.py`](../../vectorops.py), in any dimension `n`.

1. **The bound is attained.** It builds the candidate point `x = v / ||v||`
   (`get_normalize_vector`) and checks that `dot(v, x)` equals `||v||`.
2. **Nothing beats it.** It samples 10,000 random unit vectors and checks that
   `dot(v, x)` never exceeds `||v||` — confirming `||v||` is the upper bound, not
   just a value that happens to be reached.

The equality in check 1 is **not** tested with `==`. Floating-point rounding
makes `dot(v, v/||v||)` land near `||v||`, not exactly on it, and the gap scales
with magnitude: a 64-bit float keeps ~15–16 *significant* digits, so for a vector
of norm ~15000 the absolute error is around `1e-11` — far larger than the machine
epsilon (`2.2e-16`). Comparing an absolute difference to machine epsilon fails
even when the values agree to full precision, so the test uses `math.isclose`,
whose default *relative* tolerance scales with the size of the numbers.


## Takeaway
A dot product with a fixed vector is maximized if the other term is its unit vector.