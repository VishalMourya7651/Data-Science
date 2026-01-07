import numpy as np
import pandas as pd
from sklearn.utils import resample
#set the random seed for reproducibility
np.random.seed(123)


#create a dataframe with two classes
n_samples=1000
class_0_ratio=0.9
n_class_0=int(n_samples*class_0_ratio)

n_class_1=n_samples-n_class_0
#print(n_class_0)


#creating dataset 
class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0,scale=1,size=n_class_0),
    'feature_2': np.random.normal(loc=0,scale=1,size=n_class_0),
    'target': [0]*n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2,scale=1,size=n_class_1),
    'feature_2': np.random.normal(loc=2,scale=1,size=n_class_1),
    'target': [1]*n_class_1
})


df  =  pd.concat([class_0,class_1]).reset_index(drop=True)

print(df['target'].value_counts())



                                                        #UPSAMPLING




df_minority  =  df[df['target']==1]
df_majority  =  df[df['target']==0]



df_minority_upsampled  =  resample(df_minority,replace=True,n_samples=len(df_majority),random_state=42)    #by using sklearn resample

#print(df_minority_upsampled.head())

df_upsampled  =  pd.concat([df_majority,df_minority_upsampled])        #creating dataframe by concatinating 

#print(df_upsampled['target'].value_counts())


                                                        #DOWNSAMPLING

#print(df['target'].value_counts())

df_majority_downsampled  =  resample(df_majority,replace=True,n_samples=len(df_minority),random_state=42)    #by using sklearn resample
#print(df_majority_downsampled)


df_downsample  =  pd.concat([df_minority,df_majority_downsampled])
print(df_downsample['target'].value_counts())