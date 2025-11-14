# Exercises: Single and Multivariable Calculus

## Exercise 1: Direct Application (Easy)

**Problem:**
A first-order reaction occurs in a batch reactor with rate constant k = 0.15 min⁻¹. The concentration of reactant A follows:
$$C_A(t) = C_{A0} e^{-kt}$$

where C_A0 = 2.0 mol/L.

a) Find the rate of change of concentration at t = 5 minutes.
b) Calculate the total amount of A consumed in the first 10 minutes (assume constant volume V = 100 L).

**Solution:**

a) The rate of change is the derivative:
$$\frac{dC_A}{dt} = C_{A0}(-k)e^{-kt} = -kC_A(t)$$

At t = 5 min:
$$C_A(5) = 2.0 \cdot e^{-0.15 \times 5} = 2.0 \cdot e^{-0.75} = 0.944 \text{ mol/L}$$

$$\frac{dC_A}{dt}\bigg|_{t=5} = -0.15 \times 0.944 = -0.142 \text{ mol/(L·min)}$$

The negative sign indicates concentration is decreasing.

b) Initial moles: n₀ = C_A0 × V = 2.0 × 100 = 200 mol

Final concentration at t = 10 min:
$$C_A(10) = 2.0 \cdot e^{-0.15 \times 10} = 2.0 \cdot e^{-1.5} = 0.446 \text{ mol/L}$$

Final moles: n(10) = 0.446 × 100 = 44.6 mol

Moles consumed: 200 - 44.6 = **155.4 mol**

Alternatively, using integration:
$$\text{Moles consumed} = V\int_0^{10} \left|\frac{dC_A}{dt}\right| dt = V \cdot C_{A0}(1 - e^{-kt})$$
$$= 100 \times 2.0 \times (1 - e^{-1.5}) = 200(1 - 0.223) = 155.4 \text{ mol}$$

---

## Exercise 2: One-Step Reasoning (Moderate)

**Problem:**
The Arrhenius equation describes how reaction rate constant k depends on temperature T:
$$k(T) = A e^{-E_a/(RT)}$$

where A = 1.5 × 10⁸ min⁻¹, E_a = 75,000 J/mol, R = 8.314 J/(mol·K).

a) Calculate dk/dT at T = 350 K. What are the units?
b) If temperature increases by 2 K from 350 K, estimate the change in k using linear approximation.
c) Compare your estimate with the exact value. Explain any difference.

**Solution:**

a) Using the chain rule:
$$\frac{dk}{dT} = A e^{-E_a/(RT)} \cdot \frac{d}{dT}\left[-\frac{E_a}{RT}\right]$$

$$\frac{d}{dT}\left[-\frac{E_a}{RT}\right] = -E_a \cdot \left(-\frac{1}{RT^2}\right) = \frac{E_a}{RT^2}$$

Therefore:
$$\frac{dk}{dT} = k(T) \cdot \frac{E_a}{RT^2}$$

At T = 350 K:
$$k(350) = 1.5 \times 10^8 \exp\left(-\frac{75000}{8.314 \times 350}\right) = 1.5 \times 10^8 \exp(-25.79)$$
$$k(350) = 1.5 \times 10^8 \times 5.11 \times 10^{-12} = 7.67 \times 10^{-4} \text{ min}^{-1}$$

$$\frac{dk}{dT}\bigg|_{T=350} = 7.67 \times 10^{-4} \times \frac{75000}{8.314 \times 350^2}$$
$$= 7.67 \times 10^{-4} \times 0.0737 = 5.65 \times 10^{-5} \text{ min}^{-1}\text{K}^{-1}$$

b) Linear approximation (first-order Taylor series):
$$k(352) \approx k(350) + \frac{dk}{dT}\bigg|_{T=350} \times \Delta T$$
$$k(352) \approx 7.67 \times 10^{-4} + 5.65 \times 10^{-5} \times 2$$
$$k(352) \approx 7.67 \times 10^{-4} + 1.13 \times 10^{-4} = 8.80 \times 10^{-4} \text{ min}^{-1}$$

Change in k: Δk ≈ 1.13 × 10⁻⁴ min⁻¹

c) Exact value:
$$k(352) = 1.5 \times 10^8 \exp\left(-\frac{75000}{8.314 \times 352}\right) = 8.82 \times 10^{-4} \text{ min}^{-1}$$

