import matplotlib.pyplot as plt
import numpy as np
import random
x=np.random.randint(10,60,(50))
no=[47, 50, 19 ,29, 45, 20, 54, 16, 40, 23, 29 ,35 ,20 ,22 ,18 ,55 ,52 ,22 ,48 ,56 ,16 ,28 ,24 ,27,
 45 ,11, 29, 54, 54, 49, 50, 31, 42, 19 ,13 ,53 ,17, 55, 40, 15 ,17 ,16 ,28 ,53 ,43 ,49 ,15 ,26,
 54, 27]

l=[10,20,30,40,50,60]

plt.title("Record") 
plt.xlabel("python")
plt.ylabel("numbers")

plt.hist(no,color='r',edgecolor='g',bins=l,histtype="barstacked",rwidth=0.3,log=True,label="code")
#plt.hist(no,"auto",(0,100),color='r',edgecolor='g',bottom=10)

plt.axvline(45,color="pink",label="divider")
plt.grid()
plt.legend()
plt.show()