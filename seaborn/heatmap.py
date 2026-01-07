import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

var=np.linspace(1,10,20).reshape(4,5)
data=sns.load_dataset("anagrams")

x=data.drop(columns=["attnr"],axis=1)

sns.heatmap(x,vmin=0,vmax=20,cmap="gist_heat",annot=True)
plt.show()