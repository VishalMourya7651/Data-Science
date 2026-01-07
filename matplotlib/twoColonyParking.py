import matplotlib.pyplot as plt
import numpy as np 

x=["car","bike","scoty","bicycle"]
y=[30,50,40,80]
z=[20,30,10,15]

width=0.2
p=np.arange(len(x))
p1=[j+ width for j in p]
plt.title("Parking survey")
plt.xlabel("vehicles",fontsize=20)
plt.ylabel("numbers",fontsize=20)

plt.xticks(p+width/2,x,rotation=30)
 
#plt.bar(p,y,color='r')
plt.barh(p,y,color='r')
plt.barh(p1,z,color='g')
plt.show()