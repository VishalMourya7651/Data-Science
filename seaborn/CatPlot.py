import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=sns.load_dataset("tips").head(20)

sns.catplot(x="tip",y="size",data=df,hue="sex")
plt.xticks(rotation="vertical")
plt.show()