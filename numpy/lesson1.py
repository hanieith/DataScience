import numpy as np

a = np.array([1, 2, 3, 4])
print(type(a))
print(a.dtype)

b = np.array([1, 2, "3", True])
print(b.dtype)

print(a[1])

a[1] = 124

print(a[1])

z = np.array([1,2,3,4,5,6,7,8,9])

zx = z.reshape(3,3)
print(zx)

print(zx[1][2])
print(zx[0,2])