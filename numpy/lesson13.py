import numpy as np

# translation numpy alg
a = np.array([1, 2, 3, 10, 20, 30])
b = np.array([2])

print(a * b)
# error lower. len must be equal, or 1 array should have len=1
#b = np.array([2, 3])
#print(a * b)

a = np.arange(1, 10).reshape(3, 3)
b = np.array([4, 5, 6])
# in math we cant a + b, but in numpy we can with translatin. b come to a.array size. a =3 x 3, b 1x3
a = np.arange(6).reshape(3, 1, 2)
b = np.ones(4).reshape(2, 2)

c = a * b
print(c)
print(c.shape) # but we cant a * b when a.size=2,3,1

