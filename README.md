# Numerical Computing
> A collection of numeric solutions produced throughout my undergraduate degree


## 1. The Energy Levels of the Finite Square Well
> An application of the Bisection and Secant root finding Methods

Given a 1-Dimensional finite square with depth -40V we solve the Schrodinger equation 

$$- \frac{\hbar}{2m} \frac{d^2}{dx^2} \psi_0(x) + V(x) \psi_0(x) = E_0 \psi_0(x)$$
for the the state Energy level. The equation to be solved for a 1 dimensional particle in the well is 

$$ ltan(la) = k   $$

with

$$ l = \sqrt{2m(V_0 -\epsilon)/\hbar^2}, k = \sqrt{2m\epsilon}/\hbar  $$

This equation can be solved numerically in the form 

$$ F(\epsilon) = ltan(la) - k = 0  $$

to find the bound state energy 

$$ E_0 = -\epsilon $$

## 2. Monte Carlo Simulation: Pi Estimation

This program estimates pi by considering a unit circle enclosed in a square.
In order to estimate pi, the hit and miss method was employed, we consider
a 2 x 2 square piece of paper with an inscribed circle of radius one, we then simulate throwing
darts at the sqaure and we have the following relations:
    
 $$\frac{number\ of\ dots\ inside\ circle}{total\ number\ of\ dots\} = \frac{area\ of\ circle}{area\ of\ square}$$
