import pandas as pd 
df=pd.read_csv('Student Mental health.csv')
#print(df)
#print(df.head())
#print(df.tail()) 
#print(df.columns)
#print(df["What is your course?"])
#print(df[['Timestamp','Age','Marital status']])    #MULTIPLE DATA  IN FORM OF LIST

#print(df.dtypes)

#print(df.describe())
#print(df.dtypes=='object')
#print(df.dtypes[df.dtypes=='object'])
#print(df[df.dtypes[df.dtypes=='object'].index].describe())
#print(df[['Age','Marital status']][2:11])                        #[2:11] is used for slicing

#df['new_col']=0                                                   #TO CREATE NEW COLOM IN THE LAST

#df.insert(loc=2, column="serial",value=0)                        #TO CREATE NEW COLOM IN THE specific position


#print(pd.Categorical(df['Age']))
#print(len(df[df['Age']>18]))                               #HOW MANY PERSON GREATER THAN 18 YEAR AGE
a=df.head(10)

l=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']
f=pd.Series(list(a),index=l)       
print(f)