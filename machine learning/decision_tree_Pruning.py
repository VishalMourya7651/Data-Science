import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris 
dataset=load_iris()
#print(dataset)
import seaborn as sns
df=sns.load_dataset('iris')
#print(df.head())

#print(dataset.target)

#INDEPENDENT AND DEPENDENT 
x=df.iloc[:,:-1]
y=dataset.target
#print(x)
#print(y)

#Train test split

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.33,random_state=42)

from sklearn.tree import DecisionTreeClassifier
#constructing tree
treeclassifier=DecisionTreeClassifier()
treeclassifier.fit(x_train,y_train)                  #this gives model
from sklearn import tree
plt.figure(figsize=(15,10))
#tree.plot_tree(treeclassifier,filled=True)
#plt.show()


#POST PRUNING
treeclassifier=DecisionTreeClassifier(max_depth=2)
treeclassifier.fit(x_train,y_train)
plt.figure(figsize=(15,10))
#tree.plot_tree(treeclassifier,filled=True)
#plt.show()

#prediction

y_pred=treeclassifier.predict(x_test)
#print(y_pred)

from sklearn.metrics import accuracy_score,classification_report
score=accuracy_score(y_pred,y_test)
#print(score)

classi_report=classification_report(y_pred,y_test)
#print(classi_report)


     #DECISION TREE CLASSIFIER WITH        PRE PRUNING

import warnings
warnings.filterwarnings('ignore')
parameter ={
    'criterion':['ginni','entropy','log_loss'],
    'splitter':['best','random',],
    'max_depth':[1,2,3,4,5],
    'max_features':['auto','sqrt','log2']
}

from sklearn.model_selection import GridSearchCV
clf=GridSearchCV(treeclassifier,param_grid=parameter,cv=5,scoring='accuracy')
clf.fit(x_train,y_train)

#print(clf.best_params_)

y_pred=clf.predict(x_test)
#print(y_pred)

score=accuracy_score(y_pred,y_test)
print(score)