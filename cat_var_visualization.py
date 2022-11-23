import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('hour.csv')
df=df.drop(['index','date','casual','registered'],axis=1)
col=['season','month','holiday','weekday','year','hour','workingday','weather']

for i in range(0,8,1):
    plt.subplot(3,3,i+1)
    str_temp=col[i]
    title='Avg Demand vs '+str_temp.capitalize()
    plt.title(title)
    cat_list=df[str_temp].unique()
    cat_avg=df.groupby(str_temp).mean()['demand']
    colours=['g','r','m','b']
    plt.bar(cat_list,cat_avg,color=colours)


plt.tight_layout()
plt.show()