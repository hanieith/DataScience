import numpy as np

# like range in python
print(np.arange(5))
print(np.arange(3, 6))
# we can use floats
print(np.arange(2, 10, 0.5))
print(np.arange(0, np.pi, 0.1))

# like map
print(np.cos(np.arange(0, np.pi, 0.2)))

# linspace div on equal parts
print(np.linspace(0, np.pi, 1))
print(np.linspace(0, np.pi, 2))
print(np.linspace(0, np.pi, 3))
print(np.linspace(0, np.pi, 4))
# logspace equal linspace but with logs
print(np.logspace(0, 1, 3))
# geomspace
print(np.geomspace(1,4,3))
print(np.geomspace(1,16,5))
fcop = np.array([(1,2),(3,4)])
# we can coppy and check this
fcop1 = np.copy(fcop)
fcop1[0][0] = 5
print(fcop)
print(fcop1)
# from function
def getRange(x, y):
    return 100*x + y
# 3 and 4 this is index
a = np.fromfunction(getRange, (3,4))
print(a)
# offen use with lambda func
print(np.fromfunction(lambda x, y: x*100+y, (2,3)))

# from iters
print(np.fromiter("hello", dtype='U1'))
# from generator

def getRangex(N):
    for i in range(N):
        yield i
print(np.fromiter(getRangex(4), dtype='int8'))

# from string

print(np.fromstring('1 2 3', sep=' '))
print(np.fromstring('1, 2, 3', sep=','))