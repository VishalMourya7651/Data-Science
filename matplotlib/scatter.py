import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[4,2,3,5,1,8]

plt.title("Scatter plot")
plt.xlabel("month",fontsize=20)
plt.ylabel("numbers",fontsize=20)

c=['red','orange','green','blue','brown','magenta']

plt.scatter(x,y,color=c,s=150,marker="*")
plt.show()

 