from random import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# FILL THIS FUNCTION
def mean(values):
    mu = 0
    # YOUR CODE HERE
    return mu

# FILL THIS FUNCTION
def variance(values):
    sigma2 = 0
    # YOUR CODE HERE
    return sigma2
    
# Create a 10-size distribution between two bounds
values = []
for i in range(10):
    values.append(randint(-5, 20))
    
# Compute the mean and variance
mu = mean(values)
sigma2 = variance(values)
sigma = sqrt(sigma2)

# Give some output...
print("Values:  ", values)
print("Mean:    ", mu)
print("Variance:", sigma2)
print("Std Dev: ", sigma)

# ...and plot the results
minval = min(values+[mu-3*sigma])
maxval = max(values+[mu+3*sigma])
x = np.linspace(minval, maxval, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
#valplot = []
for v in values:
    plt.plot(v, 0, "ro", label=v)
plt.show()
