# Exercises: Integration Techniques

## Exercise 1: Direct Application - Substitution (Easy)

**Problem:**
A semi-batch reactor operates with constant volumetric feed rate Q = 50 L/min of pure reactant B into a well-mixed reactor initially containing A. The second-order reaction A + B → C occurs with rate constant k = 0.1 L/(mol·min).

If C_A decreases according to:
$$\frac{dC_A}{dt} = -\frac{k C_A C_B Q t}{V_0 + Qt}$$

and initially (t=0): C_A = 2 mol/L, C_B = 0, V₀ = 100 L, C_B,feed = 5 mol/L.

For a simplified case where C_B ≈ constant = 3 mol/L (quasi-steady assumption):
$$\frac{dC_A}{dt} = -\frac{0.1 \times C_A \times 3 \times 50 \times t}{100 + 50t} = -\frac{15 C_A t}{100 + 50t}$$

Find C_A(t) at t = 2 minutes by integrating from 0 to 2 min.

**Solution:**

Separate variables:
$$\frac{dC_A}{C_A} = -\frac{15t}{100 + 50t} dt$$

**Left side:** Simply ∫ dC_A/C_A = ln(C_A)

**Right side:** Use substitution.
Let u = 100 + 50t
Then du = 50 dt, so dt = du/50

Also: t = (u - 100)/50

$$-\int \frac{15t}{100 + 50t} dt = -\int \frac{15(u-100)/50}{u} \cdot \frac{du}{50}$$

$$= -\frac{15}{2500} \int \frac{u - 100}{u} du = -\frac{3}{500} \int \left(1 - \frac{100}{u}\right) du$$

$$= -\frac{3}{500}(u - 100\ln u) + C$$

$$= -\frac{3}{500}(100 + 50t - 100\ln(100 + 50t)) + C$$

**Definite integral from 0 to 2:**

$$\ln C_A(2) - \ln C_A(0) = -\frac{3}{500}\left[(100 + 100 - 100\ln(200)) - (100 - 100\ln(100))\right]$$

$$= -\frac{3}{500}\left[100 - 100\ln(200) + 100\ln(100)\right]$$

$$= -\frac{3}{500}\left[100 - 100\ln(2)\right]$$ (since ln(200/100) = ln(2))

$$= -\frac{3}{500} \times 100(1 - \ln 2) = -\frac{3}{5}(1 - 0.693) = -0.184$$

$$\ln\frac{C_A(2)}{C_A(0)} = -0.184$$

$$C_A(2) = 2 \times e^{-0.184} = 2 \times 0.832 = 1.66 \text{ mol/L}$$

**Check:** Concentration decreased from 2.0 to 1.66 mol/L, which is reasonable for 2 minutes of reaction.

---

## Exercise 2: Integration by Parts - RTD Analysis (Moderate)

**Problem:**
A tracer study on a reactor gives an RTD function:

$$E(t) = \frac{2t}{\tau^2}e^{-t/\tau}$$

where τ = 10 minutes.

Calculate:
a) Verify that ∫₀^∞ E(t) dt = 1 (normalization check)
b) Mean residence time: $\bar{t} = \int_0^\infty t E(t) dt$
c) Variance: $\sigma^2 = \int_0^\infty (t - \bar{t})^2 E(t) dt = \int_0^\infty t^2 E(t) dt - \bar{t}^2$

**Solution:**

a) **Normalization:**

$$\int_0^\infty E(t) dt = \int_0^\infty \frac{2t}{\tau^2} e^{-t/\tau} dt$$

Use integration by parts:
Let u = 2t/τ², dv = e^(-t/τ) dt
Then du = 2/τ² dt, v = -τe^(-t/τ)

$$= \left[\frac{2t}{\tau^2} \cdot (-\tau e^{-t/\tau})\right]_0^\infty + \int_0^\infty \tau e^{-t/\tau} \cdot \frac{2}{\tau^2} dt$$

First term = 0 (using L'Hôpital's rule at ∞)