Error: (8.82 - 8.80)/8.82 × 100% = 0.23%

The linear approximation is excellent for small temperature changes because the exponential function is locally well-approximated by its tangent line. For larger ΔT, higher-order terms would be needed.

**Physical insight:** A 2 K increase at 350 K causes about 15% increase in rate constant - reaction kinetics are very temperature-sensitive!

---

## Exercise 3: Multi-Step Integration (Moderate-Challenging)

**Problem:**
A CSTR (Continuous Stirred Tank Reactor) operates at steady state with a second-order reaction: 2A → B. The design equation is:

$$\tau = \frac{C_{A0} - C_A}{kC_A^2}$$

where τ is residence time, k = 0.05 L/(mol·min), C_A0 = 4.0 mol/L.

a) Find ∂C_A/∂τ and ∂C_A/∂C_A0 (implicit differentiation required).
b) If C_A0 increases by 0.2 mol/L and τ increases by 1 min from the operating point (τ = 10 min, C_A0 = 4.0 mol/L), estimate the change in C_A using the total differential.
c) What is the physical interpretation of each partial derivative?

**Solution:**

a) Starting with: $\tau = \frac{C_{A0} - C_A}{kC_A^2}$

Rearrange: $kC_A^2 \tau = C_{A0} - C_A$

Or: $kC_A^2 \tau + C_A - C_{A0} = 0$

This is an implicit function: F(τ, C_A0, C_A) = 0

**Finding ∂C_A/∂τ:**
Differentiate with respect to τ, treating C_A as a function of τ:

$$k\frac{\partial}{\partial \tau}[C_A^2 \tau] + \frac{\partial C_A}{\partial \tau} = 0$$

$$k\left(2C_A \frac{\partial C_A}{\partial \tau} \cdot \tau + C_A^2\right) + \frac{\partial C_A}{\partial \tau} = 0$$

$$\frac{\partial C_A}{\partial \tau}(2kC_A\tau + 1) = -kC_A^2$$

$$\frac{\partial C_A}{\partial \tau} = -\frac{kC_A^2}{2kC_A\tau + 1}$$

**Finding ∂C_A/∂C_A0:**
Differentiate with respect to C_A0:

$$2kC_A\tau \frac{\partial C_A}{\partial C_{A0}} + \frac{\partial C_A}{\partial C_{A0}} - 1 = 0$$

$$\frac{\partial C_A}{\partial C_{A0}} = \frac{1}{2kC_A\tau + 1}$$

First, find C_A at operating point using the design equation:
$$10 = \frac{4.0 - C_A}{0.05 \times C_A^2}$$

$$0.5C_A^2 = 4.0 - C_A$$

$$0.5C_A^2 + C_A - 4.0 = 0$$

$$C_A = \frac{-1 \pm \sqrt{1 + 8}}{1} = \frac{-1 + 3}{1} = 2.0 \text{ mol/L}$$

Now evaluate partial derivatives at (τ = 10 min, C_A = 2.0 mol/L, C_A0 = 4.0 mol/L):

$$\frac{\partial C_A}{\partial \tau} = -\frac{0.05 \times 4.0}{2 \times 0.05 \times 2.0 \times 10 + 1} = -\frac{0.2}{3} = -0.0667 \text{ mol/(L·min)}$$

$$\frac{\partial C_A}{\partial C_{A0}} = \frac{1}{3} = 0.333$$

b) Total differential:
$$dC_A = \frac{\partial C_A}{\partial \tau}d\tau + \frac{\partial C_A}{\partial C_{A0}}dC_{A0}$$

$$\Delta C_A \approx (-0.0667)(1) + (0.333)(0.2)$$
$$\Delta C_A \approx -0.0667 + 0.0667 = 0$$

The two effects cancel out!

c) **Physical interpretations:**

- **∂C_A/∂τ < 0**: Increasing residence time decreases outlet concentration (more reaction, more conversion). The reactor has more time to convert A to B.

- **∂C_A/∂C_A0 > 0**: Increasing feed concentration increases outlet concentration. Even though fractional conversion may decrease (second-order kinetics), the absolute outlet concentration increases.

- **Magnitude comparison**: |∂C_A/∂C_A0| = 0.333 means a 1 mol/L increase in feed gives only 0.333 mol/L increase in outlet - the rest is converted due to the higher driving force for reaction.

