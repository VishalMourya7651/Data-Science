import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("algerian_forest.csv")

''' NOW OUR DATA IS CLEAN AND READY FOR TRAINING THE MODEL'''

#Independent and dependent feature   FWI=FIRE WEATHER INDEX
x=df.drop('FWI',axis=1)
#print(x.head())
y=df['FWI']
#print(y.head())



#DIVIDE TRAIN AND TEST 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =  train_test_split(x,y,test_size=0.25,random_state=42)
#print(x_train.head())

#print(x_train.corr())







#MULTI CORREALINEARITY
def correlation(dataset,threshold):
    col_corr=set()
    corr_matrix=dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i,j])>threshold:
                colname=corr_matrix.columns[i]
                col_corr.add(colname)
    return col_corr


corr_feature=correlation(x_train,0.98)                
#print(corr_feature)
x_train.drop(corr_feature,axis=1,inplace=True)
x_test.drop(corr_feature,axis=1,inplace=True)
#print(x_train.shape)







#FEATURE SCALING

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

x_train_scale=scaler.fit_transform(x_train)
x_test_scale=scaler.transform(x_test)


#print(x_train_scale)




#TRAIN START

from sklearn.linear_model import LinearRegression
linreg=LinearRegression()
linreg.fit(x_train_scale,y_train)

y_pred=linreg.predict(x_test_scale)
#print(y_pred)



from sklearn.metrics import mean_absolute_error
mae=mean_absolute_error(y_test,y_pred)
#print(mae)              #THIS IS THE MEAN ABSOLUTE ERROR



#Accuracy                       acuracy=score

from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred)
#print(score)


#LASSO REGRESSION

from sklearn.linear_model import Lasso 
lasso=Lasso()
lasso.fit(x_train_scale,y_train)
y_pred=lasso.predict(x_test_scale)
#print(y_pred)

     #for lasso we find mae and 

mae2=mean_absolute_error(y_test,y_pred)
#print(mae2)     

score2=r2_score(y_test,y_pred)
#print(score2)





#RIDGE REGRESSION

from sklearn.linear_model import Ridge 
ridge=Ridge()

ridge.fit(x_train_scale,y_train)

y_pred=ridge.predict(x_test_scale)
#print(y_pred)

mae3=mean_absolute_error(y_test,y_pred)
#print(mae3)

score=r2_score(y_test,y_pred)
#print(score)









#ELASTIC NET REGRESSION

from sklearn.linear_model import ElasticNet 
elastic=ElasticNet()

elastic.fit(x_train_scale,y_train)                  #training by this line of code

y_pred=elastic.predict(x_test_scale)

#print(y_pred)
mae4=mean_absolute_error(y_test,y_pred)
print(mae4)

score4=r2_score(y_test,y_pred)
print(score4)