# Exercises: Linear Algebra for PSE

## Exercise 1: Matrix Operations and Material Balances (Easy)

**Problem:**
A chemical plant has three streams mixing in a junction. Each stream carries components A, B, and C.

- Stream 1: 100 kg/hr with composition [0.4, 0.3, 0.3] (A, B, C mass fractions)
- Stream 2: 150 kg/hr with composition [0.2, 0.6, 0.2]
- Stream 3 (exit): Unknown flow rate and composition

a) Write the material balance in matrix form.
b) Calculate the exit stream composition vector.
c) Verify your answer satisfies conservation of mass.

**Solution:**

a) **Matrix formulation:**

Component mass flow rates = (total flow) × (mass fraction)

For inlet streams:
$$\dot{m}_1 = 100 \begin{bmatrix} 0.4 \\ 0.3 \\ 0.3 \end{bmatrix} = \begin{bmatrix} 40 \\ 30 \\ 30 \end{bmatrix} \text{ kg/hr}$$

$$\dot{m}_2 = 150 \begin{bmatrix} 0.2 \\ 0.6 \\ 0.2 \end{bmatrix} = \begin{bmatrix} 30 \\ 90 \\ 30 \end{bmatrix} \text{ kg/hr}$$

b) **Exit stream:**

Total component flows (conservation):
$$\dot{m}_3 = \dot{m}_1 + \dot{m}_2 = \begin{bmatrix} 40 \\ 30 \\ 30 \end{bmatrix} + \begin{bmatrix} 30 \\ 90 \\ 30 \end{bmatrix} = \begin{bmatrix} 70 \\ 120 \\ 60 \end{bmatrix} \text{ kg/hr}$$

Total exit flow: F₃ = 70 + 120 + 60 = 250 kg/hr ✓ (= 100 + 150)

Exit composition:
$$\mathbf{x}_3 = \frac{1}{250}\begin{bmatrix} 70 \\ 120 \\ 60 \end{bmatrix} = \begin{bmatrix} 0.28 \\ 0.48 \\ 0.24 \end{bmatrix}$$

c) **Verification:**

Mass fractions sum to 1: 0.28 + 0.48 + 0.24 = 1.00 ✓

Total mass balance: 100 + 150 = 250 ✓

Component A: 100(0.4) + 150(0.2) = 40 + 30 = 70 = 250(0.28) ✓

---

## Exercise 2: Solving Linear Systems - Distillation Column (Moderate)

**Problem:**
A distillation column separates a three-component mixture. The component material balances around the column give:

$$\begin{cases}
x_D + x_B = 100 \\
0.95x_D + 0.05x_B = 60 \\
\end{cases}$$

where:
- x_D = total distillate flow (mol/s)
- x_B = total bottoms flow (mol/s)

Additionally, for component balances with distillate compositions y_D,i and bottoms compositions y_B,i:

For a specific component with feed composition 0.6:
$$0.95 y_{D,1} x_D + 0.05 y_{B,1} x_B = 0.6 \times 100$$

where distillate has y_D,1 = 0.90 and bottoms has y_B,1 = 0.10.

a) Solve for x_D and x_B using Gaussian elimination.
b) Verify the component balance.
c) Set up the same problem in matrix form and solve using matrix inversion.

**Solution:**

a) **Gaussian elimination:**

System:
$$\begin{bmatrix}
1 & 1 \\
0.95 & 0.05
\end{bmatrix}
\begin{bmatrix} x_D \\ x_B \end{bmatrix}
=
\begin{bmatrix} 100 \\ 60 \end{bmatrix}$$

Row operation: R₂ ← R₂ - 0.95R₁

$$\begin{bmatrix}
1 & 1 \\
0 & 0.05 - 0.95
\end{bmatrix}
\begin{bmatrix} x_D \\ x_B \end{bmatrix}
=
\begin{bmatrix} 100 \\ 60 - 95 \end{bmatrix}$$

$$\begin{bmatrix}
1 & 1 \\
0 & -0.90
\end{bmatrix}
\begin{bmatrix} x_D \\ x_B \end{bmatrix}
=
\begin{bmatrix} 100 \\ -35 \end{bmatrix}$$

