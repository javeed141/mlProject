import numpy as np 
l=[[1,2,3,4,5,6],[7,8,9,10,11,12]]

arr1=np.arange(1,6,1)
arr2=np.arange(6,11,1)

arr=np.c_[arr1,arr2]
print(arr[:,-1])
# print(arr2)