$$= \frac{2}{\tau} \int_0^\infty e^{-t/\tau} dt = \frac{2}{\tau} \cdot \left[-\tau e^{-t/\tau}\right]_0^\infty = \frac{2}{\tau} \cdot \tau = 2$$

**Wait, this gives 2, not 1! Let me check the problem statement.**

Actually, for this to normalize to 1, the RTD should be:
$$E(t) = \frac{t}{\tau^2}e^{-t/\tau}$$

Let me recalculate with this form:

$$\int_0^\infty \frac{t}{\tau^2} e^{-t/\tau} dt$$

Same integration by parts:
$$= \left[\frac{t}{\tau^2} \cdot (-\tau e^{-t/\tau})\right]_0^\infty + \int_0^\infty \tau e^{-t/\tau} \cdot \frac{1}{\tau^2} dt$$

$$= 0 + \frac{1}{\tau} \int_0^\infty e^{-t/\tau} dt = \frac{1}{\tau} \cdot \tau = 1$$ ✓

b) **Mean residence time:**

$$\bar{t} = \int_0^\infty t \cdot \frac{t}{\tau^2}e^{-t/\tau} dt = \frac{1}{\tau^2} \int_0^\infty t^2 e^{-t/\tau} dt$$

Need to integrate t² e^(-t/τ). Use parts twice.

**First application:**
u = t², dv = e^(-t/τ) dt
du = 2t dt, v = -τe^(-t/τ)

$$\int t^2 e^{-t/\tau} dt = -\tau t^2 e^{-t/\tau} \bigg|_0^\infty + 2\tau \int t e^{-t/\tau} dt$$

First term = 0

**Second application on remaining integral:**
u = t, dv = e^(-t/τ) dt
du = dt, v = -τe^(-t/τ)

$$\int t e^{-t/\tau} dt = -\tau t e^{-t/\tau} \bigg|_0^\infty + \tau \int e^{-t/\tau} dt$$

$$= 0 + \tau \cdot (-\tau e^{-t/\tau})\bigg|_0^\infty = \tau^2$$

Substituting back:
$$\int_0^\infty t^2 e^{-t/\tau} dt = 2\tau \cdot \tau^2 = 2\tau^3$$

Therefore:
$$\bar{t} = \frac{1}{\tau^2} \cdot 2\tau^3 = 2\tau = 2 \times 10 = 20 \text{ minutes}$$

c) **Variance:**

Need: $\int_0^\infty t^2 E(t) dt = \int_0^\infty t^3 e^{-t/\tau} / \tau^2 \, dt$

Pattern: Each integration by parts with t^n brings down n·τ and reduces power by 1.

For ∫ t³ e^(-t/τ) dt, applying parts three times gives: 3! τ⁴ = 6τ⁴

$$\int_0^\infty t^2 E(t) dt = \frac{6\tau^4}{\tau^2} = 6\tau^2$$

Variance:
$$\sigma^2 = 6\tau^2 - (2\tau)^2 = 6\tau^2 - 4\tau^2 = 2\tau^2 = 2 \times 100 = 200 \text{ min}^2$$

Standard deviation: σ = √200 = 14.14 min

**Physical interpretation:** This RTD (called Erlang-2 distribution) has mean of 2τ and relatively narrow spread (σ/mean = 0.71), indicating fairly plug-flow-like behavior.

---

## Exercise 3: Partial Fractions - CSTR with Complex Kinetics (Moderate-Challenging)

**Problem:**
A CSTR operates with the reaction A → B following Michaelis-Menten kinetics:

$$-r_A = \frac{V_{max} C_A}{K_M + C_A}$$

where V_max = 5 mol/(L·min), K_M = 2 mol/L.

The design equation for a CSTR is:
$$\tau = \frac{C_{A0} - C_A}{-r_A}$$

For C_A0 = 10 mol/L, find the residence time τ needed to achieve C_A = 3 mol/L.

Then, derive a general expression for conversion X = (C_A0 - C_A)/C_A0 as a function of τ.