---

## Exercise 4: PSE Context Application (Challenging)

**Problem:**
A heat exchanger operates with overall heat transfer coefficient U that depends on temperatures:

$$U(T_h, T_c) = U_0\left(1 + \alpha\frac{T_h + T_c}{2}\right)$$

where U₀ = 500 W/(m²·K), α = 0.002 K⁻¹, T_h is hot fluid temperature, T_c is cold fluid temperature.

The heat transfer rate is:
$$Q = U(T_h, T_c) \cdot A \cdot \Delta T_{lm}$$

where A = 25 m² and the log-mean temperature difference for counter-current flow is:

$$\Delta T_{lm} = \frac{(T_{h,in} - T_{c,out}) - (T_{h,out} - T_{c,in})}{\ln\left(\frac{T_{h,in} - T_{c,out}}{T_{h,out} - T_{c,in}}\right)}$$

For the operating point: T_h,in = 400 K, T_h,out = 350 K, T_c,in = 300 K, T_c,out = 340 K.

a) Calculate Q at the operating point.
b) For sensitivity analysis, find how Q changes with T_h,out using the chain rule.
c) If T_h,out increases by 5 K (hot fluid cools less), estimate the change in Q.
d) Discuss the physical trade-off revealed by this calculation.

**Solution:**

a) **Calculate operating point values:**

Average temperatures:
$$T_h = \frac{400 + 350}{2} = 375 \text{ K}$$
$$T_c = \frac{300 + 340}{2} = 320 \text{ K}$$

Overall heat transfer coefficient:
$$U = 500\left(1 + 0.002 \times \frac{375 + 320}{2}\right)$$
$$U = 500(1 + 0.002 \times 347.5) = 500(1.695) = 847.5 \text{ W/(m}^2\text{K)}$$

Log-mean temperature difference:
$$\Delta T_1 = T_{h,in} - T_{c,out} = 400 - 340 = 60 \text{ K}$$
$$\Delta T_2 = T_{h,out} - T_{c,in} = 350 - 300 = 50 \text{ K}$$

$$\Delta T_{lm} = \frac{60 - 50}{\ln(60/50)} = \frac{10}{\ln(1.2)} = \frac{10}{0.1823} = 54.85 \text{ K}$$

Heat transfer rate:
$$Q = 847.5 \times 25 \times 54.85 = 1,161,600 \text{ W} = 1.162 \text{ MW}$$

b) **Find dQ/dT_h,out using chain rule:**

Q depends on T_h,out through two paths:
1. Through U (which depends on T_h)
2. Through ΔT_lm directly

$$\frac{dQ}{dT_{h,out}} = \frac{\partial Q}{\partial U}\frac{\partial U}{\partial T_h}\frac{\partial T_h}{\partial T_{h,out}} + \frac{\partial Q}{\partial \Delta T_{lm}}\frac{\partial \Delta T_{lm}}{\partial T_{h,out}}$$

**Term 1: Effect through U**
$$\frac{\partial Q}{\partial U} = A \cdot \Delta T_{lm} = 25 \times 54.85 = 1371.25 \text{ m}^2\text{K}$$

$$\frac{\partial U}{\partial T_h} = U_0 \cdot \alpha/2 = 500 \times 0.002/2 = 0.5 \text{ W/(m}^2\text{K}^2\text{)}$$

$$\frac{\partial T_h}{\partial T_{h,out}} = 1/2$$

Contribution 1: $1371.25 \times 0.5 \times 0.5 = 342.8$ W/K

**Term 2: Effect through ΔT_lm**

This requires careful differentiation of the log-mean formula. Let:
- a = T_h,in - T_c,out = 60 K (independent of T_h,out)
- b = T_h,out - T_c,in (depends on T_h,out)

$$\Delta T_{lm} = \frac{a - b}{\ln(a/b)}$$

Using quotient rule and chain rule:
$$\frac{d\Delta T_{lm}}{db} = \frac{-\ln(a/b) - (a-b)\cdot(-1/b)}{[\ln(a/b)]^2}$$

At our point (a = 60, b = 50):
$$\frac{d\Delta T_{lm}}{db} = \frac{-0.1823 - 10 \times (-0.02)}{(0.1823)^2} = \frac{-0.1823 + 0.2}{0.0332} = 0.533$$

