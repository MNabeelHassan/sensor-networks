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
    
# FILL THIS FUNCTION
def covariance(values1, values2):
    assert(len(values1) == len(values2))
    cov = 0
    # YOUR CODE HERE
    return cov
    
# FILL THIS FUNCTION
def correlation_coefficient(values1, values2):
    assert(len(values1) == len(values2))
    corr = 0
    return corr

# Create some data
values1 = []
values2 = []
for i in range(10):
    values1.append(randint(-5, 20))
# This is creating simple correlated data
# If you want uncorrelated, comment this out and uncomment the next block
for v in values1:
    values2.append(v+randint(-1,20))
#for i in range(10):
#    values2.append(randint(-1,20))

# Compute -- this is calling your functions
mu1 = mean(values1)
sigma21 = variance(values1)
sigma1 = sqrt(sigma21)

mu2 = mean(values2)
sigma22 = variance(values2)
sigma2 = sqrt(sigma22)

cov = covariance(values1, values2)
corr = correlation_coefficient(values1, values2)

# Output some text...
print("Values 1:  ", values1)
print("Mean 1:    ", mu1)
print("Variance 1:", sigma21)
print("Std Dev 1: ", sigma1)
print("Values 2:  ", values2)
print("Mean 2:    ", mu2)
print("Variance 2:", sigma22)
print("Std Dev 2: ", sigma2)
print("Covariance:", cov)
print("Correlation Coefficent:", corr)

# ...and plot.
# First figure out the min and max for the x axis...
maxval = max([mu1+3*sigma1, mu2+3*sigma2])
minval = min([mu1-3*sigma1, mu2-3*sigma2])
# Plot the individual values...
for v in values1:
    plt.plot(v, 0, "ro")
for v in values2:
    plt.plot(v, 0, "bo")
# build a linear space by dividing maxval-minval by accuracy 100...
x = np.linspace(maxval, minval, 100)
# plot the normal distributions from (mu1,sigma1), (mu2,sigma2), and
# (mu1+mu2/2, cov)
plt.plot(x, stats.norm.pdf(x, mu1, sigma1), label="dist2", color="r")
plt.plot(x, stats.norm.pdf(x, mu2, sigma2), label="dist2", color="b")
plt.plot(x, stats.norm.pdf(x, (mu1+mu2)/2, sqrt(cov)), label="cov", color="g")

plt.legend()
plt.show()