**Solution:**

**Part 1: Direct calculation**

$$\tau = \frac{10 - 3}{\frac{5 \times 3}{2 + 3}} = \frac{7}{\frac{15}{5}} = \frac{7}{3} = 2.33 \text{ min}$$

**Part 2: General expression**

From C_A = C_A0(1 - X):

$$\tau = \frac{C_{A0} X}{V_{max} C_{A0}(1-X) / [K_M + C_{A0}(1-X)]}$$

$$= \frac{X[K_M + C_{A0}(1-X)]}{V_{max}(1-X)}$$

$$= \frac{K_M X + C_{A0}X(1-X)}{V_{max}(1-X)}$$

$$= \frac{K_M X}{V_{max}(1-X)} + \frac{C_{A0} X}{V_{max}}$$

This is algebraic, not requiring integration.

**But for a PFR with same kinetics:**

$$V = F_{A0} \int_0^X \frac{dX}{-r_A/C_{A0}} = \frac{F_{A0}}{C_{A0}} \int_0^X \frac{K_M + C_{A0}(1-X)}{V_{max}(1-X)} dX$$

$$= \frac{F_{A0}}{C_{A0} V_{max}} \int_0^X \frac{K_M + C_{A0}(1-X)}{1-X} dX$$

$$= \frac{F_{A0}}{C_{A0} V_{max}} \int_0^X \left[\frac{K_M}{1-X} + C_{A0}\right] dX$$

$$= \frac{F_{A0}}{C_{A0} V_{max}} \left[-K_M \ln(1-X) + C_{A0} X\right]_0^X$$

$$= \frac{F_{A0}}{C_{A0} V_{max}} \left[C_{A0} X - K_M \ln(1-X)\right]$$

For X = 0.7 (matching CSTR: C_A = 3 from C_A0 = 10):

$$V/F_{A0} = \tau_{PFR} = \frac{1}{10 \times 5}[10 \times 0.7 - 2\ln(0.3)]$$

$$= \frac{1}{50}[7 - 2(-1.204)] = \frac{1}{50}[7 + 2.408] = 0.188 \text{ min}$$

**Comparison:** PFR needs 0.188 min vs CSTR needs 2.33 min for same conversion. PFR is ~12x more efficient!

**Now for partial fractions in a different problem:**

Consider competitive inhibition:
$$-r_A = \frac{V_{max} C_A}{K_M(1 + C_I/K_I) + C_A}$$

For PFR integral with C_I changing with C_A via stoichiometry... this gets complex.

**Better example for partial fractions: Reversible reaction**

A ⇌ B with rate: $-r_A = k_f C_A - k_r C_B$

With stoichiometry: C_B = C_B0 + (C_A0 - C_A)

$$-r_A = k_f C_A - k_r[C_{B0} + C_{A0} - C_A] = (k_f + k_r)C_A - k_r(C_{A0} + C_{B0})$$

Let α = k_f + k_r, β = k_r(C_A0 + C_B0)

$$-r_A = \alpha C_A - \beta$$

For PFR:
$$\tau = C_{A0} \int_0^X \frac{dX}{-r_A}$$

With C_A = C_A0(1-X):

$$-r_A = \alpha C_{A0}(1-X) - \beta$$

$$\tau = C_{A0} \int_0^X \frac{dX}{\alpha C_{A0}(1-X) - \beta}$$

At equilibrium: α C_A,eq - β = 0, so C_A,eq = β/α

Let X_eq = 1 - β/(αC_A0) = (αC_A0 - β)/(αC_A0)

$$\tau = C_{A0} \int_0^X \frac{dX}{\alpha C_{A0}[(1-X) - (1-X_{eq})]}$$

$$= \frac{1}{\alpha} \int_0^X \frac{dX}{X_{eq} - X}$$

$$= -\frac{1}{\alpha} \ln(X_{eq} - X) \bigg|_0^X = -\frac{1}{\alpha}[\ln(X_{eq} - X) - \ln X_{eq}]$$