Back substitution:
$$-0.90 x_B = -35 \implies x_B = \frac{35}{0.90} = 38.89 \text{ mol/s}$$

$$x_D + 38.89 = 100 \implies x_D = 61.11 \text{ mol/s}$$

b) **Component verification:**

$$0.90 \times 61.11 + 0.10 \times 38.89 = 55.00 + 3.89 = 58.89$$

Expected: 0.6 × 100 = 60

**Small discrepancy due to rounding.** With exact values: x_D = 550/9, x_B = 350/9:

$$0.90 \times \frac{550}{9} + 0.10 \times \frac{350}{9} = \frac{495 + 35}{9} = \frac{530}{9} \approx 58.89$$

Wait, let me recalculate. The second equation should give:
$$0.95x_D + 0.05x_B = 60$$

This is the **split fractions** (0.95 to distillate, 0.05 to bottoms), not compositions!

Actually this means:
- 95% of feed goes to distillate
- 5% of feed goes to bottoms

So x_D = 95 mol/s, x_B = 5 mol/s directly from the split!

Let me reformulate as a proper linear system problem:

**Corrected Problem:**

Two components in feed (100 mol/s total):
- Component 1: 60 mol/s (z₁ = 0.6)
- Component 2: 40 mol/s (z₂ = 0.4)

Distillate (x_D mol/s) has composition [y₁, y₂]
Bottoms (x_B mol/s) has composition [x₁, x₂]

Balances:
$$\begin{cases}
x_D + x_B = 100 \\
y_1 x_D + x_1 x_B = 60 \\
y_2 x_D + x_2 x_B = 40
\end{cases}$$

With y₁ = 0.90, x₁ = 0.30, y₂ = 0.10, x₂ = 0.70:

$$\begin{bmatrix}
1 & 1 \\
0.90 & 0.30
\end{bmatrix}
\begin{bmatrix} x_D \\ x_B \end{bmatrix}
=
\begin{bmatrix} 100 \\ 60 \end{bmatrix}$$

Row 2: R₂ ← R₂ - 0.90R₁

$$0.30 - 0.90 = -0.60$$
$$60 - 90 = -30$$

$$-0.60 x_B = -30 \implies x_B = 50 \text{ mol/s}$$

$$x_D = 100 - 50 = 50 \text{ mol/s}$$

Check component 2:
$$0.10(50) + 0.70(50) = 5 + 35 = 40$$ ✓

c) **Matrix inversion:**

$$\mathbf{A} = \begin{bmatrix} 1 & 1 \\ 0.90 & 0.30 \end{bmatrix}$$

$$\det(\mathbf{A}) = 1(0.30) - 1(0.90) = -0.60$$

$$\mathbf{A}^{-1} = \frac{1}{-0.60}\begin{bmatrix} 0.30 & -1 \\ -0.90 & 1 \end{bmatrix} = \begin{bmatrix} -0.5 & 1.667 \\ 1.5 & -1.667 \end{bmatrix}$$

$$\begin{bmatrix} x_D \\ x_B \end{bmatrix} = \begin{bmatrix} -0.5 & 1.667 \\ 1.5 & -1.667 \end{bmatrix} \begin{bmatrix} 100 \\ 60 \end{bmatrix}$$

$$x_D = -0.5(100) + 1.667(60) = -50 + 100 = 50 \text{ mol/s}$$ ✓

$$x_B = 1.5(100) - 1.667(60) = 150 - 100 = 50 \text{ mol/s}$$ ✓

---

## Exercise 3: Eigenvalues and Stability - CSTR Dynamics (Challenging)

**Problem:**
A non-isothermal CSTR with first-order exothermic reaction has linearized dynamics:

$$\frac{d}{dt}\begin{bmatrix} C_A \\ T \end{bmatrix} = \begin{bmatrix} -5 & -2 \\ 4 & -3 \end{bmatrix} \begin{bmatrix} C_A \\ T \end{bmatrix}$$

where deviations are from steady state (C_A in mol/L, T in K).

a) Find the eigenvalues of the system matrix.
b) Determine if the system is stable.
c) Find the eigenvectors and interpret physically.
d) If C_A(0) = 0.1 mol/L and T(0) = 5 K, find the general solution C_A(t) and T(t).

