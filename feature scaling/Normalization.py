import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df=sns.load_dataset('taxis')
#print(df)


min_max=MinMaxScaler()
df1=min_max.fit(df[['distance','fare','tip']])
df2=pd.DataFrame(min_max.transform(df[['distance','fare','tip']]),columns=['distace','fare','tip'])
print(df2)