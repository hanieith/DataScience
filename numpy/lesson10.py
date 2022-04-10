import numpy as np

a = np.array([1, 2, 3, 10, 20, 30])

print(a.sum())
# среднее арифм.
print(a.mean())
print(a.max())
print(a.min())

a.resize((3, 2))
print(a)
print(a.sum())
# axis functs.
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.max(axis=0))
print(a.min(axis=1))
# and many other np.funcs.

a = np.array([-1, 1, 5, -44, 32, 2.5])
print(np.amax(a))
print(np.amin(a))
print(np.round(a))
# return index of elem
print(np.argmax(a))
print(np.argmin(a))
# also with mani axis matrix
a.resize(2,3)
print(np.amax(a, axis=0))
# random array, array len 4 in diap 5-15
print(np.random.randint(5, 15, size=4))
# we can shuffle with np.random.shuffle
# and other match static functions.
