import numpy as np
from numpy import array, newaxis, flatiter

a = array([[1, 2, 3], [4, 5, 6]])
# print(a.shape)
# print(a.dtype)

# print(a[..., 0])

# b = np.arrange(6, 10)
b = np.arange(start=2, stop=21, step=2)
# print(b)

a = np.arange(60).reshape(5, 4, 3)
# print(a)

aa = np.arange(6, 10)
# print(aa)
bb = np.arange(12, 17)
# print(bb)
table = aa[:, newaxis]*bb
# print(table)

a = np.zeros([4, 5])
b = np.ones(6)
print(b)
# z = np.add(b, b, a[1:3, 0:3] .flat)
# z = np.add([[2., 2., 2.], [2., 2., 2.]])
print(a.tolist())

a = np.arange(40).reshape([2, 4, 5])
b = a.transpose(2, 0, 1)
print(a.shape, b.shape)
print(a.strides, b.strides)

myList = ['A', 'B', 'A', 'C', 'A', 'C', 'B']
uniqueList, count = np.unique(myList, return_counts=True)
print(uniqueList, count)
