import numpy as np

a = np.arange(10)
print(a)
a.shape = 2, 5
print(a)

b = a.reshape(10)
print(b)
# -1 = other count(remainder)
a.shape = -1, 2
print(a)
# matrix in 1 axis a.ravel()
print(a.ravel())
a.shape = -1
print(a)
# resize arrm, edit a, dont return arr, a.resize(refcheck=False) for dont checking
a.resize(2, 5)
print(a)
# T made new view
a = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
print(a)
b = a.T
print(b)
# dont have second axis
x = np.arange(1, 10)
print(x)
print(x.T)
# for T
x.shape = 1, -1
print(x)
print(x.T)

# work with axis
# matrix 8 x 2 x 2
zxc = np.arange(32).reshape(8, 2, 2)
print(zxc)
# made new views, add new axis
zxc1 = np.expand_dims(zxc, axis=0)
print(zxc1.shape)
# add items in axis
a = np.append(zxc1, zxc1, axis=0)
print(a)
# delete item
b = np.delete(a, 0, axis=0)
print('DELETE')
print(b)
print(b.shape)
# add last axis
b = np.expand_dims(a, axis=-1)
print(b.shape)
# delete all axis with 1 elem
c = np.squeeze(b)
print(c.shape)
c = np.squeeze(b, axis=-1)
print(c.shape)

# new axisses
a = np.arange(1,10)
print(a)
print(a.shape)
b = a[np.newaxis,:]
print(b.shape)

