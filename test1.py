import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('hour.csv')
df=df.drop(['index','date','casual','registered'],axis=1)

df.hist(rwidth=0.9)
plt.tight_layout()
plt.show()