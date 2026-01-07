import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df1=sns.load_dataset("penguins")
#print(df1)
sns.barplot(x="island",y="bill_length_mm",data=df1,hue="sex",order=["Torgersen","Biscoe","Dream"],errcolor='r',errwidth=3)
plt.show()