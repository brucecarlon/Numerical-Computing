# Numerical Computing
> A collection of numeric solutions produced throughout my undergraduate studies


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
 
 ## 3. Newton-Rampson Method
 
    Given a function, its derivative, initial guess, threshold between two
    consecutive guesses and max number of iterations: finds the closest root
    to the initial guess.
    
    returns the root found and the number of iterations to find root
    otherwise return None value if no roots are found
    
 ## 4. Damped Oscillator Model Fitting
 We perform a Least-Sqaure Fitting, which the processing of optimizing a model by minimizing the chi-square value. The chi-square value is a measure of how well the model fits the actuall data and is given by:
 
 $$ \chi^2 = \Sigma^{N}_{i = 0}  \frac{(y_i - f(t_i : [p]) )^2}{u_i^2} $$
 
 We consider an under damped oscillator which can be modelled as
 
 $$ y(t) = A + Be^{-\gamma t}cos(\\omega t - \alpha  $$

We use he Levenberg - Marquardt algorithm to minimize the chi-squared value and find the parameters that optimze the fit.

## Author info
Bruce Mvubele \
[LinkedIn](https://www.linkedin.com/in/bruce-mvubele-494105143/) \
e-mail: cmvubele@gmail.com
