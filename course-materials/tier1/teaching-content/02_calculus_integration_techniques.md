# Calculus: Integration Techniques

## Learning Objectives
After mastering this subconcept, you will be able to:
- Apply substitution method to transform integrals
- Use integration by parts for products of functions
- Decompose rational functions using partial fractions
- Select appropriate integration techniques for PSE problems
- Solve complex integrals appearing in reactor and separation design

## Prerequisites
- Understanding of derivatives and basic integration
- Algebraic manipulation skills
- Familiarity with logarithms and exponentials

## 1. Why Integration Techniques Matter in PSE

In process systems engineering, we constantly encounter integrals that aren't straightforward:

**Example PSE Problems Requiring Advanced Integration:**
1. Variable-density batch reactor: ∫ dC/(k₁C + k₂C²) - needs partial fractions
2. Non-isothermal reactor: ∫ exp(-E/RT) dT - needs substitution
3. Work done by gas: ∫ P dV with van der Waals equation - needs algebraic manipulation
4. Residence time distribution: ∫ t·exp(-t/τ) dt - needs integration by parts

## 2. Integration by Substitution (u-substitution)

### 2.1 The Method

**Fundamental Principle:**
If we can write ∫ f(g(x))g'(x)dx, substitute u = g(x):

$$\int f(g(x))g'(x)dx = \int f(u)du$$

where du = g'(x)dx.

**Strategy:**
1. Identify inner function g(x) whose derivative appears
2. Substitute u = g(x), compute du
3. Rewrite integral entirely in terms of u
4. Integrate
5. Substitute back to original variable

### 2.2 PSE Application: Arrhenius Integral

**Problem:** Find total conversion in a non-isothermal batch reactor where temperature increases linearly: T(t) = T₀ + βt

The conversion involves:
$$X = \int_0^t k(T) dt = \int_0^t A\exp\left(-\frac{E_a}{R(T_0 + \beta t)}\right) dt$$

**Solution using substitution:**
Let u = T₀ + βt
Then du = β dt, or dt = du/β

When t = 0: u = T₀
When t = t: u = T₀ + βt = T(t)

$$X = \int_{T_0}^{T(t)} A\exp\left(-\frac{E_a}{Ru}\right) \frac{du}{\beta}$$

$$= \frac{A}{\beta} \int_{T_0}^{T(t)} \exp\left(-\frac{E_a}{Ru}\right) du$$

This can be evaluated numerically or expressed in terms of exponential integrals.

### 2.3 Common Substitutions in PSE

| Integral Form | Substitution | Application |
|---------------|--------------|-------------|
| ∫ f(ax + b) dx | u = ax + b | Linear transformations |
| ∫ x·f(x²) dx | u = x² | Symmetric functions |
| ∫ f(e^x)e^x dx | u = e^x | Exponential reactions |
| ∫ tan(x) dx | u = cos(x) | Trigonometric (rare in PSE) |
| ∫ f(ln x)/x dx | u = ln x | Logarithmic pressure/temp |

## 3. Integration by Parts

### 3.1 The Formula

**Derived from product rule:**
If (uv)' = u'v + uv', then integrating both sides:

$$\int u \, dv = uv - \int v \, du$$

**Selection Strategy (LIATE rule):**
Choose u in this priority order:
1. **L**ogarithmic: ln(x), log(x)
2. **I**nverse trig: arctan(x), arcsin(x)
3. **A**lgebraic: x, x², polynomials
4. **T**rigonometric: sin(x), cos(x)
5. **E**xponential: e^x, e^(ax)

Whatever's left becomes dv.

### 3.2 PSE Application: Mean Residence Time in RTD

**Problem:** Calculate mean residence time from an RTD (residence time distribution) function.

For E(t) = (1/τ)exp(-t/τ), the mean is:

$$\bar{t} = \int_0^\infty t \cdot E(t) \, dt = \int_0^\infty \frac{t}{\tau} e^{-t/\tau} dt$$

**Solution using integration by parts:**

Let u = t, dv = (1/τ)e^(-t/τ) dt

Then: du = dt, v = -e^(-t/τ)

$$\bar{t} = \left[t \cdot (-e^{-t/\tau})\right]_0^\infty - \int_0^\infty (-e^{-t/\tau}) dt$$

