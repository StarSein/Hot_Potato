import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection='3d')


l_x, l_y, l_z = [], [], []
out_str = ""
for i in range(1, 26):
    for j in range(1, 26):
        for k in range(1, 26):
            x = 4 * i - np.random.rand() * 3
            y = 4 * j - np.random.rand() * 3
            z = 4 * k - np.random.rand() * 3
            l_x.append(x)
            l_y.append(y)
            l_z.append(z)
            out_str = "%s%f %f %f\n" % (out_str, x, y, z)


ax.scatter(l_x, l_y, l_z, marker='o', s=15, c='orange')

plt.show()

with open('3d_scatter_plot.out', 'w') as outFile:
    outFile.write(out_str.rstrip())
