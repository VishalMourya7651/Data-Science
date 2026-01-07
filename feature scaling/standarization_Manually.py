import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df=sns.load_dataset('tips')
#print(df)
total_bills= list(df['total_bill'])
#print(toatl_bills)
mean=np.mean(total_bills)
std=np.std(total_bills)
#print(mean,std)

normlized_data=[]
for i in total_bills:
    z_score=(i-mean)/std
    normlized_data.append(z_score)
#print(normlized_data)
sns.histplot(total_bills)
sns.histplot(normlized_data, kde=True)
plt.show()
