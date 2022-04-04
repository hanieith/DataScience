import numpy as np

# random
a = np.empty(10, dtype='int16')
print(a)
# 1 in diag
b = np.eye(5)
z = np.eye(4, 3)
print(b)
print(z)
# 1 in diag sqrt
sq = np.identity(3)
print(sq)
# zeros
zer = np.zeros((2, 3, 4))
print(zer)
# ones
ones = np.ones([4, 3], dtype='int8')
print(ones)
# full of -3
fl = np.full((6, 6), -3)
print(fl)
# from strings
mat1 = np.mat('1 2 3 4')
mat2 = np.mat('1 2; 3 4')
print(mat1)
print(mat2)
# from lists
lform = [i for i in range(5)]
print(np.mat(lform))
# range in diag
print(np.diag([1, 2, 3]))
# triang on diag
print(np.tri(4))
# zeros on lower and upper main diag
tri = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(np.tril(tri))
print(np.triu(tri)) 
