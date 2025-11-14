# Process Systems Engineering Learning Roadmap

## Overview

This roadmap provides a structured progression through PSE competencies, organized into three tiers. Each tier builds on the previous one, ensuring solid foundations before advancing to complex topics.

## Learning Philosophy

- **Build from ground up**: Never skip foundational topics
- **Deep before broad**: Master fundamentals thoroughly before specializing
- **Integration emphasis**: Show connections between topics continuously
- **Application focus**: Always connect theory to real PSE problems

## Tier 1: Essential Foundations

These are the bedrock competencies that underpin all PSE work. Without solid mastery here, advanced topics will be unstable.

### 1.1 Mathematics for PSE

**Calculus:**
- Single and multivariable calculus
- Partial derivatives and total differentials
- Integration techniques (substitution, parts, partial fractions)
- Multiple integrals
- Vector calculus (gradient, divergence, curl)
- Applications to rate processes and optimization

**Linear Algebra:**
- Matrix operations and properties
- Systems of linear equations
- Eigenvalues and eigenvectors
- Matrix decomposition
- Applications to material balances and process modeling

**Ordinary Differential Equations (ODEs):**
- First-order ODEs (separation, integrating factors)
- Second-order ODEs (characteristic equations)
- Systems of ODEs
- Numerical methods (Euler, Runge-Kutta)
- Applications to batch reactors and dynamic systems

**Partial Differential Equations (PDEs):**
- Classification (elliptic, parabolic, hyperbolic)
- Separation of variables
- Heat equation, wave equation
- Boundary and initial conditions
- Applications to distributed systems

**Statistics and Probability:**
- Probability distributions
- Statistical inference
- Regression analysis
- Experimental design
- Error analysis and uncertainty quantification

**Prerequisites:** High school mathematics
**Estimated time:** 4-6 weeks per sub-topic
**Integration:** Apply each mathematical tool to PSE problems immediately

### 1.2 Physics for PSE

**Thermodynamics:**
- Laws of thermodynamics (0th through 3rd)
- State functions and path functions
- Ideal and real gases
- Phase equilibria
- Property relations (Maxwell, Gibbs-Duhem)
- Entropy and free energy
- Chemical potential
- Thermodynamic cycles

**Fluid Dynamics:**
- Fluid statics (pressure, buoyancy)
- Conservation of mass (continuity equation)
- Bernoulli's equation
- Momentum balances
- Laminar vs turbulent flow
- Boundary layers
- Dimensional analysis and similarity
- Pipe flow and friction factors

