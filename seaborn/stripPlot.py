import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=sns.load_dataset("tips")

sns.stripplot(x="day",y="total_bill",data=df,hue="sex")
plt.show()