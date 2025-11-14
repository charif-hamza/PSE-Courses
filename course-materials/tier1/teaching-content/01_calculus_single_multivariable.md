# Calculus: Single and Multivariable Calculus

## Learning Objectives
After mastering this subconcept, you will be able to:
- Understand derivatives and integrals from first principles
- Apply single-variable calculus to rate processes
- Extend calculus concepts to multivariable functions
- Visualize and interpret multivariable functions in PSE contexts
- Apply calculus to real chemical engineering problems

## Prerequisites
- Algebra and trigonometry
- Understanding of functions and graphs
- Basic mathematical reasoning

## 1. Single-Variable Calculus: Building from First Principles

### 1.1 The Derivative: Rate of Change

**Fundamental Definition:**
The derivative of a function f(x) at a point x is defined as:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

**Physical Interpretation in PSE:**
In chemical engineering, the derivative represents a **rate of change**:
- Rate of reaction: how quickly concentration changes with time
- Temperature gradient: how temperature changes with position
- Velocity: how position changes with time

**Example 1: Batch Reactor Concentration**
Consider a first-order reaction in a batch reactor:
$$\frac{dC_A}{dt} = -kC_A$$

This derivative tells us the instantaneous rate at which reactant concentration CA decreases.

### 1.2 Differentiation Rules

Building from the limit definition, we derive key rules:

**Power Rule:**
$$\frac{d}{dx}[x^n] = nx^{n-1}$$

**Product Rule:**
$$\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$$

**Chain Rule:**
$$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

**PSE Application - Arrhenius Equation:**
The rate constant k depends on temperature:
$$k(T) = A e^{-E_a/RT}$$

To find how k changes with T:
$$\frac{dk}{dT} = A e^{-E_a/RT} \cdot \frac{E_a}{RT^2} = k \cdot \frac{E_a}{RT^2}$$

This shows reaction rates are more sensitive to temperature at lower temperatures!

### 1.3 The Integral: Accumulation

**Fundamental Definition:**
The definite integral represents accumulation:

$$\int_a^b f(x)dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*)\Delta x$$

**Physical Interpretation in PSE:**
- Total amount produced: integrating production rate over time
- Heat transferred: integrating heat flux over area
- Work done: integrating force over distance

**Fundamental Theorem of Calculus:**
$$\int_a^b f'(x)dx = f(b) - f(a)$$

This connects rates (derivatives) with accumulation (integrals).

**Example 2: Total Product from Batch Reactor**
If production rate is r(t) = k₀e^(-kt), total product after time T:

$$P_{total} = \int_0^T k_0 e^{-kt} dt = k_0 \left[-\frac{1}{k}e^{-kt}\right]_0^T = \frac{k_0}{k}(1 - e^{-kT})$$

## 2. Multivariable Calculus

### 2.1 Functions of Multiple Variables

In PSE, properties depend on multiple variables:
- Pressure: P(T, V, n) - temperature, volume, moles
- Gibbs energy: G(T, P, composition)
- Reaction rate: r(T, P, C_A, C_B)

**Visualization:**
For f(x,y), we can visualize as:
- 3D surface plot
- Contour plots (level curves)
- Cross-sections

### 2.2 Partial Derivatives

**Definition:**
The partial derivative ∂f/∂x measures how f changes with x **while holding other variables constant**:

$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

**PSE Application - Ideal Gas Law:**
For n moles of ideal gas: PV = nRT

How does pressure change with temperature at constant volume?
$$\left(\frac{\partial P}{\partial T}\right)_V = \frac{nR}{V}$$

How does pressure change with volume at constant temperature?
$$\left(\frac{\partial P}{\partial V}\right)_T = -\frac{nRT}{V^2} = -\frac{P}{V}$$

Notice the subscripts indicating what's held constant - crucial in thermodynamics!

### 2.3 The Chain Rule for Multiple Variables

For z = f(x,y) where x = x(t) and y = y(t):

$$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$

**PSE Application - Temperature Change in Flowing Fluid:**
Temperature T(x,y,t) in a 2D flow field with velocity (u,v):

$$\frac{DT}{Dt} = \frac{\partial T}{\partial t} + u\frac{\partial T}{\partial x} + v\frac{\partial T}{\partial y}$$

This is the **material derivative** - the rate of temperature change following a fluid particle.

### 2.4 Optimization in Multiple Variables

To find extrema of f(x,y):
1. Find critical points where ∇f = 0:
   $$\frac{\partial f}{\partial x} = 0, \quad \frac{\partial f}{\partial y} = 0$$

2. Use second derivative test with Hessian matrix

**PSE Application - Optimal Reactor Temperature:**
For a CSTR with selectivity S(T, τ) depending on temperature and residence time, we maximize by:

$$\frac{\partial S}{\partial T} = 0, \quad \frac{\partial S}{\partial \tau} = 0$$

## 3. Key Theorems and Their PSE Significance

### 3.1 Mean Value Theorem
If f is continuous on [a,b] and differentiable on (a,b), then:
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$ for some c ∈ (a,b)

**PSE Meaning:** The average rate equals the instantaneous rate somewhere in the interval.

### 3.2 Taylor Series
Any smooth function can be approximated:
$$f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + ...$$

**PSE Application:** Linearizing nonlinear models for control system design.

## 4. Integration Techniques Preview

We'll cover in the next section:
- Substitution (change of variables)
- Integration by parts
- Partial fractions
- Applications to area, volume, work

## Physical Intuition Summary

**Single-Variable Calculus:**
- Derivative = instantaneous rate of change
- Integral = accumulation over an interval
- Fundamental theorem connects the two

**Multivariable Calculus:**
- Partial derivatives = rate of change in one direction
- Total differential = change considering all directions
- Gradient points in direction of steepest increase

## Connections to PSE

Every PSE concept involves calculus:
- **Material balances:** Rate in - Rate out = Rate of accumulation (derivatives and integrals)
- **Energy balances:** Same structure, different property
- **Reaction kinetics:** Rates are derivatives
- **Transport phenomena:** Flux equations involve gradients (spatial derivatives)
- **Optimization:** Finding best operating conditions uses derivatives

## Common Pitfalls

1. **Confusing partial and total derivatives** in thermodynamics
2. **Forgetting chain rule** in complex functions
3. **Not checking boundary conditions** in optimization
4. **Mixing up rates and amounts** (derivative vs. function)
5. **Ignoring units** in PSE applications

## Mental Model

Think of calculus as the mathematics of **change and accumulation**:
- Want to know how fast? → Derivative
- Want to know how much total? → Integral
- Multiple factors affecting outcome? → Partial derivatives
- Everything changing together? → Chain rule

In PSE, almost nothing is static - processes are dynamic, conditions vary, and optimization is key. Calculus is the language we use to describe and control these changes.

## Next Steps

After mastering this subconcept through exercises, we'll dive deeper into:
- Advanced integration techniques
- Multiple integrals for 2D/3D systems
- Vector calculus for transport phenomena
- Differential equations for dynamic systems
