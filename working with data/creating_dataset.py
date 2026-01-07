import numpy as np
import pandas as pd

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


df=pd.concat([class_0,class_1]).reset_index(drop=True)
print(df)
print(df['target'].value_counts())