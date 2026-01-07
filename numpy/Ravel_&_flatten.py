import numpy as np
# CONVERT MULTI DIMENSIONAL TO 1D
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr)
print("dimension:- ",arr.ndim)
print()

m=arr.ravel()  #TO MAKE ARRAY TO ONE DIMENSION      arr.flatten()
print(m)
print("dimension:- ",m.ndim)


