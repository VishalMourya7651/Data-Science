import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df1=sns.load_dataset("penguins")
sns.displot(df1['flipper_length_mm'],kde=True,rug=True)
plt.show()