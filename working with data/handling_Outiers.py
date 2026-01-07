import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
lst_marks=[45,32,56,75,89,54,32,89,90,87,67,54,45,98,99,67,74,1000,1100]

minimum,q1,q2,q3,maximum=np.quantile(lst_marks,[0,0.25,0.50,0.75,1.0])

IQR=q3-q1
lower_fence=q1-1.5*(IQR)

higher_fence=q3+1.5*(IQR)

#print(lower_fence)
#print(higher_fence)

outliers=[]
for i in lst_marks:
    if i>0.75 and i<=142.75:           #lower_fence  and  higher_fence
        print("this is not outlier")
    else:
        outliers.append(i)
print(outliers)