# Linear Algebra: Foundations for PSE

## Learning Objectives
After mastering this subconcept, you will be able to:
- Perform matrix operations and understand their properties
- Solve systems of linear equations using multiple methods
- Calculate and interpret eigenvalues and eigenvectors
- Apply matrix decompositions for computational efficiency
- Use linear algebra in material balances and process modeling

## Prerequisites
- Basic algebra and equation solving
- Understanding of vectors and coordinate systems
- Familiarity with summation notation

## 1. Why Linear Algebra in PSE?

Linear algebra is fundamental to PSE because:

1. **Material balances** → systems of linear equations
2. **Energy balances** → matrix formulations
3. **Linearized models** → matrix differential equations
4. **Process control** → state-space representation
5. **Optimization** → linear programming
6. **Data analysis** → principal component analysis (PCA)

**Core Insight:** Most PSE problems involve multiple variables with linear relationships, making matrices the natural mathematical language.

## 2. Matrices and Vectors

### 2.1 Definitions

**Vector:** Ordered list of numbers (column vector default)
$$\vec{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$$

**Matrix:** Rectangular array of numbers
$$\mathbf{A} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}$$

Dimensions: m × n (m rows, n columns)

### 2.2 Matrix Operations

**Addition:** (same dimensions)
$$(\mathbf{A} + \mathbf{B})_{ij} = a_{ij} + b_{ij}$$

**Scalar Multiplication:**
$$(c\mathbf{A})_{ij} = c \cdot a_{ij}$$

**Matrix Multiplication:** (A is m×n, B is n×p → AB is m×p)
$$(\mathbf{AB})_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$$

**Critical:** Matrix multiplication is **not commutative**: AB ≠ BA in general!

### 2.3 Special Matrices

**Identity Matrix:**
$$\mathbf{I} = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}$$

Property: $\mathbf{AI} = \mathbf{IA} = \mathbf{A}$

**Transpose:** Flip rows and columns
$$(\mathbf{A}^T)_{ij} = a_{ji}$$

**Symmetric Matrix:** $\mathbf{A} = \mathbf{A}^T$

**Diagonal Matrix:** Non-zero only on diagonal

**Inverse Matrix:** $\mathbf{A}^{-1}$ satisfies:
$$\mathbf{AA}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$$

(Only exists if matrix is square and non-singular)

### 2.4 PSE Application: Material Balance Matrix

**Problem:** A process has 3 streams mixing. Conservation of 3 components:

Stream 1: 10 kg/s with [30% A, 50% B, 20% C]
Stream 2: x kg/s with [60% A, 20% B, 20% C]
Stream 3 (exit): (10+x) kg/s with [y_A, y_B, y_C]

Material balances in matrix form:

$$\begin{bmatrix}
0.30 & 0.60 \\
0.50 & 0.20 \\
0.20 & 0.20
\end{bmatrix}
\begin{bmatrix} 10 \\ x \end{bmatrix}
=
\begin{bmatrix} y_A \\ y_B \\ y_C \end{bmatrix}
(10 + x)$$

This shows how material balances naturally lead to matrix equations!

## 3. Systems of Linear Equations

### 3.1 Matrix Form

General system:
$$\begin{cases}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
\end{cases}$$

**Matrix notation:**
$$\mathbf{Ax} = \mathbf{b}$$

where A is coefficient matrix, x is unknown vector, b is right-hand side.

### 3.2 Solution Methods

**Method 1: Matrix Inversion**

If A is square and invertible:
$$\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$$

**Method 2: Gaussian Elimination**

Transform [A | b] to row echelon form through elementary row operations:
1. Swap rows
2. Multiply row by non-zero scalar
3. Add multiple of one row to another

**Method 3: LU Decomposition**

Factor A = LU (Lower × Upper triangular)
- Solve Ly = b (forward substitution)
- Solve Ux = y (backward substitution)

### 3.3 PSE Application: Multi-Component Distillation

**Problem:** Four-component distillation column with specified recoveries.

Let x_i = flow rate of component i in distillate (mol/s)
Feed: [10, 20, 30, 40] mol/s of components [A, B, C, D]

Specifications:
- 95% of A in distillate
- 90% of B in distillate
- 10% of C in distillate
- 5% of D in distillate

Material balances:
$$\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} x_A \\ x_B \\ x_C \\ x_D \end{bmatrix}
=
\begin{bmatrix} 0.95 \times 10 \\ 0.90 \times 20 \\ 0.10 \times 30 \\ 0.05 \times 40 \end{bmatrix}
=
\begin{bmatrix} 9.5 \\ 18 \\ 3 \\ 2 \end{bmatrix}$$

