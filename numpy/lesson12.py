import numpy as np

a = np.array([1,2,3,4,4,3,2,1])
print(a)
# set
setA = np.unique(a)
print(setA)
# set + counters
setAcount = np.unique(a, return_counts=True)
print(setAcount)
# index first pos elem
setAcount = np.unique(a, return_index=True)
print(setAcount)
# all posses, second array show posses of num in 1 array
setAcount = np.unique(a, return_inverse=True)
print(setAcount)
setA, indx = np.unique(a, return_inverse=True)
print(setA[indx])
# aslo its work with matrix and have 1 axis array with unic numbers
# show True or false if num 1 in num2 array
x = np.array([0,1,2,3])
y = np.array([1,2,3,4,5,6,7,8])
print(np.in1d(x,y))
# np.intersect1d = set intersection
# np.uniond1d = set + set
# and other np.setdiff1d(setA, setB) = SetA-SetB unic in sec a without in setB