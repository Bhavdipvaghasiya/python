import numpy as np
from numpy.core.fromnumeric import reshape

# arr=np.arange(0,60,5)
# arr=arr.reshape(3,4)

# print(arr)
# for x in np.nditer(arr,order='C'):
#     print(x)

# arr=np.arange(0,60,5)
# arr=arr.reshape(3,4)
# for x in np.nditer(arr,op_flags=['readwrite']):
#     x[...]=2*x
# print(arr)

arr=np.array([40,60,66,10,30,360])
arr1=np.array([10])


print(arr)
for x,y in np.nditer([arr,arr1]):
    print(x,y)