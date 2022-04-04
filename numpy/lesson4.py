import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# we can change type with a.dtype = 'float64'

# size
print(a.size)
# item size in bites
print(a.itemsize)
# size array
print(a.size * a.itemsize)

b = np.ones((3, 4, 5))
print(b)

# count axis
print(b.ndim)
# size axises
print(b.shape)
# edit array with shape, not new array
b.shape = 60
print(b)
b.shape = 12, 5
print(b)
# reshape, one array but diff views of array data
c = b.reshape(3, 2, 10)
print(c)
b[0, 0] = 10
print(c)
print(b)

d = b.T
print(d)

# views copy
zx = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a.view()
print(b)
a.shape = 3, 3
print(a)
print(b)
# copy data

zxc = np.array(zx)
zx[0] = 5
print(zx)
print(zxc)
