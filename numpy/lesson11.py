import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)

# matrix * matrix in math
print(np.dot(a, b))
print(np.dot(b, a))
# also mat * mat, but better then np.dot shape must be equal
print(np.matmul(a, b))
print(np.matmul(b, a))
# for vectors a @ b, also np.inner and np.outer
# also we can vector * matrix but its need vectos stolbec, a.shape=-1, 1