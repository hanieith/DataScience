import numpy as np

a = np.array([(1, 2), (3, 4)])
b = np.array([(5, 6), (7, 8)])

# union horizontal hstack and vertical vstack and made copy
print(np.hstack([a, b]))
print(np.vstack([a, b]))
print(np.vstack([a, b, b, a]))

a = np.fromiter(range(18), dtype='int8')
b = np.fromiter(range(18), dtype='int8')
a.resize(3, 2, 2)
b.resize(3, 2, 2)

print(np.hstack([a, b]))
print(np.vstack([a, b]))

a = np.fromstring('1 2 3 4', sep=' ')
b = np.fromstring('3 4 5 6', sep=' ')
print(np.hstack([a, b]))
print(np.vstack([a, b]))

# объединения по столбцам 1 с 3, 2 с 4 и тд
print(np.column_stack([a, b]))
# row_stack = vstack
# but only axis 1 or axis 0
# for axis >1 we use concatenate([a,b], axis= n (1,2,3 and other)

a = np.arange(1, 13)
b = np.arange(13, 26)
a.resize(3,3,2)
b.resize(3,3,2)
print(np.concatenate([a,b], axis=0)) # 6 x 3 x 2
print(np.concatenate([a,b], axis=1)) # 3 x 6 x 2
print(np.concatenate([a,b], axis=2))# 3 x 3 x 4

# we can union in row with np.r_[] made array with any items, r made axis 0
# and have string

print(np.r_[1:9, 90, 100])
print(np.r_[np.array([1,2,3]), np.array([4,5,6])])

# np.c_ made union axis 1 and we have matris
print(np.c_[[1,2,3], [3,4,5]])
print(np.c_[np.array([1,2,3]), np.array([4,5,6])])

# we can split also, but need int a/2 on h
# with v we need vector, 2 axis

a = np.arange(10)
print(np.hsplit(a, 2))
a.shape = 10, -1
print(np.vsplit(a, 2))

# with matrix
a = np.arange(12)
a.resize(2,6)
print(np.hsplit(a,2))
print(np.vsplit(a,2))

