import matplotlib.pyplot as plt
x=['car','bike','scoty','bicycle']
y=[40,85,75,35]
plt.title("parking servey")
plt.xlabel("vehicles",fontsize=20)
plt.ylabel("numbers",fontsize=20)

c=['red','yellow','green','magenta']

plt.bar(x,y,width=0.2,color=c,align='center',edgecolor='blue',linewidth=3,linestyle=":",alpha=0.9) #alpha is for less color

plt.legend("Transport")

plt.show()