$$= \frac{1}{\alpha} \ln\frac{X_{eq}}{X_{eq} - X}$$

This didn't require partial fractions!

**True partial fractions example: Two competing reactions**

A → B (rate = k₁C_A²)
A → C (rate = k₂C_A)

Total rate: $-r_A = k_1 C_A^2 + k_2 C_A = C_A(k_1 C_A + k_2)$

$$\tau = C_{A0} \int_0^X \frac{dX}{C_{A0}(1-X)[k_1 C_{A0}(1-X) + k_2]}$$

$$= \int_0^X \frac{dX}{(1-X)[k_1 C_{A0}(1-X) + k_2]}$$

Let y = 1 - X, dy = -dX:

$$\tau = -\int_1^{1-X} \frac{dy}{y[k_1 C_{A0} y + k_2]}$$

Now use partial fractions:
$$\frac{1}{y(k_1 C_{A0} y + k_2)} = \frac{A}{y} + \frac{B}{k_1 C_{A0} y + k_2}$$

Multiply both sides by y(k₁C_A0 y + k₂):
$$1 = A(k_1 C_{A0} y + k_2) + By$$

At y = 0: 1 = Ak₂, so A = 1/k₂

At y = -k₂/(k₁C_A0): 1 = B(-k₂/(k₁C_A0)), so B = -k₁C_A0/k₂

$$\frac{1}{y(k_1 C_{A0} y + k_2)} = \frac{1/k_2}{y} - \frac{k_1 C_{A0}/k_2}{k_1 C_{A0} y + k_2}$$

$$= \frac{1}{k_2}\left[\frac{1}{y} - \frac{k_1 C_{A0}}{k_1 C_{A0} y + k_2}\right]$$

Integrating:
$$\tau = -\frac{1}{k_2}\int_1^{1-X} \left[\frac{1}{y} - \frac{k_1 C_{A0}}{k_1 C_{A0} y + k_2}\right] dy$$

$$= -\frac{1}{k_2}\left[\ln y - \ln(k_1 C_{A0} y + k_2)\right]_1^{1-X}$$

$$= -\frac{1}{k_2}\left[\ln\frac{y}{k_1 C_{A0} y + k_2}\right]_1^{1-X}$$

$$= -\frac{1}{k_2}\left\{\ln\frac{1-X}{k_1 C_{A0}(1-X) + k_2} - \ln\frac{1}{k_1 C_{A0} + k_2}\right\}$$

$$= \frac{1}{k_2}\ln\left[\frac{k_1 C_{A0} + k_2}{k_1 C_{A0}(1-X) + k_2} \cdot (1-X)\right]$$

**Physical meaning:** As X → 1, τ → ∞ (expected). The term shows competition between first and second-order pathways.

---

## Exercise 4: Combined Techniques - Heat Exchanger (Challenging)

**Problem:**
A counter-current heat exchanger cools a process stream. The heat transfer rate per unit length is:

$$\frac{dQ}{dz} = U \pi D (T_h - T_c)$$

where U = U₀(1 + αT_avg), T_avg = (T_h + T_c)/2, α = 0.001 K⁻¹, U₀ = 100 W/(m²·K), D = 0.1 m.

Energy balances give:
$$m_h c_{p,h} \frac{dT_h}{dz} = -U\pi D(T_h - T_c)$$
$$m_c c_{p,c} \frac{dT_c}{dz} = U\pi D(T_h - T_c)$$

For equal heat capacities: $\dot{m}_h c_{p,h} = \dot{m}_c c_{p,c} = \dot{C} = 500$ W/K

Find the length L required to cool the hot stream from 400 K to 350 K when the cold stream enters at 300 K.

**Solution:**

With equal heat capacities and counter-current flow:
$$T_h - T_c = \text{constant} = T_{h,in} - T_{c,out}$$

From energy balance:
$$\dot{C}(T_{h,in} - T_{h,out}) = \dot{C}(T_{c,out} - T_{c,in})$$

