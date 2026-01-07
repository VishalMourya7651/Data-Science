import matplotlib.pyplot as plt

x=[10,20,30,40]
y=["english","hindi","maths","science"]

ex=[0.0,0.4,0.0,0.0]
#plt.pie(x,labels=y,explode=ex)# to cut the part

c=["yellow","magenta","brown","aqua"]
plt.pie(x,labels=y,colors=c,autopct="%0.1f%%",radius=0.9,textprops={"fontsize":10})
plt.legend(loc=1 )
plt.show()
