import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.datasets import fetch_california_housing
california=fetch_california_housing()
#print(california.keys())


#print(california.DESCR)   #TO DESCRIBE

dataset=pd.DataFrame(california.data,columns=california.feature_names)
#print(dataset.head())

dataset['price']=california.target

#print(dataset.head())


# frist task is completed that is read the dataset


#now second task start that is EDA FE

#print(dataset.isnull().sum())


#print(dataset.corr()) #corelation by row and colom

# now corelation by heat map

sns.heatmap(dataset.corr(),annot=True)
#plt.show()

#third step that is DIVIDE THE DATASET INTO DEPENDENT  AND INDEPENDENT feature

x=dataset.iloc[:,:-1]  # independent feature
y=dataset.iloc[:,-1]    # dependent feature
#print(y.head())

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=10)


from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

#MODEL TRAINING

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(x_train_scaled,y_train)
#print(regressor.coef_)
#print(regressor.intercept_)



#PREDICTON


y_pred_test=regressor.predict(x_test_scaled)
#print(y_pred_test)
#print(y_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error
print(mean_squared_error(y_test,y_pred_test))
print(mean_absolute_error(y_test,y_pred_test))

from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred_test)
print(score)







#PICKLING    convert object ko file

import pickle
pickle.dump(scaler,open('scaler.pkl','wb'))
pickle.dump(regressor,open('regressor.pkl','wb'))


