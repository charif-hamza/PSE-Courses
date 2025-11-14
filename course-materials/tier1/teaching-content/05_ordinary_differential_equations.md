# Ordinary Differential Equations (ODEs) for PSE

## Learning Objectives
After mastering this subconcept, you will be able to:
- Classify and solve first-order ODEs using multiple methods
- Solve second-order ODEs with constant coefficients
- Handle systems of ODEs using matrix methods
- Apply numerical methods for ODEs that lack analytical solutions
- Model dynamic PSE systems (batch reactors, transient heat transfer, tank drainage)

## Prerequisites
- Calculus (derivatives and integrals)
- Linear algebra (eigenvalues for systems of ODEs)
- Basic physics (Newton's laws, conservation principles)

## 1. Why ODEs in PSE?

**Ordinary Differential Equations** describe how quantities change with respect to **one** independent variable (usually time or position).

**PSE Applications:**
- **Batch reactors:** How does concentration change with time?
- **Transient heat transfer:** How does temperature evolve?
- **Tank drainage:** How does liquid level decrease?
- **Dynamic pressure drop:** How do flows respond to valve changes?
- **Population balances:** How do particle size distributions evolve?

**Key Distinction:**
- **ODE:** One independent variable (e.g., dC/dt)
- **PDE:** Multiple independent variables (e.g., ∂C/∂t and ∂C/∂x)

## 2. First-Order ODEs

### 2.1 General Form

$$\frac{dy}{dx} = f(x, y)$$

or in chemical engineering notation:

$$\frac{dC}{dt} = r(C, t)$$

### 2.2 Separable ODEs

**Form:** $\frac{dy}{dx} = g(x)h(y)$

**Solution Method:** Separate variables and integrate both sides.

$$\int \frac{dy}{h(y)} = \int g(x) dx$$

### 2.3 PSE Application: First-Order Batch Reactor

**Problem:** Irreversible reaction A → B with rate r = kC_A in a constant-volume batch reactor.

**Material Balance:**
$$\frac{dC_A}{dt} = -kC_A$$

This is separable! Divide both sides by C_A:

$$\frac{dC_A}{C_A} = -k \, dt$$

Integrate from t=0 (C_A = C_A0) to t (C_A = C_A):

$$\int_{C_{A0}}^{C_A} \frac{dC_A}{C_A} = \int_0^t -k \, dt$$

$$\ln C_A - \ln C_{A0} = -kt$$

$$\ln\frac{C_A}{C_{A0}} = -kt$$

$$C_A(t) = C_{A0} e^{-kt}$$

**Physical interpretation:**
- Exponential decay
- Half-life: t₁/₂ = ln(2)/k ≈ 0.693/k
- Time constant: τ = 1/k
- After time 3τ, about 95% reacted

### 2.4 Linear First-Order ODEs

**Standard form:**
$$\frac{dy}{dx} + P(x)y = Q(x)$$

**Solution Method:** Integrating factor

$$\mu(x) = e^{\int P(x) dx}$$

Multiply both sides by μ(x):

$$\mu(x)\frac{dy}{dx} + \mu(x)P(x)y = \mu(x)Q(x)$$

The left side is the derivative of μ(x)y:

$$\frac{d}{dx}[\mu(x)y] = \mu(x)Q(x)$$

Integrate:

$$y(x) = \frac{1}{\mu(x)}\left[\int \mu(x)Q(x) dx + C\right]$$

### 2.5 PSE Application: CSTR with Variable Feed

**Problem:** CSTR with first-order reaction, variable inlet concentration:

$$V\frac{dC}{dt} = QC_{in}(t) - QC - VkC$$

Dividing by V and rearranging:

$$\frac{dC}{dt} + \left(\frac{Q}{V} + k\right)C = \frac{Q}{V}C_{in}(t)$$

This is linear first-order! With constant τ = V/Q:

$$\frac{dC}{dt} + \left(\frac{1}{\tau} + k\right)C = \frac{1}{\tau}C_{in}(t)$$

For step change C_in(t) = C₁ (constant), the solution is:

$$C(t) = \frac{C_1/\tau}{1/\tau + k} + \left(C_0 - \frac{C_1/\tau}{1/\tau + k}\right)e^{-(1/\tau + k)t}$$

where C₀ is initial concentration.

**Physical insight:**
- Approaches new steady state: C_ss = C₁/(1 + kτ)
- Time constant: τ_eff = 1/(1/τ + k)
- Faster response if either flow rate increases (τ↓) or reaction rate increases (k↑)

### 2.6 Exact ODEs

An ODE M(x,y)dx + N(x,y)dy = 0 is **exact** if:

$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

**Solution:** Find function F(x,y) such that:
$$\frac{\partial F}{\partial x} = M, \quad \frac{\partial F}{\partial y} = N$$

Then F(x,y) = C is the solution.

Less common in PSE, but appears in thermodynamic relationships.

## 3. Second-Order ODEs

### 3.1 General Form

$$\frac{d^2y}{dx^2} = f\left(x, y, \frac{dy}{dx}\right)$$

or in standard form:

$$a\frac{d^2y}{dx^2} + b\frac{dy}{dx} + cy = g(x)$$

### 3.2 Homogeneous Linear ODEs with Constant Coefficients

**Form:**
$$a\frac{d^2y}{dx^2} + b\frac{dy}{dx} + cy = 0$$

**Solution Method:** Assume y = e^(rx), substitute:

$$ar^2e^{rx} + bre^{rx} + ce^{rx} = 0$$

Divide by e^(rx):

$$ar^2 + br + c = 0$$

This is the **characteristic equation**.

**Solutions depend on discriminant:** Δ = b² - 4ac

**Case 1: Two distinct real roots** (Δ > 0)

r₁, r₂ real and different:

$$y(x) = C_1 e^{r_1 x} + C_2 e^{r_2 x}$$

**Case 2: Repeated real root** (Δ = 0)

r₁ = r₂ = r:

$$y(x) = (C_1 + C_2 x)e^{rx}$$

**Case 3: Complex conjugate roots** (Δ < 0)

r = α ± iβ:

$$y(x) = e^{\alpha x}(C_1\cos(\beta x) + C_2\sin(\beta x))$$

### 3.3 PSE Application: Pressure Dynamics in Pipeline

**Problem:** Pressure wave propagation in a gas pipeline can be modeled (linearized) as:

$$\frac{d^2P}{dx^2} - \frac{1}{c^2}\frac{d^2P}{dt^2} = 0$$

For steady oscillations P(x,t) = p(x)e^(iωt), this reduces to:

$$\frac{d^2p}{dx^2} + \frac{\omega^2}{c^2}p = 0$$

Characteristic equation: $r^2 + \omega^2/c^2 = 0$

$$r = \pm i\frac{\omega}{c}$$

Complex roots! Solution:

$$p(x) = A\cos\left(\frac{\omega x}{c}\right) + B\sin\left(\frac{\omega x}{c}\right)$$

**Physical meaning:**
- Waves propagate at speed c
- Frequency ω determines wavelength λ = 2πc/ω
- Boundary conditions determine A and B

### 3.4 Non-Homogeneous ODEs: Method of Undetermined Coefficients

**Form:**
$$ay'' + by' + cy = g(x)$$

**Solution:** y = y_h + y_p

where:
- y_h: homogeneous solution (from characteristic equation)
- y_p: particular solution (guess based on g(x))

**Common forms for y_p:**

| g(x) | Try y_p |
|------|---------|
| Polynomial (degree n) | Polynomial (degree n) |
| e^(ax) | Ae^(ax) |
| sin(ωx) or cos(ωx) | A sin(ωx) + B cos(ωx) |
| x^n e^(ax) | (polynomial)e^(ax) |

If guess matches homogeneous solution, multiply by x.

### 3.5 PSE Application: Forced Oscillations in Control System

**Problem:** A controlled process responds to sinusoidal setpoint changes:

$$\frac{d^2y}{dt^2} + 2\zeta\omega_n\frac{dy}{dt} + \omega_n^2 y = \omega_n^2 \sin(\omega t)$$

where:
- ζ: damping ratio
- ω_n: natural frequency
- ω: forcing frequency

**Homogeneous solution:** (depends on ζ)

For ζ < 1 (underdamped, typical):
$$y_h = e^{-\zeta\omega_n t}(A\cos(\omega_d t) + B\sin(\omega_d t))$$

where $\omega_d = \omega_n\sqrt{1-\zeta^2}$ (damped frequency)

**Particular solution:** Try $y_p = C\sin(\omega t) + D\cos(\omega t)$

After substitution and solving:

$$y_p = \frac{\omega_n^2}{(\omega_n^2 - \omega^2)^2 + (2\zeta\omega_n\omega)^2}^{1/2} \sin(\omega t - \phi)$$

where φ is phase shift.

**Physical interpretation:**
- Transient dies out (e^(-ζω_n t) → 0)
- Steady-state oscillation at forcing frequency ω
- **Resonance** when ω ≈ ω_n: amplitude maximum
- Higher damping ζ reduces resonance peak

Critical for control system design!

## 4. Systems of ODEs

### 4.1 Matrix Form

For n coupled first-order ODEs:

$$\frac{d\mathbf{x}}{dt} = \mathbf{Ax} + \mathbf{f}(t)$$

where:
- x: n×1 state vector
- A: n×n system matrix
- f(t): n×1 forcing function

### 4.2 Homogeneous Systems (f = 0)

$$\frac{d\mathbf{x}}{dt} = \mathbf{Ax}$$

**Solution using eigenvalues:**

1. Find eigenvalues λ_i and eigenvectors v_i of A
2. General solution:

$$\mathbf{x}(t) = \sum_{i=1}^n c_i e^{\lambda_i t} \mathbf{v}_i$$

where c_i determined by initial conditions.

**For real eigenvalues:**
Each mode evolves as e^(λᵢt)

**For complex eigenvalues λ = α ± iβ:**
Mode evolves as e^(αt)[cos(βt) + sin(βt)]

### 4.3 PSE Application: Two CSTRs in Series

**Problem:** Two reactors in series, first-order reaction in each:

Reactor 1: $V_1\frac{dC_1}{dt} = QC_0 - QC_1 - V_1 k_1 C_1$

Reactor 2: $V_2\frac{dC_2}{dt} = QC_1 - QC_2 - V_2 k_2 C_2$

Define τ₁ = V₁/Q, τ₂ = V₂/Q:

$$\frac{dC_1}{dt} = \frac{C_0}{\tau_1} - \left(\frac{1}{\tau_1} + k_1\right)C_1$$

$$\frac{dC_2}{dt} = \frac{C_1}{\tau_2} - \left(\frac{1}{\tau_2} + k_2\right)C_2$$

For homogeneous system (C₀ = 0), matrix form:

$$\frac{d}{dt}\begin{bmatrix} C_1 \\ C_2 \end{bmatrix} = \begin{bmatrix} -(1/\tau_1 + k_1) & 0 \\ 1/\tau_2 & -(1/\tau_2 + k_2) \end{bmatrix} \begin{bmatrix} C_1 \\ C_2 \end{bmatrix}$$

**Eigenvalues:**

Matrix is triangular! Eigenvalues are diagonal elements:

$$\lambda_1 = -(1/\tau_1 + k_1), \quad \lambda_2 = -(1/\tau_2 + k_2)$$

Both negative → **system is stable**

**Solution:**

$$C_1(t) = C_{1,0} e^{\lambda_1 t}$$

$$C_2(t) = \frac{C_{1,0}/\tau_2}{\lambda_2 - \lambda_1}(e^{\lambda_1 t} - e^{\lambda_2 t}) + C_{2,0} e^{\lambda_2 t}$$

**Physical interpretation:**
- C₁ decays exponentially (single exponential)
- C₂ shows cascade behavior: rises then falls (difference of exponentials)
- Faster decay (more negative λ) dominates long-term

### 4.4 Converting Higher-Order ODEs to Systems

**Any nth-order ODE can be rewritten as n first-order ODEs.**

**Example:** Second-order ODE
$$\frac{d^2y}{dt^2} + a\frac{dy}{dt} + by = 0$$

Define: $x_1 = y$, $x_2 = \frac{dy}{dt}$

Then:
$$\frac{dx_1}{dt} = x_2$$

$$\frac{dx_2}{dt} = -ax_2 - bx_1$$

Matrix form:

$$\frac{d}{dt}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -b & -a \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$

This allows using matrix methods and numerical solvers designed for first-order systems.

## 5. Numerical Methods for ODEs

When analytical solutions don't exist or are too complex, use numerical methods.

### 5.1 Euler's Method (Simplest)

$$y_{n+1} = y_n + h f(x_n, y_n)$$

where h = step size

**Pros:** Simple, easy to understand
**Cons:** Low accuracy (O(h)), unstable for stiff equations

### 5.2 Runge-Kutta Methods

**RK4 (4th-order Runge-Kutta):** Most popular

$$k_1 = f(x_n, y_n)$$
$$k_2 = f(x_n + h/2, y_n + hk_1/2)$$
$$k_3 = f(x_n + h/2, y_n + hk_2/2)$$
$$k_4 = f(x_n + h, y_n + hk_3)$$

$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

**Pros:** High accuracy (O(h⁴)), good stability
**Cons:** More function evaluations per step

### 5.3 PSE Application: Batch Reactor with Complex Kinetics

**Problem:** Multiple reactions with non-linear kinetics:

A + B → C (rate = k₁C_A C_B)
2C → D (rate = k₂C_C²)

$$\frac{dC_A}{dt} = -k_1 C_A C_B$$

$$\frac{dC_B}{dt} = -k_1 C_A C_B$$

$$\frac{dC_C}{dt} = k_1 C_A C_B - 2k_2 C_C^2$$

$$\frac{dC_D}{dt} = k_2 C_C^2$$

**No analytical solution!** Use RK4:

```python
import numpy as np
from scipy.integrate import odeint

def batch_reactor(C, t, k1, k2):
    CA, CB, CC, CD = C
    dCAdt = -k1 * CA * CB
    dCBdt = -k1 * CA * CB
    dCCdt = k1 * CA * CB - 2*k2 * CC**2
    dCDdt = k2 * CC**2
    return [dCAdt, dCBdt, dCCdt, dCDdt]

# Initial conditions
C0 = [1.0, 1.5, 0.0, 0.0]  # mol/L
k1, k2 = 0.5, 0.1  # L/(mol·min)

# Time span
t = np.linspace(0, 20, 200)

# Solve
solution = odeint(batch_reactor, C0, t, args=(k1, k2))
```

### 5.4 Stiff ODEs

**Stiff systems:** Multiple timescales (fast and slow dynamics)

**Example:** Fast reaction coupled with slow heat transfer

**Problem:** Explicit methods (Euler, RK4) require tiny steps → very slow

**Solution:** Implicit methods (backward Euler, BDF)

**In Python:** Use `solve_ivp` with `method='BDF'` or `method='Radau'`

```python
from scipy.integrate import solve_ivp

sol = solve_ivp(batch_reactor, [0, 20], C0,
                method='BDF', args=(k1, k2))
```

## 6. Boundary Value Problems (BVPs)

**Initial Value Problem (IVP):** Given y(x₀), find y(x) for x > x₀

**Boundary Value Problem (BVP):** Given conditions at multiple points

**PSE Example:** Steady-state temperature in a rod with heat generation

$$\frac{d^2T}{dx^2} + \frac{\dot{q}}{k} = 0$$

Boundaries: T(0) = T₁, T(L) = T₂

**Solution methods:**
1. **Shooting method:** Guess initial slope, solve IVP, adjust until boundary met
2. **Finite difference:** Discretize domain, solve system of algebraic equations

## 7. Special Topics for PSE

### 7.1 Phase Plane Analysis

For autonomous systems $\frac{dx}{dt} = f(x,y)$, $\frac{dy}{dt} = g(x,y)$:

- Plot trajectories in (x,y) space
- Find equilibrium points: f = 0, g = 0
- Classify equilibria using Jacobian eigenvalues:
  - Stable node: both λ < 0 (real)
  - Unstable node: both λ > 0
  - Saddle point: λ₁ < 0, λ₂ > 0
  - Stable spiral: Re(λ) < 0 (complex)
  - Center: Re(λ) = 0 (complex, marginal stability)

**PSE Use:** Analyzing CSTR multiple steady states, predator-prey in ecosystems

### 7.2 Limit Cycles

Periodic solutions that attract or repel nearby trajectories.

**Example:** Oscillating chemical reactions (Belousov-Zhabotinsky)

**Engineering concern:** Unwanted oscillations in control systems

### 7.3 Linearization

For non-linear ODE near equilibrium x*:

$$\frac{dx}{dt} = f(x)$$

Taylor expand: $f(x) \approx f(x^*) + f'(x^*)(x - x^*)$

Since f(x*) = 0 at equilibrium:

$$\frac{d(\delta x)}{dt} \approx f'(x^*) \delta x$$

where δx = x - x*.

**Local stability determined by f'(x*)** (or Jacobian for systems)

## 8. Common Pitfalls

1. **Forgetting initial conditions:** ODEs have infinitely many solutions; ICs select one
2. **Wrong sign in characteristic equation:** Check ar² + br + c = 0 carefully
3. **Confusing particular and homogeneous solutions:** Total = homogeneous + particular
4. **Unstable numerical methods:** Use implicit methods for stiff systems
5. **Not checking eigenvalues for stability:** Re(λ) < 0 for all λ required
6. **Units!** Always track units through derivation

## 9. Summary

**First-Order ODEs:**
- Separable: separate and integrate
- Linear: integrating factor method
- Applications: batch reactors, CSTR dynamics, tank drainage

**Second-Order ODEs:**
- Characteristic equation determines solution form
- Real roots → exponentials
- Complex roots → oscillations
- Applications: wave equations, control systems, vibrations

**Systems of ODEs:**
- Use eigenvalue decomposition
- Stability from eigenvalues
- Convert higher-order to first-order system
- Applications: multiple reactors, non-isothermal systems

**Numerical Methods:**
- Euler: simple but inaccurate
- RK4: good general purpose
- BDF/implicit: for stiff systems
- Always validate against analytical solution when possible

## Next Steps

With ODE mastery, you're prepared for:
- Partial Differential Equations (distributed systems)
- Advanced control theory (state-space, MPC)
- Dynamic process simulation
- Transient analysis of processes
