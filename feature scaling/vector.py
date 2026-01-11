import seaborn as sns
from sklearn.preprocessing import normalize
import pandas as pd 

df=sns.load_dataset('iris')
df1=pd.DataFrame(normalize(df[['sepal_length','sepal_width','petal_length','petal_width']]),columns=['sepal_length','sepal_width','petal_length','petal_width'])
print(df1)