This is trivial (diagonal matrix), but with inter-component interactions or energy balance coupling, the matrix becomes full and non-trivial!

### 3.4 Determinant and Singularity

**Determinant** (for square matrix): Scalar value that indicates:
- det(A) ≠ 0: Matrix is invertible (unique solution exists)
- det(A) = 0: Matrix is singular (no unique solution)

**2×2 case:**
$$\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$

**3×3 case (cofactor expansion):**
$$\det\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix} = a(ei - fh) - b(di - fg) + c(dh - eg)$$

**Physical meaning in PSE:** A singular matrix means equations are linearly dependent - redundant or conflicting specifications!

## 4. Eigenvalues and Eigenvectors

### 4.1 Definition

For square matrix A, **eigenvector** v and **eigenvalue** λ satisfy:
$$\mathbf{Av} = \lambda \mathbf{v}$$

**Meaning:** Transformation A stretches v by factor λ without changing direction.

### 4.2 Finding Eigenvalues

Solve characteristic equation:
$$\det(\mathbf{A} - \lambda \mathbf{I}) = 0$$

This gives polynomial in λ (degree n for n×n matrix).

**Example:**
$$\mathbf{A} = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$$

$$\det\begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} = (4-\lambda)(3-\lambda) - 2 = 0$$

$$\lambda^2 - 7\lambda + 10 = 0$$

$$(\lambda - 5)(\lambda - 2) = 0$$

Eigenvalues: λ₁ = 5, λ₂ = 2

### 4.3 Finding Eigenvectors

For each λ, solve (A - λI)v = 0:

**For λ₁ = 5:**
$$\begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Solution: $v_1 = v_2$, so eigenvector is $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ (or any scalar multiple)

**For λ₂ = 2:**
$$\begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Solution: $v_2 = -2v_1$, so eigenvector is $\mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$

### 4.4 PSE Application: Stability Analysis

**Problem:** Two CSTRs in series with recycle. Linearized dynamics:

$$\frac{d}{dt}\begin{bmatrix} C_1 \\ C_2 \end{bmatrix} = \begin{bmatrix} -3 & 1 \\ 2 & -4 \end{bmatrix} \begin{bmatrix} C_1 \\ C_2 \end{bmatrix}$$

**Stability criterion:** System is stable if all eigenvalues have **negative real parts**.

Characteristic equation:
$$\det\begin{bmatrix} -3-\lambda & 1 \\ 2 & -4-\lambda \end{bmatrix} = 0$$

$$(-3-\lambda)(-4-\lambda) - 2 = 0$$

$$\lambda^2 + 7\lambda + 10 = 0$$

$$\lambda = \frac{-7 \pm \sqrt{49-40}}{2} = \frac{-7 \pm 3}{2}$$

λ₁ = -2, λ₂ = -5

**Both negative → System is stable!** Disturbances decay exponentially.

**Physical interpretation:**
- λ₁ = -2: Fast mode (decays as e^(-2t), half-life ≈ 0.35 time units)
- λ₂ = -5: Slow mode (decays as e^(-5t), half-life ≈ 0.14 time units)

The eigenvectors tell us the directions of these modes in concentration space.

## 5. Matrix Decompositions

### 5.1 LU Decomposition

Factor A into Lower × Upper triangular:
$$\mathbf{A} = \mathbf{LU}$$

**Use:** Efficiently solve Ax = b for multiple right-hand sides.

**Example:**
$$\mathbf{A} = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}$$

$$\mathbf{L} = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{bmatrix}, \quad \mathbf{U} = \begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{bmatrix}$$

### 5.2 Eigenvalue Decomposition (Diagonalization)

For matrix with n independent eigenvectors:
$$\mathbf{A} = \mathbf{V\Lambda V}^{-1}$$

where:
- V = matrix with eigenvectors as columns
- Λ = diagonal matrix of eigenvalues

**Use:** Solve differential equations, compute matrix powers A^k.

**PSE Application - Solving ODEs:**

For $\frac{d\mathbf{x}}{dt} = \mathbf{Ax}$:

Transform to eigenbasis: y = V^(-1)x

$$\frac{d\mathbf{y}}{dt} = \mathbf{\Lambda y}$$

This decouples into independent equations:
$$\frac{dy_i}{dt} = \lambda_i y_i \implies y_i(t) = y_i(0) e^{\lambda_i t}$$

Transform back: x(t) = V y(t)

### 5.3 Singular Value Decomposition (SVD)

Any m×n matrix can be factored:
$$\mathbf{A} = \mathbf{U \Sigma V}^T$$

