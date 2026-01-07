import numpy as np 
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([1,4,9,16,25])

p=np.polyfit(x,y,10)
x_new=np.linspace(1,5,10)
y_interp=np.polyval(p,x_new)

plt.scatter(x_new,y_interp)
plt.show()