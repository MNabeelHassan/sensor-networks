from random import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# FILL THIS FUNCTION
def mean(values):
    mu = 0
    sum_of_values = 0
    no_of_values = len(values)
    for value in values:
        sum_of_values += value
    mu = sum_of_values / no_of_values
    return mu

# FILL THIS FUNCTION
def variance(values):
    sigma2 = 0
    len_minus_one = len(values) - 1
    mu = mean(values)
    deviation = []
    squared_deviation = []
    for value in values:
        deviation.append(value - mu)
    for dev in deviation:
        squared_deviation.append(dev ** 2)
    sum_of_squared_deviation = 0
    for sq_dev in squared_deviation:
        sum_of_squared_deviation += sq_dev
    sigma2 = sum_of_squared_deviation / len_minus_one
    return sigma2
    
# Create a 10-size distribution between two bounds
values = [-2, 15, 4, 2, 16, 4, 3, -4, 15, 7]
# for i in range(10):
#     values.append(randint(-5, 20))
    
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