where:
- U: m×m orthogonal (left singular vectors)
- Σ: m×n diagonal (singular values)
- V: n×n orthogonal (right singular vectors)

**Uses in PSE:**
- Principal Component Analysis (PCA)
- Dimensionality reduction
- Noise filtering in process data
- Model order reduction

## 6. Matrix Norms and Conditioning

### 6.1 Vector Norms

**Euclidean norm (L2):**
$$\|\mathbf{x}\|_2 = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$$

**Maximum norm (L∞):**
$$\|\mathbf{x}\|_\infty = \max_i |x_i|$$

### 6.2 Matrix Norms

**Induced norm:**
$$\|\mathbf{A}\| = \max_{\mathbf{x} \neq 0} \frac{\|\mathbf{Ax}\|}{\|\mathbf{x}\|}$$

**Frobenius norm:**
$$\|\mathbf{A}\|_F = \sqrt{\sum_{i,j} a_{ij}^2}$$

### 6.3 Condition Number

$$\kappa(\mathbf{A}) = \|\mathbf{A}\| \cdot \|\mathbf{A}^{-1}\|$$

**Interpretation:**
- κ ≈ 1: Well-conditioned (small input errors → small output errors)
- κ >> 1: Ill-conditioned (small input errors → large output errors)

**PSE Implication:** Ill-conditioned material balance matrices indicate redundant or nearly-dependent specifications - numerical solution will be unreliable!

## 7. Special Topics for PSE

### 7.1 Sparse Matrices

**Definition:** Mostly zeros (common in large process flowsheets).

**Special storage:** Only store non-zero elements.

**Special solvers:** Exploit sparsity for efficiency (important for 1000+ equations).

### 7.2 Positive Definite Matrices

Matrix A is **positive definite** if:
$$\mathbf{x}^T \mathbf{Ax} > 0 \quad \forall \mathbf{x} \neq 0$$

**Properties:**
- All eigenvalues are positive
- Unique minimum exists in optimization
- Cholesky decomposition available (faster than LU)

**PSE:** Hessian matrices in optimization should be positive definite at minimum.

### 7.3 State-Space Representation

Dynamic PSE systems often written as:
$$\frac{d\mathbf{x}}{dt} = \mathbf{Ax} + \mathbf{Bu}$$
$$\mathbf{y} = \mathbf{Cx} + \mathbf{Du}$$

where:
- x = state vector (compositions, temperatures, etc.)
- u = input vector (feed rates, heating, etc.)
- y = output vector (measurements)
- A, B, C, D = system matrices

**Linear algebra tools:**
- Eigenvalues of A → stability
- Controllability matrix → can we control all states?
- Observability matrix → can we measure all states?

## 8. Practical Computational Aspects

### 8.1 Solving Linear Systems in Python

```python
import numpy as np

# Define system Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Method 1: Direct solve (uses LU internally)
x = np.linalg.solve(A, b)

# Method 2: Matrix inverse (less efficient, avoid)
x = np.linalg.inv(A) @ b  # @ is matrix multiplication

# Method 3: Least squares (overdetermined systems)
x = np.linalg.lstsq(A, b, rcond=None)[0]
```

### 8.2 Eigenvalue Calculation

```python
# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Check stability (all eigenvalues negative real part)
is_stable = np.all(np.real(eigenvalues) < 0)
```

### 8.3 When to Use Which Method

- **Small systems (<100 equations):** Direct solve
- **Large sparse systems:** Iterative methods (conjugate gradient, GMRES)
- **Multiple right-hand sides:** LU decomposition once, then reuse
- **Least squares fit:** SVD or QR decomposition
- **Stability analysis:** Eigenvalue decomposition

## 9. Summary and Connections

**Linear Algebra provides:**
1. **Compact notation** for multi-equation systems
2. **Efficient solution methods** for large problems
3. **Stability analysis** through eigenvalues
4. **Data analysis tools** (SVD, PCA)
5. **Foundation for numerical methods** (Tier 2)

**PSE Applications:**
- Material and energy balances
- Process control state-space models
- Optimization (linear programming)
- Data reconciliation
- Fault detection
- Model reduction

## 10. Common Pitfalls

1. **Matrix multiplication not commutative:** AB ≠ BA
2. **Dimensions must match:** Can't add 2×3 and 3×2 matrices
3. **Inverse doesn't always exist:** Check determinant ≠ 0
4. **Numerical errors accumulate:** Use stable algorithms
5. **Condition number matters:** Check before solving
6. **Units in material balances:** All equations must be consistent

## Next Steps

Build on linear algebra with:
- Ordinary Differential Equations (ODEs)
- Optimization theory
- Numerical linear algebra methods
- Control systems (state-space)