Since db/dT_h,out = 1:

$$\frac{\partial Q}{\partial \Delta T_{lm}} = U \cdot A = 847.5 \times 25 = 21,187.5 \text{ W/K}$$

Contribution 2: $21,187.5 \times 0.533 = 11,293$ W/K

**Total:**
$$\frac{dQ}{dT_{h,out}} = 342.8 + 11,293 = 11,636 \text{ W/K}$$

c) **Estimate change for ΔT_h,out = 5 K:**

$$\Delta Q \approx \frac{dQ}{dT_{h,out}} \times \Delta T_{h,out} = 11,636 \times 5 = 58,180 \text{ W} = 58.2 \text{ kW}$$

New Q ≈ 1162 + 58.2 = 1220.2 kW (increase of 5.0%)

d) **Physical trade-off discussion:**

When T_h,out increases (hot fluid exits hotter):
- **Positive effect:** The driving force (ΔT_lm) increases because the temperature difference at the hot end increases
- **Negative effect:** Less heat is actually removed from the hot fluid (lower effectiveness)

The calculation shows Q *increases* with T_h,out, which seems paradoxical - how can less cooling give more heat transfer?

The resolution: This is a *local* sensitivity analysis. The derivative dQ/dT_h,out assumes we're perturbing the outlet temperature while holding inlet temperatures constant. In reality, if T_h,out increases while T_h,in stays constant, the hot fluid must be flowing faster (less residence time), which increases film coefficient and hence U, and also increases the log-mean driving force.

In actual operation, the sign and magnitude depend on whether we're:
- Changing flow rates (affects U and outlet T's together)
- Changing heat exchanger area (affects Q and outlet T's)
- Experiencing fouling (decreases U, increases T_h,out)

This exercise demonstrates why process engineers must carefully define their sensitivity analysis - "what changes while what stays constant?"

---

## Exercise 5: Challenge Problem (Advanced)

**Problem:**
In distillation column design, the Fenske equation gives minimum number of stages:

$$N_{min} = \frac{\ln[(x_D/(1-x_D)) \cdot ((1-x_B)/x_B)]}{\ln \alpha}$$

where:
- x_D = distillate composition (mole fraction of light component)
- x_B = bottoms composition (mole fraction of light component)
- α = relative volatility (assumed constant)

For a benzene-toluene separation: α = 2.4, x_D = 0.95, x_B = 0.05

a) Calculate N_min.
b) Derive expressions for ∂N_min/∂x_D and ∂N_min/∂x_B.
c) Calculate these sensitivities at the operating point.
d) If product specification tightens to x_D = 0.98 and x_B = 0.02, estimate the change in N_min using the total differential.
e) Compare with exact calculation and explain the difference.
f) Discuss practical implications for column design and operation.

**Solution:**

a) **Calculate N_min:**

$$N_{min} = \frac{\ln[(0.95/0.05) \cdot (0.95/0.05)]}{\ln 2.4}$$
$$= \frac{\ln[(19) \cdot (19)]}{\ln 2.4} = \frac{\ln(361)}{0.8755} = \frac{5.888}{0.8755} = 6.72 \text{ stages}$$

b) **Derive sensitivities:**

Let $R = \frac{x_D/(1-x_D)}{x_B/(1-x_B)} = \frac{x_D(1-x_B)}{x_B(1-x_D)}$

Then: $N_{min} = \frac{\ln R}{\ln \alpha}$

$$\frac{\partial N_{min}}{\partial x_D} = \frac{1}{\ln \alpha} \cdot \frac{1}{R} \cdot \frac{\partial R}{\partial x_D}$$

Finding ∂R/∂x_D:
$$R = x_D(1-x_B) \cdot \frac{1}{x_B(1-x_D)}$$

Using quotient rule:
$$\frac{\partial R}{\partial x_D} = \frac{(1-x_B)}{x_B} \cdot \frac{d}{dx_D}\left[\frac{x_D}{1-x_D}\right]$$

$$\frac{d}{dx_D}\left[\frac{x_D}{1-x_D}\right] = \frac{(1-x_D) + x_D}{(1-x_D)^2} = \frac{1}{(1-x_D)^2}$$

Therefore:
$$\frac{\partial R}{\partial x_D} = \frac{1-x_B}{x_B(1-x_D)^2}$$

