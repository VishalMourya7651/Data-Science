import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df1=sns.load_dataset("penguins").head(20)

sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=df1,hue="sex",style="sex",size="sex")
plt.show()