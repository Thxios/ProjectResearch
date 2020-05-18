import numpy as np


a = np.array([
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [14, 13, 12, 11, 10],
    [-1, -5, -2, -3, -4],
])

print(a)
b = [*np.argwhere(a)]
# print(a.flatten())
print(b)
b.sort(key=lambda x: a[x[0], x[1]])
print(b)
# print(a[1, 2])
