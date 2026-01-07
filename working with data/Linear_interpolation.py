import numpy as np 
import matplotlib.pyplot as plt 



x=np.array([1,2,3,4,5])
y=np.array([2,4,6,8,10])

x_new=np.linspace(1,5,10)
y_interp=np.interp(x_new,x,y)


print(y_interp)
plt.scatter(x_new,y_interp)
plt.show()