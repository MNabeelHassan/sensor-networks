import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mean = [0, 0, 0]
cov = [[4, 2, 3],[2, 5, 3], [3, 3, 6]]

x, y, z = np.random.multivariate_normal(mean, cov, 500).T

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z)
ax.axis("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
