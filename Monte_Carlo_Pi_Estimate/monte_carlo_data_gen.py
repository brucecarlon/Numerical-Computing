import numpy as np
import scipy as sp
import scipy.stats as stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.mlab as mlab
import numpy.random as random

numbers = random.normal(40, 2, 61)  # 60 random numbers

axis = np.arange(0, 61, 1)  # labeling of the numbers

# creating a text file called random60 with two columns one for the numbering system
# and the other with the the random numbers created above
# f = open('random60.txt', 'w')
# f.write('Random numbers drawn from Gaussian with mu = 40.0 and sigma = 2.0 \n')
# i = 0

# for i in range(1,61):
#    val = str(axis[i])+'\t'+str(numbers[i])+'\n'
#  f.write(val)
#    i += 1
# f.close()

# create histogram
g = open("random60.txt", "r")
header = g.readline()
data = np.zeros(60)
i = 0

x, y = [], []
for line in g:
    values = [float(s) for s in line.split()]
    x.append(values[0])
    y.append(values[1])

x = np.array(x)
y = np.array(y)

mu = 40
sigma = 2

mean = np.mean(y)
var = np.var(y)
std = np.sqrt(np.var(y))

gaus = (np.exp(-((mean - std) ** 2) / (2 * (std) ** 2))) / (
    std * (np.sqrt(2 * np.pi))
)

# Gausian
n_sort = np.sort(y)

# Gausian with bell shape and extracted values
f = np.exp(-np.square(n_sort - mean) / 2 * (std) ** 2) / (
    std * (np.sqrt(2 * np.pi))
)
# print(len(f))
sumv = sum(f)
# print(sumv)
plt.plot(n_sort, f, "r-", label="Gaussian (Red) with Extracted Values")
minv = min(y)
maxv = max(y)
sumv = sum(y)

# secondary gausian with bell shape and intented values
f = np.exp(-np.square(n_sort - 40) / 2 * (std) ** 2) / (
    std * (np.sqrt(2 * np.pi))
)
sumv = sum(f)
plt.plot(n_sort, f, "c-", label="Guassian (cyan) with intended values")

# print(minv)
# print(maxv)
print(sumv)

binwidth = 0.5
bins = np.arange(np.floor(min(y)), np.floor(max(y)) + 1, binwidth)
result = plt.hist(y, bins)
plt.xlabel("x")
plt.ylabel("Occurnace")


# Gausian with no bell shape and extracred values
q = np.linspace(minv, maxv, 5)
dq = result[1][1] - result[1][0]
scale = len(y) * dq
plt.plot(
    q,
    mlab.normpdf(q, mean, std),
    "y-",
    label="Guassian (yellow) with extracted values",
)
plt.legend(loc="upper left")
plt.show()

# secondary gausian not bell shaped and with inted values
w = np.linspace(minv, maxv, 5)
dw = result[1][1] - result[1][0]
scale = len(y) * dw
# plt.plot(w,mlab.normpdf(w, 40, 2),'g-')

print(mean)
print(std)