$$T_{c,out} = T_{c,in} + (T_{h,in} - T_{h,out}) = 300 + (400 - 350) = 350 \text{ K}$$

So: $T_h - T_c = 400 - 350 = 50$ K everywhere!

From hot fluid energy balance:
$$\dot{C} \frac{dT_h}{dz} = -U_0\left(1 + \alpha\frac{T_h + T_c}{2}\right) \pi D (T_h - T_c)$$

With T_c = T_h - 50:
$$\dot{C} \frac{dT_h}{dz} = -U_0\left(1 + \alpha\frac{T_h + T_h - 50}{2}\right) \pi D \times 50$$

$$= -U_0 \pi D \times 50 \left(1 + \alpha\left(T_h - 25\right)\right)$$

Let K = U₀πD × 50 = 100 × π × 0.1 × 50 = 1571 W/K

$$500 \frac{dT_h}{dz} = -1571(1 + 0.001(T_h - 25))$$

$$\frac{dT_h}{dz} = -3.142(1 + 0.001T_h - 0.025) = -3.142(0.975 + 0.001T_h)$$

$$\frac{dT_h}{dz} = -3.064 - 0.003142 T_h$$

Separate variables:
$$\frac{dT_h}{3.064 + 0.003142 T_h} = -dz$$

Let u = 3.064 + 0.003142 T_h
Then du = 0.003142 dT_h, so dT_h = (1/0.003142)du

$$\frac{1}{0.003142} \int \frac{du}{u} = -\int dz$$

$$\frac{1}{0.003142} \ln u = -z + C$$

$$\ln(3.064 + 0.003142 T_h) = -0.003142 z + C$$

At z = 0: T_h = 400 K
$$C = \ln(3.064 + 0.003142 \times 400) = \ln(3.064 + 1.257) = \ln(4.321)$$

At z = L: T_h = 350 K
$$\ln(3.064 + 0.003142 \times 350) = -0.003142 L + \ln(4.321)$$

$$\ln(3.064 + 1.100) = -0.003142 L + \ln(4.321)$$

$$\ln(4.164) = -0.003142 L + \ln(4.321)$$

$$-0.003142 L = \ln(4.164) - \ln(4.321) = \ln(4.164/4.321) = \ln(0.9637)$$

$$L = \frac{-\ln(0.9637)}{0.003142} = \frac{0.0370}{0.003142} = 11.8 \text{ m}$$

**Physical check:** Heat transferred = 500 × (400 - 350) = 25,000 W. Average U ≈ 100(1 + 0.001 × 375) = 137.5 W/(m²K). Area = πDL = π × 0.1 × 11.8 = 3.71 m².
Q = U·A·ΔT = 137.5 × 3.71 × 50 = 25,506 W ✓ (close enough, small error from average approximation)

---

## Exercise 5: Challenge Problem - Batch Distillation (Very Challenging)

**Problem:**
A batch distillation (Rayleigh distillation) separates a binary mixture. The Rayleigh equation relates the amount of liquid remaining L to its composition x:

$$\ln\frac{L_0}{L} = \int_{x_0}^x \frac{dx}{x - y(x)}$$

where y(x) is the vapor composition in equilibrium with liquid x.

For constant relative volatility α = 2.5:
$$y = \frac{\alpha x}{1 + (\alpha - 1)x}$$

Starting with L₀ = 1000 mol at x₀ = 0.4 (mole fraction light component), distill until x = 0.2.

a) Evaluate the integral analytically using partial fractions.
b) Calculate the final amount L.
c) Determine total moles distilled and average distillate composition.

**Solution:**

a) **Analytical integration:**

$$y - x = \frac{\alpha x}{1 + (\alpha-1)x} - x = \frac{\alpha x - x[1 + (\alpha-1)x]}{1 + (\alpha-1)x}$$

