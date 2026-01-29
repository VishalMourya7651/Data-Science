import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

dataset=pd.read_csv('Algerian_forest_fires_dataset.csv')
#print(dataset.shape)
#print(dataset.isnull().sum())
#print(dataset[dataset.isnull().any(axis=1)])

#ADD NEW COLOM NAMED REGION
dataset.loc[:122,"Region"]= 0
dataset.loc[122:"Region"]= 1
df=dataset

df[['Region']]=df[['Region']].astype(int)
##print(df.head())
#print(df.tail())

#print(df.isnull().sum())   # if there is 1 to 2 missing value then we will drop that data


#REMOVING NULL VALUE
df=df.dropna().reset_index(drop=True)
#print(df.isnull().sum())

df.columns=df.columns.str.strip()

#change all datatypes from object to int
df[['day','month','year','Temperature','RH','Ws']]=df[['day','month','year','Temperature','RH','Ws']].astype(int)
df[['Rain','FFMC','DMC','DC','ISI','FWI']]=df[['Rain','FFMC','DMC','DC','ISI','FWI']].astype(float)
#print(df.describe())
#print(df.info())

df_copy=df.drop(['day','month','year'],axis=1)  #BECAUSE FIRE KA DAY MONTH YEAR SE KOI RELATION NAHI HAI

#print(df_copy.describe())
#print(df_copy['Classes'].value_counts())
df_copy['Classes']=np.where(df_copy['Classes'].str.contains('not fire'),0,1)
#print(df_copy.tail())
df_copy.to_csv('algerian_forest.csv',index=False)




plt.style.use('seaborn-v0_8')

#df_copy = df.copy()
#df_copy.hist(bins=50, figsize=(20, 15))

sns.heatmap(df_copy.corr(),annot=True)

plt.show()

