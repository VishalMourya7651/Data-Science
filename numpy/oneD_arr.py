import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.ndim)# Dimension of array
print(arr)



#USER INPUT

m=[]
for i in range(1,5):
    num=int(input("enter number: "))
    m.append(num)
a=np.array(m)  #TO CONVERT LIST TO ARRAY
print(a)    
print(m)

