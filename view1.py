import numpy as np
arr1=np.array([10,20,30,40,50,60])
#arr2=arr1.view()
arr2=arr1.copy()
arr1[0]=100
arr2[1]=200
arr2.shape=3,2
print(id(arr1),arr1)
print(id(arr2),arr2)