$$\frac{\partial N_{min}}{\partial x_D} = \frac{1}{\ln \alpha} \cdot \frac{x_B(1-x_D)}{x_D(1-x_B)} \cdot \frac{1-x_B}{x_B(1-x_D)^2}$$

$$= \frac{1}{\ln \alpha} \cdot \frac{1}{x_D(1-x_D)}$$

By symmetry:
$$\frac{\partial N_{min}}{\partial x_B} = -\frac{1}{\ln \alpha} \cdot \frac{1}{x_B(1-x_B)}$$

(Negative because increasing x_B makes separation easier)

c) **Calculate at operating point:**

$$\frac{\partial N_{min}}{\partial x_D}\bigg|_{x_D=0.95} = \frac{1}{0.8755 \times 0.95 \times 0.05} = \frac{1}{0.0416} = 24.04 \text{ stages per mole fraction}$$

$$\frac{\partial N_{min}}{\partial x_B}\bigg|_{x_B=0.05} = -\frac{1}{0.8755 \times 0.05 \times 0.95} = -24.04 \text{ stages per mole fraction}$$

The sensitivities have equal magnitude but opposite sign - makes physical sense!

d) **Estimate using total differential:**

$$dN_{min} \approx \frac{\partial N_{min}}{\partial x_D}dx_D + \frac{\partial N_{min}}{\partial x_B}dx_B$$

$$\Delta N_{min} \approx 24.04 \times (0.98 - 0.95) + (-24.04) \times (0.02 - 0.05)$$
$$= 24.04 \times 0.03 + (-24.04) \times (-0.03)$$
$$= 0.721 + 0.721 = 1.442 \text{ stages}$$

New estimate: N_min ≈ 6.72 + 1.44 = 8.16 stages

e) **Exact calculation:**

$$N_{min,new} = \frac{\ln[(0.98/0.02) \cdot (0.98/0.02)]}{\ln 2.4}$$
$$= \frac{\ln[(49) \cdot (49)]}{0.8755} = \frac{\ln(2401)}{0.8755} = \frac{7.783}{0.8755} = 8.89 \text{ stages}$$

Actual change: ΔN_min = 8.89 - 6.72 = 2.17 stages

Error: (2.17 - 1.44)/2.17 × 100% = 33.6%

**Why the large error?**
The linear approximation is poor because:
1. The function N_min has significant curvature (second derivatives matter)
2. The change in x (0.03) is relatively large (3% is substantial for high-purity separations)
3. Near x → 1, the function becomes very nonlinear due to the logarithm of a ratio

A second-order Taylor expansion would give much better accuracy.

f) **Practical implications:**

1. **Design margins:** Because N_min is highly sensitive near high purities (∂N_min/∂x is large), designers add significant safety factors. A linear estimate can severely underestimate actual stages needed.

2. **Operating flexibility:** The high sensitivity means small changes in product specs (e.g., from customer requirements) can require major column modifications.

3. **Nonlinear effects dominate:** At high purities (>95%), nonlinear effects are strong. Operators must be aware that "just a little purer" can mean "much harder to achieve."

4. **Control challenges:** The steep sensitivity makes composition control near endpoints difficult - small disturbances cause large changes.

5. **Economic optimization:** The nonlinearity suggests there's often an economic optimum purity that balances:
   - Product value (higher x_D is better)
   - Capital cost (more stages)
   - Operating cost (more reflux, energy)

This problem illustrates why process engineers need both analytical tools (calculus) and engineering judgment (knowing when linearization fails).

---

## Summary of Key Skills Demonstrated

1. **Direct differentiation** of exponential functions (Exercise 1)
2. **Chain rule** with implicit temperature dependence (Exercise 2)
3. **Implicit differentiation** and total differential (Exercise 3)
4. **Multivariable chain rule** with multiple paths (Exercise 4)
5. **Complex function differentiation** with logarithms and ratios (Exercise 5)
6. **Physical interpretation** of mathematical results in PSE contexts
7. **Error analysis** and understanding limitations of linear approximation

## Common Mistakes to Avoid

- Forgetting negative signs in rate expressions
- Mixing up partial and total derivatives
- Not specifying what's held constant in partial derivatives
- Ignoring higher-order terms when changes are large
- Losing track of units through calculations
- Missing physical interpretation opportunities