**Solution:**

a) **Eigenvalues:**

$$\mathbf{A} = \begin{bmatrix} -5 & -2 \\ 4 & -3 \end{bmatrix}$$

Characteristic equation:
$$\det(\mathbf{A} - \lambda \mathbf{I}) = \det\begin{bmatrix} -5-\lambda & -2 \\ 4 & -3-\lambda \end{bmatrix} = 0$$

$$(-5-\lambda)(-3-\lambda) - (-2)(4) = 0$$

$$15 + 5\lambda + 3\lambda + \lambda^2 + 8 = 0$$

$$\lambda^2 + 8\lambda + 23 = 0$$

Using quadratic formula:
$$\lambda = \frac{-8 \pm \sqrt{64 - 92}}{2} = \frac{-8 \pm \sqrt{-28}}{2} = \frac{-8 \pm 2i\sqrt{7}}{2}$$

$$\lambda_1 = -4 + i\sqrt{7} \approx -4 + 2.65i$$
$$\lambda_2 = -4 - i\sqrt{7} \approx -4 - 2.65i$$

**Complex conjugate eigenvalues!**

b) **Stability:**

Real part: Re(λ) = -4 < 0

**System is STABLE** - deviations decay exponentially with oscillations.

**Physical interpretation:**
- Decay rate: e^(-4t) (time constant τ = 0.25 min)
- Oscillation frequency: ω = √7 ≈ 2.65 rad/min
- Period: T = 2π/ω ≈ 2.37 min

The system exhibits **damped oscillations** - concentration and temperature oscillate while returning to steady state.

c) **Eigenvectors:**

For λ₁ = -4 + i√7:

$$\begin{bmatrix} -5-(-4+i\sqrt{7}) & -2 \\ 4 & -3-(-4+i\sqrt{7}) \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

$$\begin{bmatrix} -1-i\sqrt{7} & -2 \\ 4 & 1+i\sqrt{7} \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

From first row: $(-1-i\sqrt{7})v_1 - 2v_2 = 0$

$$v_2 = -\frac{1+i\sqrt{7}}{2}v_1$$

Choosing v₁ = 2:

$$\mathbf{v}_1 = \begin{bmatrix} 2 \\ -1-i\sqrt{7} \end{bmatrix}$$

Similarly: $\mathbf{v}_2 = \overline{\mathbf{v}_1} = \begin{bmatrix} 2 \\ -1+i\sqrt{7} \end{bmatrix}$

**Physical interpretation:**
The complex eigenvectors indicate the system doesn't have simple exponential modes - instead it has oscillatory modes. The real and imaginary parts of the eigenvector give the shape of the oscillation in (C_A, T) phase space.

d) **General solution:**

For complex eigenvalues λ = α ± iβ with α = -4, β = √7:

The real-valued solution is:
$$\begin{bmatrix} C_A(t) \\ T(t) \end{bmatrix} = e^{\alpha t}\left[c_1 \text{Re}(\mathbf{v}e^{i\beta t}) + c_2 \text{Im}(\mathbf{v}e^{i\beta t})\right]$$

This can be written as:
$$\begin{bmatrix} C_A(t) \\ T(t) \end{bmatrix} = e^{-4t}\left[A\cos(\sqrt{7}t)\mathbf{u} + B\sin(\sqrt{7}t)\mathbf{w}\right]$$

where u and w are real vectors related to Re(v) and Im(v).

**Simpler approach using matrix exponential:**

The solution is $\mathbf{x}(t) = e^{\mathbf{A}t}\mathbf{x}(0)$.

For this problem, we can use the fact that:
$$e^{\mathbf{A}t} = e^{-4t}\left[\cos(\sqrt{7}t)\mathbf{I} + \frac{\sin(\sqrt{7}t)}{\sqrt{7}}(\mathbf{A} + 4\mathbf{I})\right]$$

With $\mathbf{A} + 4\mathbf{I} = \begin{bmatrix} -1 & -2 \\ 4 & 1 \end{bmatrix}$:

