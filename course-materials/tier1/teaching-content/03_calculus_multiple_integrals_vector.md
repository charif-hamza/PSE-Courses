# Calculus: Multiple Integrals and Vector Calculus

## Learning Objectives
After mastering this subconcept, you will be able to:
- Set up and evaluate double and triple integrals
- Apply multiple integrals to calculate volumes, masses, and total amounts
- Understand vector fields and their operations (gradient, divergence, curl)
- Apply vector calculus to transport phenomena and conservation laws
- Use line and surface integrals for flux calculations

## Prerequisites
- Single-variable integration
- Partial derivatives
- 3D coordinate systems (Cartesian, cylindrical, spherical)

## 1. Double Integrals

### 1.1 Geometric Interpretation

A double integral ∬_R f(x,y) dA calculates:
- **Volume** under surface z = f(x,y) above region R
- **Total mass** if f(x,y) is density
- **Total heat transfer** if f(x,y) is heat flux

### 1.2 Evaluation Methods

**Iterated Integrals:**
$$\iint_R f(x,y) \, dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) \, dy \, dx$$

or

$$= \int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y) \, dx \, dy$$

**Order matters for computation but not for result** (Fubini's theorem).

### 1.3 PSE Application: Heat Generation in a Plate

**Problem:** A rectangular catalytic plate (0 ≤ x ≤ L, 0 ≤ y ≤ W) has heat generation rate:

$$\dot{q}(x,y) = \dot{q}_0 \sin\left(\frac{\pi x}{L}\right) \sin\left(\frac{\pi y}{W}\right)$$

where q̇₀ = 1000 W/m², L = 0.5 m, W = 0.3 m.

Find total heat generated.

**Solution:**

$$Q_{total} = \int_0^L \int_0^W \dot{q}_0 \sin\left(\frac{\pi x}{L}\right) \sin\left(\frac{\pi y}{W}\right) dy \, dx$$

Separate the integrals (product of functions of different variables):

$$= \dot{q}_0 \left[\int_0^L \sin\left(\frac{\pi x}{L}\right) dx\right] \left[\int_0^W \sin\left(\frac{\pi y}{W}\right) dy\right]$$

First integral:
$$\int_0^L \sin\left(\frac{\pi x}{L}\right) dx = \left[-\frac{L}{\pi}\cos\left(\frac{\pi x}{L}\right)\right]_0^L$$

$$= -\frac{L}{\pi}[\cos(\pi) - \cos(0)] = -\frac{L}{\pi}[-1 - 1] = \frac{2L}{\pi}$$

Similarly, second integral = 2W/π

$$Q_{total} = \dot{q}_0 \cdot \frac{2L}{\pi} \cdot \frac{2W}{\pi} = \frac{4\dot{q}_0 LW}{\pi^2}$$

$$= \frac{4 \times 1000 \times 0.5 \times 0.3}{\pi^2} = \frac{600}{9.87} = 60.8 \text{ W}$$

**Physical insight:** Peak generation is at center (x=L/2, y=W/2), zero at edges. The π² factor shows how sinusoidal distribution averages down from peak.

### 1.4 Changing Order of Integration

Sometimes one order is easier to evaluate than the other.

**Example:** $\int_0^1 \int_x^1 e^{y^2} dy \, dx$

The inner integral ∫ e^(y²) dy has no elementary antiderivative!

**Solution:** Change order.

Region: 0 ≤ x ≤ 1, x ≤ y ≤ 1

Equivalently: 0 ≤ y ≤ 1, 0 ≤ x ≤ y

$$\int_0^1 \int_0^y e^{y^2} dx \, dy = \int_0^1 x \big|_0^y e^{y^2} dy = \int_0^1 y e^{y^2} dy$$

Now use substitution u = y², du = 2y dy:

$$= \frac{1}{2} \int_0^1 e^u du = \frac{1}{2}[e^u]_0^1 = \frac{e-1}{2} \approx 0.859$$

## 2. Triple Integrals

### 2.1 Applications in PSE

Triple integrals calculate quantities over 3D volumes:
- Total mass: ∭_V ρ(x,y,z) dV
- Total heat content: ∭_V ρc_p T dV
- Average concentration: C_avg = (1/V) ∭_V C(x,y,z) dV

### 2.2 Coordinate Systems

**Cartesian:** dV = dx dy dz

**Cylindrical (r, θ, z):**
- x = r cos θ, y = r sin θ, z = z
- **dV = r dr dθ dz** (don't forget the r!)

**Spherical (ρ, θ, φ):**
- x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ
- **dV = ρ² sin φ dρ dθ dφ**

**Choose coordinates matching problem symmetry!**

### 2.3 PSE Application: Mass in Cylindrical Reactor

**Problem:** A cylindrical reactor (radius R = 0.5 m, height H = 2 m) has concentration profile:

$$C(r,z) = C_0 \left(1 - \frac{r^2}{R^2}\right) \left(1 - \frac{z}{H}\right)$$

where C₀ = 10 mol/L. Find total moles.

**Solution:** Use cylindrical coordinates.

$$n_{total} = \int_0^{2\pi} \int_0^R \int_0^H C_0 \left(1 - \frac{r^2}{R^2}\right) \left(1 - \frac{z}{H}\right) r \, dz \, dr \, d\theta$$

By symmetry, no θ dependence, so θ integral gives 2π:

$$= 2\pi C_0 \int_0^R \left(1 - \frac{r^2}{R^2}\right) r \, dr \int_0^H \left(1 - \frac{z}{H}\right) dz$$

**Radial integral:**
$$\int_0^R \left(r - \frac{r^3}{R^2}\right) dr = \left[\frac{r^2}{2} - \frac{r^4}{4R^2}\right]_0^R = \frac{R^2}{2} - \frac{R^2}{4} = \frac{R^2}{4}$$

**Axial integral:**
$$\int_0^H \left(1 - \frac{z}{H}\right) dz = \left[z - \frac{z^2}{2H}\right]_0^H = H - \frac{H}{2} = \frac{H}{2}$$

**Total:**
$$n_{total} = 2\pi C_0 \cdot \frac{R^2}{4} \cdot \frac{H}{2} = \frac{\pi C_0 R^2 H}{4}$$

$$= \frac{\pi \times 10 \times 0.25 \times 2}{4} = \frac{\pi \times 5}{4} = 3.93 \text{ mol}$$

**Check:** Volume = πR²H = π × 0.25 × 2 = 1.57 m³. If C = C₀ everywhere, n = 10 × 1.57 = 15.7 mol. Our answer (3.93 mol) is about 1/4 of this, consistent with the concentration profile that averages to roughly C₀/4.

## 3. Vector Fields and Vector Calculus

### 3.1 Vector Fields in PSE

A **vector field** assigns a vector to each point in space.

**Examples:**
- **Velocity field:** v⃗(x,y,z,t) in fluid flow
- **Heat flux:** q⃗ = -k∇T (Fourier's law)
- **Mass flux:** N⃗_A = -D∇C_A (Fick's law)
- **Electric field:** E⃗ (for electrochemical processes)

### 3.2 Gradient (∇f)

The **gradient** of a scalar field f is a vector pointing in direction of steepest increase:

$$\nabla f = \frac{\partial f}{\partial x}\hat{i} + \frac{\partial f}{\partial y}\hat{j} + \frac{\partial f}{\partial z}\hat{k}$$

**Properties:**
- ∇f is perpendicular to level surfaces of f
- |∇f| is the rate of maximum increase
- Direction of -∇f is direction of maximum decrease

**PSE Application - Temperature Gradient:**

If T(x,y,z) = 400 - 50x² - 30y² (temperature in a plate, K), find heat flux at (0.1, 0.2) m if k = 15 W/(m·K).

$$\nabla T = -100x\hat{i} - 60y\hat{j}$$

At (0.1, 0.2):
$$\nabla T = -10\hat{i} - 12\hat{j} \text{ K/m}$$

Heat flux:
$$\vec{q} = -k\nabla T = -15(-10\hat{i} - 12\hat{j}) = 150\hat{i} + 180\hat{j} \text{ W/m}^2$$

Heat flows from hot to cold (positive direction), magnitude = √(150² + 180²) = 234 W/m².

### 3.3 Divergence (∇·v⃗)

The **divergence** measures "spreading out" of a vector field:

$$\nabla \cdot \vec{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} + \frac{\partial v_z}{\partial z}$$

**Physical meaning:**
- ∇·v⃗ > 0: Source (fluid expanding, leaving point)
- ∇·v⃗ < 0: Sink (fluid contracting, entering point)
- ∇·v⃗ = 0: Incompressible flow (conservation of mass)

**PSE Application - Continuity Equation:**

Conservation of mass for incompressible flow:
$$\nabla \cdot \vec{v} = 0$$

For v⃗ = (x² - y²)î + (2xy)ĵ:

$$\nabla \cdot \vec{v} = \frac{\partial}{\partial x}(x^2 - y^2) + \frac{\partial}{\partial y}(2xy) = 2x + 2x = 4x$$

This flow is **not incompressible** except along x = 0 plane.

### 3.4 Curl (∇×v⃗)

The **curl** measures rotation/circulation of a vector field:

$$\nabla \times \vec{v} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ v_x & v_y & v_z \end{vmatrix}$$

$$= \left(\frac{\partial v_z}{\partial y} - \frac{\partial v_y}{\partial z}\right)\hat{i} + \left(\frac{\partial v_x}{\partial z} - \frac{\partial v_z}{\partial x}\right)\hat{j} + \left(\frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y}\right)\hat{k}$$

**Physical meaning:**
- ∇×v⃗ = 0: Irrotational flow (potential flow)
- |∇×v⃗| = vorticity magnitude

**PSE Application - Stirred Tank:**

In a mixing vessel with angular velocity ω about z-axis:
$$\vec{v} = \omega(-y\hat{i} + x\hat{j})$$

$$\nabla \times \vec{v} = \left(\frac{\partial x}{\partial x} - \frac{\partial(-y)}{\partial y}\right)\hat{k} = (1 + 1)\omega\hat{k} = 2\omega\hat{k}$$

Vorticity = 2ω, pointing along rotation axis.

## 4. Line Integrals

### 4.1 Definition

A **line integral** integrates a function along a curve:

$$\int_C f \, ds = \int_a^b f(\vec{r}(t)) |\vec{r}'(t)| dt$$

For vector fields (work/circulation):

$$\int_C \vec{F} \cdot d\vec{r} = \int_a^b \vec{F}(\vec{r}(t)) \cdot \vec{r}'(t) \, dt$$

### 4.2 PSE Application - Pipe Flow Work

**Problem:** Fluid flows through a bent pipe from (0,0,0) to (1,1,0) along path r⃗(t) = (t, t², 0) for 0 ≤ t ≤ 1. Pressure gradient force is F⃗ = -∇P = (100, 50, 0) N/m³. Find work done by pressure.

**Solution:**

$$\vec{r}'(t) = (1, 2t, 0)$$

$$W = \int_0^1 (100, 50, 0) \cdot (1, 2t, 0) dt = \int_0^1 (100 + 100t) dt$$

$$= [100t + 50t^2]_0^1 = 150 \text{ J/m}^3$$

## 5. Surface Integrals and Flux

### 5.1 Flux Through a Surface

**Flux** of vector field F⃗ through surface S:

$$\Phi = \iint_S \vec{F} \cdot \hat{n} \, dS$$

where n̂ is unit normal vector.

### 5.2 PSE Application - Mass Flux Through Membrane

**Problem:** A cylindrical membrane (radius R, height H) has radial mass flux:

$$\vec{N}_A = -D\frac{dC_A}{dr}\hat{r} = \frac{D(C_{in} - C_{out})}{R}\hat{r}$$

Find total molar flow rate through the membrane.

**Solution:**

Flux through cylindrical surface:
$$\dot{n}_A = \iint_S \vec{N}_A \cdot \hat{n} \, dS$$

On the cylinder, n̂ = r̂, dS = R dθ dz:

$$\dot{n}_A = \int_0^{2\pi} \int_0^H \frac{D(C_{in} - C_{out})}{R} \cdot R \, dz \, d\theta$$

$$= D(C_{in} - C_{out}) \int_0^{2\pi} d\theta \int_0^H dz = D(C_{in} - C_{out}) \cdot 2\pi \cdot H$$

$$= 2\pi H D(C_{in} - C_{out})$$

This is **Fick's first law** applied to cylindrical geometry!

## 6. Fundamental Theorems

### 6.1 Divergence Theorem (Gauss's Theorem)

$$\iiint_V (\nabla \cdot \vec{F}) \, dV = \iint_S \vec{F} \cdot \hat{n} \, dS$$

**Meaning:** Total divergence inside volume = net flux out of surface

**PSE Application:** Derive conservation laws from differential equations.

Example - Mass conservation:
$$\iiint_V \frac{\partial \rho}{\partial t} dV = -\iint_S \rho \vec{v} \cdot \hat{n} \, dS$$

Using divergence theorem on RHS:
$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0$$

This is the **continuity equation**!

### 6.2 Stokes' Theorem

$$\iint_S (\nabla \times \vec{F}) \cdot \hat{n} \, dS = \oint_C \vec{F} \cdot d\vec{r}$$

**Meaning:** Circulation around boundary = total curl through surface

Less commonly used in PSE, but appears in rotating flow analysis.

### 6.3 Gradient Theorem

$$\int_C \nabla f \cdot d\vec{r} = f(\vec{r}_B) - f(\vec{r}_A)$$

**Meaning:** Line integral of gradient depends only on endpoints, not path.

**PSE Application:** Work in conservative force fields (pressure, potential energy).

## 7. Applications to Transport Phenomena

### 7.1 General Transport Equation

All transport phenomena follow:
$$\text{Flux} = -(\text{Diffusivity}) \times \nabla(\text{Potential})$$

| Transport | Flux | Diffusivity | Potential | Equation |
|-----------|------|-------------|-----------|----------|
| Heat | q⃗ | k | T | Fourier's law |
| Mass | N⃗_A | D | C_A | Fick's law |
| Momentum | τ | μ | v | Newton's law |

### 7.2 Conservation Laws in Differential Form

**General form:**
$$\frac{\partial \psi}{\partial t} + \nabla \cdot \vec{J}_\psi = S_\psi$$

where:
- ψ = conserved quantity (mass, energy, momentum)
- J⃗_ψ = flux of ψ
- S_ψ = source/sink of ψ

**Heat equation:**
$$\rho c_p \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T) + \dot{q}$$

**Diffusion equation:**
$$\frac{\partial C_A}{\partial t} = \nabla \cdot (D \nabla C_A) + r_A$$

These are the PDEs governing process systems!

## 8. Summary and Connections

**Multiple Integrals:**
- Calculate total quantities over regions/volumes
- Choose coordinate system matching symmetry
- Separate variables when possible

**Vector Calculus:**
- Gradient: points uphill, gives flux from potential
- Divergence: measures sources/sinks
- Curl: measures rotation

**Integral Theorems:**
- Connect volume and surface integrals
- Derive conservation laws
- Transform between differential and integral forms

**PSE Applications:**
- Transport phenomena equations
- Flux calculations
- Conservation laws
- Reactor and separator analysis

## Common Pitfalls

1. **Forgetting Jacobian factors** (r in cylindrical, ρ²sinφ in spherical)
2. **Wrong integration limits** for complex regions
3. **Not checking coordinate system match** to problem symmetry
4. **Confusing gradient, divergence, curl** - review definitions!
5. **Missing negative signs** in flux laws (Fourier, Fick)
6. **Wrong normal vector direction** in flux calculations

## Next Steps

With this foundation, you're ready for:
- Partial differential equations (Tier 1.1)
- Transport phenomena detailed analysis (Tier 1.4)
- Numerical methods for multidimensional problems (Tier 2.1)
