import numpy as np

lst = [1, 2, 3]

a = np.array([1, 2, 3])
print(lst * 2)
print(a * 2)
print(-a)
print(a - 3)
print(a * 5)
print(a // 2)
print(a ** 2)
# elem + elem(*-/)
b = np.array([3, 4, 5])
print(a - b)
print(a + b)
# translation arrays
b = np.arange(1, 7)
b.resize(2, 3)
print(a + b)
print(a * b)
print(a - b)
print(a += 5)  # update a
print(a + 5)  # coppy new array
