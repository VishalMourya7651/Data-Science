import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d


x=np.array([1,2,3,4,5])
y=np.array([1,8,27,64,125])

interp1d(x,y,kind='cubic')
x_new=np.linspace(1,5,10)
y_interp=np.interp(x_new,x,y)
#print(y_interp)

plt.scatter(x_new,y_interp)
plt.show()