$$e^{\mathbf{A}t} = e^{-4t}\left[\begin{bmatrix} \cos(\sqrt{7}t) & 0 \\ 0 & \cos(\sqrt{7}t) \end{bmatrix} + \frac{\sin(\sqrt{7}t)}{\sqrt{7}}\begin{bmatrix} -1 & -2 \\ 4 & 1 \end{bmatrix}\right]$$

Applying initial condition $\begin{bmatrix} 0.1 \\ 5 \end{bmatrix}$:

$$\begin{bmatrix} C_A(t) \\ T(t) \end{bmatrix} = e^{-4t}\left[\begin{bmatrix} 0.1\cos(\sqrt{7}t) \\ 5\cos(\sqrt{7}t) \end{bmatrix} + \frac{\sin(\sqrt{7}t)}{\sqrt{7}}\begin{bmatrix} -0.1 - 10 \\ 0.4 + 5 \end{bmatrix}\right]$$

$$= e^{-4t}\begin{bmatrix} 0.1\cos(\sqrt{7}t) - \frac{10.1}{\sqrt{7}}\sin(\sqrt{7}t) \\ 5\cos(\sqrt{7}t) + \frac{5.4}{\sqrt{7}}\sin(\sqrt{7}t) \end{bmatrix}$$

**Key observations:**
- Both C_A and T oscillate with period ≈ 2.37 min
- Amplitude decays as e^(-4t)
- System reaches steady state (within 5%) after about t = 3/4 ≈ 0.75 min

---

## Exercise 4: Matrix Decomposition - Multiple Reactors (Challenging)

**Problem:**
A system of 4 CSTRs in series has the following linearized material balance matrix:

$$\mathbf{A} = \begin{bmatrix}
-2 & 0 & 0 & 0 \\
2 & -2 & 0 & 0 \\
0 & 2 & -2 & 0 \\
0 & 0 & 2 & -2
\end{bmatrix}$$

a) Perform LU decomposition by hand.
b) Use the LU factors to solve Ax = b where b = [10, 0, 0, 0]^T.
c) Find all eigenvalues of A.
d) What do the eigenvalues tell you about the system dynamics?

**Solution:**

a) **LU Decomposition:**

The matrix is already lower triangular-friendly. We seek A = LU.

**Step-by-step elimination:**

Original matrix:
$$\begin{bmatrix}
-2 & 0 & 0 & 0 \\
2 & -2 & 0 & 0 \\
0 & 2 & -2 & 0 \\
0 & 0 & 2 & -2
\end{bmatrix}$$

Row 2 ← Row 2 + (2/-2)Row 1 = Row 2 - Row 1:
Multiplier: l₂₁ = 2/(-2) = -1

Row 3 already has zero in position (3,1)
Row 4 already has zero in position (4,1)

After first column:
$$\begin{bmatrix}
-2 & 0 & 0 & 0 \\
0 & -2 & 0 & 0 \\
0 & 2 & -2 & 0 \\
0 & 0 & 2 & -2
\end{bmatrix}$$

Row 3 ← Row 3 + (2/-2)Row 2 = Row 3 - Row 2:
Multiplier: l₃₂ = 2/(-2) = -1

Row 4 ← Row 4 + (2/-2)Row 3 = Row 4 - Row 3:
Multiplier: l₄₃ = 2/(-2) = -1

**Result:**

$$\mathbf{U} = \begin{bmatrix}
-2 & 0 & 0 & 0 \\
0 & -2 & 0 & 0 \\
0 & 0 & -2 & 0 \\
0 & 0 & 0 & -2
\end{bmatrix}$$

$$\mathbf{L} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 \\
0 & -1 & 1 & 0 \\
0 & 0 & -1 & 1
\end{bmatrix}$$

**Verify:** LU = ?

First row of LU: [1×(-2), ...] = [-2, 0, 0, 0] ✓
Second row: [-1×(-2) + 1×(-2), ...] = [2-2, -2, 0, 0] = [0, -2, 0, 0]... Wait, that's wrong!

Let me recalculate properly. The multipliers go in L below the diagonal:

$$\mathbf{L} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 \\
0 & -1 & 1 & 0 \\
0 & 0 & -1 & 1
\end{bmatrix}$$

Check row 2 of LU:
$$[-1 \times -2, \; -1 \times 0 + 1 \times (-2), \; ...] = [2, -2, 0, 0]$$ ✓