The first term vanishes at both limits (using L'Hôpital's rule at ∞):

$$\bar{t} = 0 + \int_0^\infty e^{-t/\tau} dt = \left[-\tau e^{-t/\tau}\right]_0^\infty = \tau$$

**Physical meaning:** For an exponential RTD, mean residence time equals the time constant τ.

### 3.3 Repeated Integration by Parts

**Problem:** Higher moments of RTD require repeated application.

Second moment (for variance calculation):
$$\sigma^2 = \int_0^\infty (t - \bar{t})^2 E(t) \, dt$$

For exponential RTD, this requires integrating t²e^(-t/τ), needing parts twice.

## 4. Partial Fractions

### 4.1 The Method

**Purpose:** Decompose rational functions (ratio of polynomials) into simpler fractions that are easy to integrate.

**General Form:**
$$\frac{P(x)}{Q(x)} = \text{polynomial} + \sum \frac{A_i}{(x - r_i)^k}$$

where r_i are roots of denominator Q(x).

**Key Steps:**
1. If degree(P) ≥ degree(Q), do polynomial long division first
2. Factor denominator completely
3. Write partial fraction decomposition
4. Solve for coefficients (cover-up method or equating coefficients)
5. Integrate term by term

### 4.2 Cases for Partial Fractions

**Case 1: Distinct Linear Factors**
$$\frac{1}{(x-a)(x-b)} = \frac{A}{x-a} + \frac{B}{x-b}$$

**Case 2: Repeated Linear Factors**
$$\frac{1}{(x-a)^2(x-b)} = \frac{A}{x-a} + \frac{B}{(x-a)^2} + \frac{C}{x-b}$$

**Case 3: Irreducible Quadratic Factors**
$$\frac{1}{(x^2+1)(x-a)} = \frac{Ax + B}{x^2+1} + \frac{C}{x-a}$$

### 4.3 PSE Application: CSTR Design Equation

**Problem:** For second-order reaction A → products in a CSTR:

$$\tau = \frac{C_{A0} - C_A}{kC_A^2}$$

Solve for space time τ as a function of conversion X where X = (C_A0 - C_A)/C_A0:

Starting from reaction rate: -r_A = kC_A² = k C_A0²(1-X)²

Design equation: $V = F_{A0} \int_0^X \frac{dX}{-r_A}$

$$\tau = \frac{V}{Q} = C_{A0} \int_0^X \frac{dX}{kC_{A0}^2(1-X)^2} = \frac{1}{kC_{A0}} \int_0^X \frac{dX}{(1-X)^2}$$

This is straightforward, but for complex kinetics like:
$$-r_A = \frac{k_1 C_A}{1 + k_2 C_A}$$

The integral becomes:
$$\tau = C_{A0} \int_0^X \frac{(1 + k_2 C_{A0}(1-X))}{k_1 C_{A0}(1-X)} dX$$

**Another Example: Langmuir Adsorption**

For adsorption with Langmuir isotherm:
$$\frac{dq}{dt} = k_a C(q_{max} - q) - k_d q$$

At equilibrium, dq/dt = 0:
$$k_a C q_{max} = q(k_a C + k_d)$$

To find time to reach q from q₀:
$$\int_{q_0}^q \frac{dq}{k_a C(q_{max} - q) - k_d q} = \int_0^t dt$$

The left side needs partial fractions. Rewrite denominator:
$$k_a C q_{max} - k_a C q - k_d q = k_a C q_{max} - (k_a C + k_d)q$$

Let K = k_a C + k_d:
$$\frac{1}{k_a C q_{max} - Kq}$$

This doesn't need partial fractions (single term), but if we had:
$$\frac{q}{k_a C(q_{max} - q)(b + q)}$$

Then we'd need:
$$\frac{q}{(q_{max} - q)(b + q)} = \frac{A}{q_{max} - q} + \frac{B}{b + q}$$

Solving: $q = A(b + q) + B(q_{max} - q)$

At q = q_max: $q_{max} = A(b + q_{max})$, so $A = \frac{q_{max}}{b + q_{max}}$

At q = -b: $-b = B(q_{max} + b)$, so $B = \frac{-b}{q_{max} + b}$

### 4.4 Partial Fractions for PFR with nth Order Reaction

**Problem:** Plug flow reactor with nth order irreversible reaction.

