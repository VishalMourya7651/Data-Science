import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=sns.load_dataset("tips")

sns.pairplot(df,vars=["total_bill","tip"],hue="sex")
plt.show()