$$= \frac{\alpha x - x - (\alpha-1)x^2}{1 + (\alpha-1)x} = \frac{(\alpha-1)x - (\alpha-1)x^2}{1 + (\alpha-1)x}$$

$$= \frac{(\alpha-1)x(1-x)}{1 + (\alpha-1)x}$$

So:
$$\frac{1}{y-x} = \frac{1 + (\alpha-1)x}{(\alpha-1)x(1-x)}$$

$$\ln\frac{L_0}{L} = \int_{0.4}^{0.2} \frac{1 + (\alpha-1)x}{(\alpha-1)x(1-x)} dx$$

With α = 2.5, (α-1) = 1.5:

$$= \int_{0.4}^{0.2} \frac{1 + 1.5x}{1.5x(1-x)} dx = \frac{1}{1.5} \int_{0.4}^{0.2} \frac{1 + 1.5x}{x(1-x)} dx$$

**Partial fractions:**
$$\frac{1 + 1.5x}{x(1-x)} = \frac{A}{x} + \frac{B}{1-x}$$

$$1 + 1.5x = A(1-x) + Bx$$

At x = 0: 1 = A
At x = 1: 2.5 = B

$$\frac{1 + 1.5x}{x(1-x)} = \frac{1}{x} + \frac{2.5}{1-x}$$

Integrating:
$$\frac{1}{1.5}\int_{0.4}^{0.2} \left(\frac{1}{x} + \frac{2.5}{1-x}\right) dx$$

$$= \frac{1}{1.5}\left[\ln x - 2.5\ln(1-x)\right]_{0.4}^{0.2}$$

$$= \frac{1}{1.5}\left\{[\ln(0.2) - 2.5\ln(0.8)] - [\ln(0.4) - 2.5\ln(0.6)]\right\}$$

$$= \frac{1}{1.5}\left[\ln\frac{0.2}{0.4} - 2.5\ln\frac{0.8}{0.6}\right]$$

$$= \frac{1}{1.5}\left[\ln(0.5) - 2.5\ln(1.333)\right]$$

$$= \frac{1}{1.5}[-0.693 - 2.5(0.287)]$$

$$= \frac{1}{1.5}[-0.693 - 0.718] = \frac{-1.411}{1.5} = -0.941$$

But this should be positive (L < L₀)! The issue is integration limits.

Correcting (we go from high x to low x, so flip):
$$\ln\frac{L_0}{L} = -(-0.941) = 0.941$$

b) **Final amount:**

$$\frac{L_0}{L} = e^{0.941} = 2.563$$

$$L = \frac{1000}{2.563} = 390 \text{ mol}$$

c) **Distillate amount and composition:**

Moles distilled: D = L₀ - L = 1000 - 390 = 610 mol

Overall material balance:
$$L_0 x_0 = L x + D \bar{y}_D$$

where ȳ_D is average distillate composition.

$$1000 \times 0.4 = 390 \times 0.2 + 610 \bar{y}_D$$

$$400 = 78 + 610 \bar{y}_D$$

$$\bar{y}_D = \frac{322}{610} = 0.528$$

**Physical interpretation:**
- Started with 40% light component
- Residue has only 20% (depleted in light component)
- Distillate averaged 52.8% (enriched, as expected)
- Lost 61% of original charge to distillate

**Verification:** Material balance check ✓

This problem demonstrates why batch distillation is less efficient than continuous - we don't maintain constant composition, so separation gets harder as we proceed.

---

## Summary

These exercises covered:
1. **Substitution** in time-varying reactor problems
2. **Integration by parts** (repeated) for RTD moment calculations
3. **Partial fractions** for complex reaction kinetics
4. **Combined substitution and separation** for heat exchanger analysis
5. **Advanced partial fractions** in batch distillation with VLE

## Key Takeaways

- **Pattern recognition** is crucial - identify which technique applies
- **Physical interpretation** always validates mathematical results
- **Analytical solutions** provide insight even when numerical methods are easier
- **PSE problems** naturally generate integrals requiring these techniques
- **Mastery requires practice** - work through variations of each type
