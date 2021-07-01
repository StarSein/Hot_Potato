import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math


def proper_plot(x, y, z):
    min_dist = 2
    for a, b, c in plots:
        v_scale = math.sqrt((x-a)**2 + (y-b)**2 + (z-c)**2)
        if v_scale < min_dist:
            min_dist = v_scale
            adj_spot = (a, b, c)
    if 1 <= min_dist <= 1.5:
        i_p = inner_product(x, y, z, adj_spot[0], adj_spot[1], adj_spot[2])
        if i_p > math.sqrt(3) / 2 or i_p == 0:
            return 1
        else:
            return 0
    else:
        return 0


def inner_product(p, q, r, l, m, n):
    return abs(r-n) / math.sqrt((p-l)**2 + (q-m)**2 + (r-n)**2)


fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection='3d')

# Make data. 점과 점 사이의 거리 1mm~1.5mm, 두 점을 연결한 선분이 z축과 이루는 각도가 30도 이내 // 나비의 높이 40mm 너비 80mm 두께 10mm(두께는 지점마다 상이할 수 있다) ??
# 전체 공간(정육면체)의 한 축의 길이 300mm
plots = [(i, j, k) for i in range(0, 301, 30) for j in range(0, 301, 30) for k in range(0, 301, 30)]
count = 1
while len(plots) <= 1000:
    x, y, z = np.random.rand() * 300, np.random.rand() * 300, np.random.rand() * 300
    if proper_plot(x, y, z) == 1:
        plots.append((x, y, z))
        count += 1
        print(count)

l_x, l_y, l_z = [], [], []
for x, y, z in plots:
    l_x.append(x)
    l_y.append(y)
    l_z.append(z)

ax.scatter(l_x, l_y, l_z, marker='o', s=15, c='pink')

plt.show()
