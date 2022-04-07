import numpy as np

a = np.arange(12)

print(a[2])
print(a[-1])
a[1] = 100
print(a)

a[3:5] = 100, 200
print(a)

print(a[::-1])

for _ in a:
    print(_ + 1, end=' ')
print('')
x = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(x)
print(x[1, 1])
print(x[0])

a = np.arange(1, 82).reshape(3, 3, 3, 3)
print(a)
print(a[:, 1, :, :])
print(a[1, 2, 0, 1])
print(a[0, 0])

a = np.arange(1, 9)
print(a[0])
# a[[0]] its copy !!!
print(a[[0]])
print(a[[0, 3, 7, 5]])
# we can sort with fals/true and made array with "True" func


a = np.arange(1, 9)
print('asdasdsa')
print(a)
i = np.array([[0, 1], [2, 3]])

print(a[i])

a = np.arange(1, 13).reshape(3, 4)
print(a)
indx = [2, 1, 0]
print(a[indx])
indx = np.array([[1, 0], [2, 1]])
print(a[indx])

# for choose elem we need 2 lists

i1 = [1, 2]  # choose elem in strings 0 and 1
i0 = [0, 1]  # choose strings
print(a[i0, i1])

# math action do only 1 time for elem
# +1 to 0 , 1 , 2 elem
a[[0, 0, 1, 2]] += 1
print(a)