b) **Solve Ax = b using LU:**

First solve **Ly = b** (forward substitution):

$$\begin{bmatrix}
1 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 \\
0 & -1 & 1 & 0 \\
0 & 0 & -1 & 1
\end{bmatrix}
\begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ y_4 \end{bmatrix}
=
\begin{bmatrix} 10 \\ 0 \\ 0 \\ 0 \end{bmatrix}$$

$y_1 = 10$
$-y_1 + y_2 = 0 \implies y_2 = 10$
$-y_2 + y_3 = 0 \implies y_3 = 10$
$-y_3 + y_4 = 0 \implies y_4 = 10$

So $\mathbf{y} = \begin{bmatrix} 10 \\ 10 \\ 10 \\ 10 \end{bmatrix}$

Now solve **Ux = y** (backward substitution):

$$\begin{bmatrix}
-2 & 0 & 0 & 0 \\
0 & -2 & 0 & 0 \\
0 & 0 & -2 & 0 \\
0 & 0 & 0 & -2
\end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix}
=
\begin{bmatrix} 10 \\ 10 \\ 10 \\ 10 \end{bmatrix}$$

$-2x_4 = 10 \implies x_4 = -5$
$-2x_3 = 10 \implies x_3 = -5$
$-2x_2 = 10 \implies x_2 = -5$
$-2x_1 = 10 \implies x_1 = -5$

**Solution:** $\mathbf{x} = \begin{bmatrix} -5 \\ -5 \\ -5 \\ -5 \end{bmatrix}$

**Verification:**

$$\mathbf{Ax} = \begin{bmatrix}
-2 & 0 & 0 & 0 \\
2 & -2 & 0 & 0 \\
0 & 2 & -2 & 0 \\
0 & 0 & 2 & -2
\end{bmatrix}
\begin{bmatrix} -5 \\ -5 \\ -5 \\ -5 \end{bmatrix}$$

Row 1: $-2(-5) = 10$ ✓
Row 2: $2(-5) + (-2)(-5) = -10 + 10 = 0$ ✓
Row 3: $2(-5) + (-2)(-5) = 0$ ✓
Row 4: $2(-5) + (-2)(-5) = 0$ ✓

c) **Eigenvalues:**

For a triangular matrix (upper, lower, or diagonal), **eigenvalues are the diagonal elements**!

$$\lambda_1 = \lambda_2 = \lambda_3 = \lambda_4 = -2$$

**Repeated eigenvalue** of multiplicity 4.

d) **Physical interpretation:**

**All eigenvalues = -2** means:
- System is **stable** (all λ < 0)
- **No oscillations** (all real eigenvalues)
- All modes decay as e^(-2t)
- Time constant τ = 1/2 = 0.5 time units for each reactor

**For reactors in series:**
- Disturbance in Reactor 1 propagates downstream
- Each reactor has same residence time (since all λ identical)
- The cascade effect creates a delay but not oscillations

The repeated eigenvalue indicates **similar dynamics** in all reactors - they're identical units in series!

---

## Exercise 5: Condition Number and Numerical Stability (Advanced)

**Problem:**
Two material balance systems are given:

**System A:**
$$\begin{bmatrix} 1 & 1 \\ 1 & 1.0001 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}$$

**System B:**
$$\begin{bmatrix} 10 & 7 \\ 7 & 5 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 17 \\ 12 \end{bmatrix}$$

a) Solve both systems exactly.
b) Calculate the condition number (using ∞-norm) for each matrix.
c) If the right-hand side of System A changes by 0.0001, estimate the change in solution using the condition number.
d) Discuss implications for process design when material balances are nearly singular.

**Solution:**

a) **Exact solutions:**

**System A:**

Second equation minus first: $(1.0001 - 1)x_2 = 2 - 2 = 0$

$$0.0001 x_2 = 0 \implies x_2 = 0$$

First equation: $x_1 + 0 = 2 \implies x_1 = 2$

**Solution A:** $(x_1, x_2) = (2, 0)$

**System B:**

$$\det = 10(5) - 7(7) = 50 - 49 = 1$$

