import numpy as np

a = np.array([1, 2, 3, 7, 8, 9])
b = np.array([1, 2, 3, 10, 11, 9])
print(a == b) # return ARRAU #np.equal(a,b)
print(a != b)
# np.greate(a, b)
print(a > b)
# np.less(a,b)
print(a < b)
print(np.array_equal(a,b)) # return TRUE OR FALSE
# min 1 true and then return True
print(np.any(a > 5))
print(np.any(a > b))
# all True
print(np.all(a>5))
print(a / 0) # return INF = INFINITY, dont raise error
# inf * 0 = nan, not a number. nan + number = nan
b = np.array([1, 2, nan, inf, -inf])
# return bool array, where True = inf or nan, use for exception
print(np.isinf(b))
print(np.isnan(b))
indx = np.isinf(b)
# ~ invertion
print(b[~inf])
# np.iscomplex return true false array
# np.isreal() return true false array

X = np.array([True, False, True, False])
Y = np.array([True, True, False, False])
# return True False array, where all True
print(np.logical_and(X,Y))
# 1 true
print(np.logical_or(X,Y))

print(np.logical_not(X,Y))
print(np.logical_xor(X,Y))

# also work like in python 1 = True 0 = False