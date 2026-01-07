import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df=sns.load_dataset("tips")
#sns.barplot(x="sex",y="total_bill",data=df,hue="sex")
sns.countplot(x="sex",data=df,hue="smoker")
plt.show()