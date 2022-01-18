import numpy as np
arr1=np.array([10,20,30])
arr2=arr1
arr1[0]=100
arr2[1]=200
print(id(arr1),arr1)
print(id(arr2),arr2)
