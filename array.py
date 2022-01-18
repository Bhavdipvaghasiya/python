import numpy as np
from numpy.core.fromnumeric import partition

# lst=range(5)
# it=iter(lst)
# arr=np.fromiter(it,np.int16)
# print(arr)

# arr=np.arange(2,10,2)
# print(arr)

# arr=np.logspace(1.0,2.0,endpoint=False)
# print(arr)

# arr=np.arange(10)
# s=slice(2,10,3)
# print(arr[5])

# arr=np.arange(10)
# print(arr[2:9:3])

# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr[2,0])
# print(arr[1:])
# print(arr[1])
# print('------------------------')
# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr[...,1])
# print(arr[1,...])
# print(arr[...,1:])


# arr=np.array([[1,2],[3,4],[5,6]])
# y=arr[[0,1,2],[1,1,0]]
# print(y)

# arr=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# row=np.array([[0,1],[1,2]])
# col=np.array([[0,2],[1,1]])
# y=arr[row,col]
# print(y)

# arr=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])

# y=arr[1:4,1:3]
# print(y)

arr=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])

y=arr[arr%2==0]
print(y)
y=arr[arr>6]
print(y)