import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

var=[1,2,3,4,5,6,7]
var1=[7,6,5,4,3,2,1]

df=pd.DataFrame({"var":var,"var1":var})
#print(df)
#sns.lineplot(x=var,y=var1,data=df)
#plt.plot(var,var1)
df1=sns.load_dataset("penguins")
#print(df1)

sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=df1,hue="sex",style="sex",palette="rainbow_r",markers=["o",">"])
plt.grid()

plt.show()




#plt.show()