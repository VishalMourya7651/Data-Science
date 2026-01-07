from sklearn.preprocessing import StandardScaler
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=sns.load_dataset('tips')
#print(df.head())

scaler=StandardScaler()  #Object
scaler.fit(df[['total_bill','tip']])
tdf=pd.DataFrame(scaler.transform(df[['total_bill','tip']]),columns=['total_bills','tips'])    
#print(tdf)
sns.histplot(df)
sns.histplot(tdf)
plt.show()