**Heat Transfer:**
- Conduction (Fourier's law, heat equation)
- Convection (natural and forced)
- Radiation (Stefan-Boltzmann, view factors)
- Heat exchangers
- Fins and extended surfaces
- Transient heat transfer
- Dimensionless numbers (Nusselt, Prandtl, Grashof)

**Prerequisites:** High school physics
**Estimated time:** 6-8 weeks total
**Integration:** Connect to chemical processes continuously

### 1.3 Chemistry for PSE

**Physical Chemistry:**
- Thermodynamic properties of solutions
- Activity and fugacity
- Equations of state (van der Waals, Peng-Robinson, etc.)
- Phase diagrams and phase rule
- Colligative properties
- Chemical equilibrium
- Electrochemistry basics

**Reaction Kinetics:**
- Rate laws and reaction orders
- Elementary vs complex reactions
- Temperature dependence (Arrhenius)
- Activation energy and transition state theory
- Catalysis fundamentals
- Mechanism determination
- Steady-state approximation

**Prerequisites:** General chemistry
**Estimated time:** 4-5 weeks
**Integration:** Apply to reactor design and process operations

### 1.4 Chemical Engineering Core

**Material and Energy Balances:**
- System definition and boundaries
- Conservation principles
- Steady-state balances
- Unsteady-state balances
- Single-unit operations
- Multiple-unit processes
- Recycle and bypass streams
- Reactive systems
- Simultaneous material and energy balances

**Transport Phenomena:**
- Analogies between momentum, heat, and mass transfer
- Molecular transport (diffusion, conduction, viscosity)
- Convective transport
- Shell balances
- Boundary layer theory
- Dimensionless analysis

**Unit Operations:**
- Fluid flow systems (pumps, compressors, turbines)
- Heat exchangers (types, design, effectiveness)
- Separation processes overview
- Reactors overview
- Process flow diagrams (PFD)
- Piping and instrumentation diagrams (P&ID)

**Prerequisites:** Tier 1.1-1.3 topics
**Estimated time:** 10-12 weeks
**Integration:** Core of PSE, connects everything

### 1.5 Computer Science for PSE

**Python Fundamentals:**
- Data types and structures
- Control flow and functions
- Object-oriented programming basics
- File I/O and data handling

**Intermediate Python:**
- List comprehensions
- Generators and iterators
- Lambda functions and functional programming
- Error handling and debugging
- Modules and packages

**Advanced Python for PSE:**
- NumPy for numerical arrays
- SciPy for scientific computing
- Matplotlib for visualization
- Pandas for data analysis
- Symbolic mathematics with SymPy

**Algorithms and Data Structures:**
- Algorithm complexity (Big-O notation)
- Searching and sorting algorithms
- Data structures (arrays, linked lists, trees, graphs)
- Recursion and dynamic programming

**Prerequisites:** Basic programming experience helpful but not required
**Estimated time:** 8-10 weeks
**Integration:** Implement PSE calculations and visualizations continuously

## Tier 2: Core PSE Competencies

Build on Tier 1 foundations to develop specialized PSE skills.

### 2.1 Numerical Methods

**Root Finding:**
- Bisection, Newton-Raphson, secant methods
- Systems of nonlinear equations

**Numerical Integration:**
- Trapezoidal rule, Simpson's rule
- Gaussian quadrature
- Monte Carlo integration

**Numerical Differentiation:**
- Finite difference methods
- Richardson extrapolation

**Linear Systems:**
- Direct methods (Gaussian elimination, LU decomposition)
- Iterative methods (Jacobi, Gauss-Seidel, SOR)
- Sparse matrix methods

**ODEs:**
- Explicit methods (Euler, Runge-Kutta)
- Implicit methods (backward Euler, BDF)
- Stiff systems
- Boundary value problems (shooting, finite difference)

**PDEs:**
- Finite difference methods
- Method of lines
- Stability analysis

**Prerequisites:** Tier 1.1 (Mathematics), 1.5 (Python)
**Estimated time:** 6-8 weeks
**Integration:** Solve real PSE problems numerically

### 2.2 Optimization Theory

**Unconstrained Optimization:**
- Gradient descent and variants
- Newton's method
- Quasi-Newton methods (BFGS)
- Conjugate gradient methods

**Constrained Optimization:**
- Linear programming (simplex method)
- Nonlinear programming (KKT conditions)
- Penalty and barrier methods
- Lagrange multipliers

**Global Optimization:**
- Simulated annealing
- Genetic algorithms
- Particle swarm optimization

**Applications:**
- Parameter estimation
- Process optimization
- Design optimization
- Supply chain optimization

**Prerequisites:** Tier 1.1 (Calculus, Linear Algebra), 2.1 (Numerical Methods)
**Estimated time:** 5-7 weeks
**Integration:** Optimize process designs and operations

### 2.3 Mass Transfer

**Molecular Diffusion:**
- Fick's laws
- Binary and multicomponent diffusion
- Temperature and pressure effects
- Diffusion in gases, liquids, solids

**Convective Mass Transfer:**
- Mass transfer coefficients
- Dimensionless correlations (Sherwood, Schmidt)
- Analogies with heat transfer

**Interphase Mass Transfer:**
- Two-film theory
- Overall mass transfer coefficients
- Equilibrium stages
- Rate-based models

**Applications:**
- Absorption and stripping
- Distillation column design
- Extraction
- Crystallization
- Adsorption

**Prerequisites:** Tier 1.2 (Heat Transfer), 1.4 (Transport Phenomena)
**Estimated time:** 5-6 weeks
**Integration:** Design separation processes

### 2.4 Reactor Design

**Ideal Reactors:**
- Batch reactors
- Continuous stirred-tank reactors (CSTR)
- Plug flow reactors (PFR)
- Performance equations and design equations

**Non-Ideal Reactors:**
- Residence time distribution (RTD)
- Segregation models
- Dispersion models
- Compartment models

**Multiple Reactions:**
- Series and parallel reactions
- Selectivity and yield
- Reactor choice for optimal selectivity

**Heat Effects:**
- Adiabatic operation
- Non-isothermal design
- Heat removal/addition
- Stability analysis

**Catalytic Reactors:**
- Catalyst fundamentals
- Heterogeneous catalysis
- Fixed bed reactors
- Fluidized bed reactors
- Catalyst deactivation

**Prerequisites:** Tier 1.3 (Reaction Kinetics), 1.4 (Material Balances), 2.1 (Numerical Methods)
**Estimated time:** 7-9 weeks
**Integration:** Design reactors for chemical processes

### 2.5 Separation Processes

**Phase Equilibrium:**
- VLE, LLE, SLE fundamentals
- Raoult's law and Henry's law
- Activity coefficient models (Wilson, NRTL, UNIQUAC)
- Equations of state for phase equilibrium

**Distillation:**
- Binary distillation (McCabe-Thiele)
- Multicomponent distillation (Fenske-Underwood-Gilliland)
- Rigorous distillation (stage-by-stage calculations)
- Azeotropes and extractive distillation
- Batch distillation

**Absorption and Stripping:**
- Operating line analysis
- Design methods
- Packed vs tray columns

**Extraction:**
- Liquid-liquid equilibrium
- Single and multistage extraction
- Supercritical extraction

**Membrane Separations:**
- Membrane types and materials
- Permeation models
- Module design
- Applications (RO, UF, gas separation)

**Prerequisites:** Tier 1.2 (Thermodynamics), 2.3 (Mass Transfer)
**Estimated time:** 8-10 weeks
**Integration:** Design separation systems

### 2.6 Process Dynamics and Control

**Dynamic Modeling:**
- Linearization of nonlinear systems
- Transfer functions
- Laplace transforms
- Block diagrams
- State-space representation

**System Response:**
- First-order systems
- Second-order systems
- Time delays
- Stability analysis (Routh-Hurwitz, Nyquist)

**Feedback Control:**
- PID controllers (proportional, integral, derivative actions)
- Controller tuning (Ziegler-Nichols, Cohen-Coon, IMC)
- Cascade control
- Feedforward control
- Ratio control

**Advanced Control Concepts:**
- Multivariable systems
- Decoupling
- Frequency response
- Root locus

**Prerequisites:** Tier 1.1 (ODEs, Laplace), 1.4 (Material/Energy Balances)
**Estimated time:** 6-8 weeks
**Integration:** Control process units and plants

### 2.7 Process Simulation

**Simulation Fundamentals:**
- Sequential modular approach
- Equation-oriented approach
- Recycle convergence
- Tear streams

**Thermodynamic Models:**
- Property packages
- Phase equilibrium calculations
- Enthalpy calculations

**Unit Operation Models:**
- Rigorous vs shortcut models
- Efficiency specifications
- Pressure drop calculations

**Steady-State Simulation:**
- Flowsheet development
- Convergence strategies
- Sensitivity analysis
- Optimization in simulators

**Dynamic Simulation:**
- Startup and shutdown procedures
- Control system design
- Safety studies

**Prerequisites:** All Tier 1, Tier 2.1-2.6
**Estimated time:** 6-7 weeks
**Tools:** Introduction to Aspen HYSYS, Aspen Plus, or open-source alternatives
**Integration:** Simulate complete processes

## Tier 3: Advanced/Specialized Topics

Cutting-edge topics and specialized areas for depth.

### 3.1 Advanced Process Control

**Model Predictive Control (MPC):**
- Linear MPC formulation
- Constraint handling
- Tuning and implementation
- Nonlinear MPC

**System Identification:**
- Parametric models (ARX, ARMAX)
- Non-parametric methods (step response, impulse response)
- Frequency domain identification
- Validation techniques

**Real-Time Optimization:**
- Economic optimization
- Constraint satisfaction
- Integration with control

**Prerequisites:** Tier 2.6 (Process Control), 2.2 (Optimization)
**Estimated time:** 5-6 weeks

### 3.2 Machine Learning for PSE

**Supervised Learning:**
- Regression (linear, polynomial, kernel methods)
- Classification (logistic regression, SVM, decision trees)
- Neural networks and deep learning
- Ensemble methods

**Unsupervised Learning:**
- Clustering (k-means, hierarchical, DBSCAN)
- Dimensionality reduction (PCA, t-SNE)
- Anomaly detection

**Applications:**
- Soft sensors
- Process monitoring
- Predictive maintenance
- Quality prediction
- Fault detection and diagnosis

**Prerequisites:** Tier 1.1 (Statistics), 1.5 (Python), 2.1 (Numerical Methods)
**Estimated time:** 8-10 weeks

### 3.3 Process Integration and Synthesis

**Pinch Analysis:**
- Energy targeting
- Heat exchanger network design
- Multiple utilities
- Total site integration

**Process Synthesis:**
- Superstructure optimization
- Reactor-separator-recycle systems
- Distillation sequencing
- Process intensification

**Sustainability:**
- Life cycle analysis
- Environmental impact assessment
- Green chemistry principles
- Waste minimization

**Prerequisites:** Tier 2 competencies
**Estimated time:** 6-7 weeks

### 3.4 Supply Chain Optimization

**Planning and Scheduling:**
- Production planning models
- Batch scheduling
- Continuous process scheduling
- Multi-site coordination

**Logistics:**
- Inventory management
- Distribution network design
- Transportation optimization

**Uncertainty Management:**
- Stochastic programming
- Robust optimization
- Demand forecasting

**Prerequisites:** Tier 2.2 (Optimization), 2.7 (Process Simulation)
**Estimated time:** 5-6 weeks

## Progression Guidelines

### How to Advance

1. **Complete prerequisites**: Never skip foundational topics
2. **Demonstrate mastery**: Solve challenging problems successfully
3. **Show integration**: Connect concepts across domains
4. **Apply practically**: Work through realistic scenarios

### Pacing Recommendations

- **Tier 1**: 6-9 months for complete coverage
- **Tier 2**: 6-8 months for core competencies
- **Tier 3**: Ongoing, based on interests and needs

### Revisiting Topics

- Schedule spaced repetition per pedagogy guidelines
- Revisit fundamentals when advancing to applications
- Integrate earlier topics into advanced problem sets
- Recognize that learning is spiral, not linear

## Using This Roadmap

**For topic selection:**
1. Check student's learning history from the progression file
2. Identify current tier and sub-topic
3. Verify prerequisite mastery
4. Select next topic in sequence OR
5. Identify topic needing spaced repetition

**For teaching:**
- Reference this roadmap to show student their position
- Highlight connections to upcoming topics
- Explain why prerequisites matter
- Celebrate progress through tiers

**For problem design:**
- Draw from student's covered topics
- Include multi-topic integration problems
- Preview next topics subtly in advanced problems
- Review prerequisite topics in new contexts

## Flexibility

This roadmap is a guide, not a rigid prescription. Adapt based on:
- Student's background and goals
- Industry vs academic focus
- Time constraints
- Emerging interests
- Career objectives

The key is maintaining rigor while allowing personalization within the framework.