Using Cramer's rule:
$$y_1 = \frac{\det\begin{bmatrix} 17 & 7 \\ 12 & 5 \end{bmatrix}}{1} = 17(5) - 7(12) = 85 - 84 = 1$$

$$y_2 = \frac{\det\begin{bmatrix} 10 & 17 \\ 7 & 12 \end{bmatrix}}{1} = 10(12) - 17(7) = 120 - 119 = 1$$

**Solution B:** $(y_1, y_2) = (1, 1)$

b) **Condition numbers:**

**For System A:**

$$\mathbf{A}_A = \begin{bmatrix} 1 & 1 \\ 1 & 1.0001 \end{bmatrix}$$

∞-norm: $\|\mathbf{A}\|_\infty = \max_i \sum_j |a_{ij}|$

Row 1: |1| + |1| = 2
Row 2: |1| + |1.0001| = 2.0001

$$\|\mathbf{A}_A\|_\infty = 2.0001$$

For inverse:
$$\det = 1(1.0001) - 1(1) = 0.0001$$

$$\mathbf{A}_A^{-1} = \frac{1}{0.0001}\begin{bmatrix} 1.0001 & -1 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 10001 & -10000 \\ -10000 & 10000 \end{bmatrix}$$

$$\|\mathbf{A}_A^{-1}\|_\infty = \max(|10001| + |-10000|, |-10000| + |10000|) = 20001$$

$$\kappa_\infty(\mathbf{A}_A) = 2.0001 \times 20001 \approx 40,000$$

**Extremely ill-conditioned!**

**For System B:**

$$\|\mathbf{A}_B\|_\infty = \max(17, 12) = 17$$

$$\mathbf{A}_B^{-1} = \frac{1}{1}\begin{bmatrix} 5 & -7 \\ -7 & 10 \end{bmatrix}$$

$$\|\mathbf{A}_B^{-1}\|_\infty = \max(12, 17) = 17$$

$$\kappa_\infty(\mathbf{A}_B) = 17 \times 17 = 289$$

**Moderately conditioned.**

c) **Sensitivity analysis for System A:**

Error bound:
$$\frac{\|\Delta \mathbf{x}\|}{\|\mathbf{x}\|} \leq \kappa(\mathbf{A}) \frac{\|\Delta \mathbf{b}\|}{\|\mathbf{b}\|}$$

With $\|\Delta \mathbf{b}\|_\infty = 0.0001$ and $\|\mathbf{b}\|_\infty = 2$:

$$\frac{\|\Delta \mathbf{x}\|}{\|\mathbf{x}\|} \leq 40000 \times \frac{0.0001}{2} = 40000 \times 0.00005 = 2$$

**The relative error in solution can be up to 200%!**

A tiny 0.005% change in RHS can cause 200% change in solution!

d) **Process design implications:**

1. **Nearly singular matrices** arise when:
   - Specifications are redundant
   - Components have very similar properties
   - Operating points are near phase boundaries
   - Equipment is poorly designed (bypass nearly equal to flow)

2. **Consequences:**
   - Small measurement errors → large calculation errors
   - Numerical solvers may fail or give meaningless results
   - Optimization becomes unreliable
   - Process is difficult to control

3. **Engineering solutions:**
   - **Reformulate problem** - remove redundant equations
   - **Add constraints** that are well-conditioned
   - **Change design** to avoid near-singularity
   - **Use regularization** in numerical methods
   - **Check condition number** before trusting results

4. **Example in distillation:**
   If two components have very similar volatilities (α ≈ 1), the separation matrix becomes ill-conditioned. Small errors in feed composition lead to large errors in predicted product compositions. **Solution:** Use different separation method or add intermediate processing step.

**Key lesson:** Always check matrix condition number when solving process equations. High κ signals physical or mathematical problems requiring attention!

---

## Summary

These exercises demonstrated:
1. **Matrix operations** for material balance bookkeeping
2. **Linear system solution** for separation processes
3. **Eigenanalysis** for reactor stability and dynamics
4. **LU decomposition** for efficient repeated solving
5. **Condition number** for numerical reliability assessment

**Practical PSE skills developed:**
- Formulating balances in matrix form
- Choosing appropriate solution methods
- Interpreting eigenvalues physically
- Recognizing ill-conditioned problems
- Understanding stability from linear analysis
