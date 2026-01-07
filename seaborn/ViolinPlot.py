import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=sns.load_dataset("tips")
sns.violinplot(x="day",y="total_bill",data=df,hue="time",palette="jet_r",split=True)
plt.show()