For n ≠ 1:
$$V = F_{A0} \int_0^X \frac{dX}{k C_{A0}^n (1-X)^n}$$

For n = 2:
$$V = \frac{F_{A0}}{k C_{A0}^2} \int_0^X \frac{dX}{(1-X)^2}$$

$$= \frac{F_{A0}}{k C_{A0}^2} \left[\frac{1}{1-X}\right]_0^X = \frac{F_{A0}}{k C_{A0}^2} \left(\frac{1}{1-X} - 1\right)$$

$$= \frac{F_{A0} X}{k C_{A0}^2 (1-X)}$$

For reversible reactions like A ⇌ B with:
$$-r_A = k_f C_A - k_r C_B$$

The integral:
$$\int \frac{dC_A}{k_f C_A - k_r C_B}$$

With C_B related to C_A by stoichiometry, this becomes a rational function requiring partial fractions if the kinetics are complex.

## 5. Strategy Selection Guide

**Decision Tree for Integration:**

```
Is the integrand a product of functions?
├─ Yes: Try integration by parts
│   └─ Use LIATE to choose u and dv
│
└─ No: Is there a composition f(g(x))?
    ├─ Yes: Is g'(x) present (or easily factored out)?
    │   └─ Yes: Use substitution
    │
    └─ No: Is it a rational function?
        ├─ Yes: Use partial fractions
        │   └─ Factor denominator first
        │
        └─ No: Try:
            - Trigonometric identities
            - Algebraic manipulation
            - Numerical methods
```

## 6. Combined Techniques

Many PSE integrals require multiple techniques in sequence.

**Example: Non-isothermal Van't Hoff equation**

$$\frac{d(\ln K_{eq})}{dT} = \frac{\Delta H_{rxn}}{RT^2}$$

Integrating from T₁ to T₂:
$$\ln K_{eq,2} - \ln K_{eq,1} = \int_{T_1}^{T_2} \frac{\Delta H_{rxn}}{RT^2} dT$$

If ΔH_rxn varies with temperature: ΔH_rxn = a + bT

$$\int \frac{a + bT}{RT^2} dT = \int \left(\frac{a}{RT^2} + \frac{b}{RT}\right) dT$$

First term: $\frac{a}{R} \int T^{-2} dT = -\frac{a}{RT}$

Second term: $\frac{b}{R} \int T^{-1} dT = \frac{b}{R} \ln T$

Result:
$$\ln\frac{K_{eq,2}}{K_{eq,1}} = -\frac{a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) + \frac{b}{R}\ln\frac{T_2}{T_1}$$

## 7. Numerical Integration When Analytical Fails

Some PSE integrals have no closed-form solution:

$$\int_0^t e^{-E_a/(RT(t))} dt$$

with arbitrary T(t) function.

**Methods:**
- Trapezoidal rule
- Simpson's rule
- Gaussian quadrature
- Adaptive methods

These will be covered in Tier 2: Numerical Methods.

## 8. Physical Interpretation of Integration

**Remember:**
- **Definite integral** = accumulated quantity over an interval
- **Indefinite integral** = family of functions whose derivative gives integrand
- **Limits of integration** = boundaries of the process (time, position, composition)

**PSE Context:**
- Integrating reaction rate over time = total conversion
- Integrating heat flux over area = total heat transfer
- Integrating concentration gradient over thickness = mass flux
- Integrating RTD function = probability (must equal 1)

## 9. Common Pitfalls

1. **Forgetting constant of integration** in indefinite integrals
2. **Not checking if substitution produces simpler form**
3. **Choosing wrong u in integration by parts** (violates LIATE)
4. **Arithmetic errors in partial fraction decomposition**
5. **Forgetting to transform limits** when doing u-substitution in definite integrals
6. **Mixing up which variable to integrate** in multivariable problems

## 10. Practice Strategy

To master integration:
1. Recognize patterns (becomes automatic with practice)
2. Try simplest method first
3. Check answer by differentiation
4. Verify physical units and limiting behavior
5. Compare with numerical integration for validation

## Next Steps

After mastering integration techniques, we'll extend to:
- Multiple integrals (double, triple) for 2D/3D systems
- Line and surface integrals for transport phenomena
- Applications to volume, mass, and energy calculations in PSE
