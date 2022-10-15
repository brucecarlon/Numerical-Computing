import numpy as np
from scipy.optimize import curve_fit  # uses LM algorithm through least sq
import matplotlib.pyplot as plt
from statistics import mean

f = open("DampedData1.txt", "r")  # assume 0.001m uncert on all pos readings
header = f.readline()

i = 0

tdata, ydata, udata = [], [], []
for line in f:
    values = [float(s) for s in line.split()]
    tdata.append(values[0])
    ydata.append(values[1])
    udata.append(0.001)

tdata = np.array(tdata)
ydata = np.array(ydata)


def f(t, A, B, gamma, omega, alpha):
    return A + (B * np.exp(-gamma * t) * np.cos(omega * t - alpha))


A0 = 0.283
B0 = -0.028
gamma0 = 0.2812
omega0 = 21.46227
alpha0 = 3.470977

# list of intial guesses
p0 = [A0, B0, gamma0, omega0, alpha0]
name = ["A", "B", "gamma", "omega", "alpha"]

tmodel = np.linspace(0.0, 5.0, 1000)
ystart = f(tmodel, *p0)
#
popt, pcov = curve_fit(f, tdata, ydata, p0, sigma=udata, absolute_sigma=True)

dymin = (ydata - f(tdata, *popt)) / udata  # Vectorised
min_chisq = sum(dymin * dymin)  # summation step
dof = len(tdata) - len(popt)  # number of degrees of freedom

perr = np.sqrt(np.diag(pcov))


print("Uncertainty in Parameters", perr)
print("Chi square: ", min_chisq)
print("Number of degrees of freedom :", dof)
print("Chi square per degree of freedom: ", min_chisq / dof)
print()

# Calculate uncertainty and format for printing

print("Fitted parameters with 68% C.I.:")

for i, pmin in enumerate(popt):
    print(
        "%2i %-10s %12f +/- %10f "
        % (i, name[i], pmin, np.sqrt(pcov[i, i]) * np.sqrt(min_chisq / dof))
    )
print()

perr = np.sqrt(np.diag(pcov))

print("standard uncertainty of the parameters", perr)

# Calculate and print correlation matrix

print("Correlation matrix")
print("     ")
for i in range(len(popt)):
    print("%-10s " % (name[i],)),
print()

for i in range(len(popt)):
    print("%10s " % (name[i])),
    for j in range(i + 1):
        print("%10f " % (pcov[i, j] / np.sqrt(pcov[i, i] * pcov[j, j]),)),
    print()

x_values = tdata
y_values = ydata


yfit = f(tmodel, *popt)
plt.plot(tmodel, yfit, color="red", label="Line Of Best Fit")
plt.xlabel("Time t (s)")
plt.ylabel("Position y (m)")
plt.title("The result of the model fit to the data of oscillator 1")
plt.plot(tdata, ydata, label="Data", color="blue", marker="P", linestyle="none")
plt.legend()
plt.show()
# plt.savefig("line.png")
