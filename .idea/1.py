import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_continuous

COUNT_FIRST = 100
COUNT_SECOND = 1000
COUNT_THIRD = 1000

class Distribution(rv_continuous):
    # override Cumulative distribution function
    def _cdf(self, x, *args):
        return (0.5 * np.exp(x)) if (x <= 0) else (1 - 0.5 * np.exp(-x))

# density
def f(x):
    return (0.5 * np.exp(x)) if (x <= 0) else (0.5 * np.exp(-x))



dist = Distribution(name='gaussian')
#x = d.rvs()
print("Created")


# create first selection
selection = dist.rvs(size=COUNT_FIRST)
print("First")

fig = plt.figure()
plt.hist(selection, bins=10)
plt.grid(True)
plt.title("Our distribution at " + str(COUNT_FIRST) + " values")
plt.xlabel("Value")
plt.ylabel("Times")


# create second selection
selection = dist.rvs(size=COUNT_SECOND)
print("Second")

fig = plt.figure()
plt.hist(selection, bins=10)
plt.grid(True)
plt.title("Our distribution at " + str(COUNT_SECOND) + " values")
plt.xlabel("Value")
plt.ylabel("Times")


# create third selection
selection = [sum(dist.rvs(size=30)) for i in range(COUNT_THIRD)]
print("Third")
fig = plt.figure()
plt.hist(selection, bins=10)
plt.grid(True)
plt.title("Distribution Yi = SUM Xij where j=1...30, i=1..." + str(COUNT_THIRD))
plt.xlabel("Value")
plt.ylabel("Times")


# create density
fig = plt.figure()
sequence = np.arange(-10.0, 10.0, 0.1)
vf = np.vectorize(f)
plt.plot(sequence, vf(sequence), "-bo")
plt.grid(True)
plt.title("Density function")
plt.xlabel("Value")
plt.ylabel("Density")


# show results
plt.show()