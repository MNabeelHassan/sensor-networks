import numpy as np
from math import *
import matplotlib.pyplot as plt

# FILL THIS FUNCTION
def rot_cov(angle, scale_x, scale_y):
    cov = [[1, 0], [0, 1]]
    # YOUR CODE HERE
    return cov
    
def extract_angles_from_cov(cov):
    angle1 = 0
    angle2 = 0
    
    # YOUR CODE HERE
    
    print("Angle 1:", angle1*180/pi)
    print("Angle 2:", angle2*180/pi)
    print("Difference:", (angle2-angle1)*180/pi)
    return angle1, angle2

# Build data
mean = [0, 0]
cov = [[22, 7],[7,4]]
# cov = rot_cov(30*pi/180, 5, 1)
print(cov)
extract_angles_from_cov(cov)

# Make a scatter plot of 1000 points following the mean and covariance
x, y = np.random.multivariate_normal(mean, cov, 1000).T

# ...and plot
fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(x, y)
ax.axis("equal")
plt.show()
