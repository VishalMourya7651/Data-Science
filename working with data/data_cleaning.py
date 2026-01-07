import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('titanic')
#print(df)

#print(df.isnull().sum())                #kaha kaha pe kitna missing value hai

#sns.heatmap(df.isnull())
#plt.show()

#df.dropna()

#print(df.dropna().shape)                #deleting All null value's row from data set
                                

#print(df.dropna(axis=1).shape)              #NOW DELETING ALL NULL VALUE'S COLOUM
         

                                   # DELETING row or COLOUM is not good for load_dataset


                            #    ******Imputation missing value by mean meadian mode********

                                    #first method by mean value imputation 

#sns.distplot(df['age'])
sns.histplot(df['age'],kde=True)
#plt.show()

#print(df.head())

df['age_mean']=df['age'].fillna(df['age'].mean())
#print(df[['age_mean','age']]) 


sns.histplot(df['age_mean'],kde=True)
#plt.show()

#print(df)

df['age_median']=df['age'].fillna(df['age'].median())
#print(df[df['embarked'].isnull()])
#print(df['embarked'].unique())
mode_value=df[df['embarked'].notna()]['embarked'].mode()[0]


df['embarked_mode']=df['embarked'].fillna(mode_value)
print(df[['embarked_mode','embarked']])