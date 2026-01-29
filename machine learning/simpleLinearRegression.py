import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


#load dataset
df=pd.read_csv('height_weight_linear_101.csv')
#print(df)
#plt.scatter(df['Weight'],df['Height'])
plt.xlabel('weight')
plt.ylabel('height')
#plt.show()
#print(df.isnull().sum())

#DIVIDE THE DATASET -{ DEPENDENT FEATURE AND INDEPENDENT FEATURE}


x=df[['Weight']]
y=df[['Height']]


#Divde dataset into TRAIN and TEST 


from sklearn.model_selection import train_test_split


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=42)

#print(x_train)


#Standard scale

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

x_train=scaler.fit_transform(x_train)
#print(x_train)
x_test=scaler.transform(x_test)
#plt.scatter(x_train,y_train)
#plt.show()


#model training


from sklearn.linear_model import LinearRegression

regressor=LinearRegression()

##Traing the data set
regressor.fit(x_train,y_train)

#in y=mx+b     here we get b by below code
#print(regressor.intercept_)

#slope =below code
#print(regressor.coef_)

plt.scatter(x_train,y_train)
plt.plot(x_train,regressor.predict(x_train),'r')
#plt.show()


#prediction for test data

y_pred_test=regressor.predict(x_test)
#print(y_pred_test)


#MAE MSE RMSE

from sklearn.metrics import mean_squared_error, mean_absolute_error
mse=mean_squared_error(y_test,y_pred_test)
mae=mean_absolute_error(y_test,y_pred_test)
rmse=np.sqrt(mse)
print(mse)
print(mae)
print(rmse)


#to check the accuracy == R squared  and Adjusted Rsquared

from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred_test)
print(score)    #0.9115749166216336 accuracy



