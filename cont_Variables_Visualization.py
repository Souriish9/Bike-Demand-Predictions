import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('hour.csv')
df=df.drop(['index','date','casual','registered'],axis=1)

plt.subplot(2,2,1)
plt.title('Temp vs Demand')
plt.scatter(df['temp'],df['demand'],s=2,c='g')

plt.subplot(2,2,2)
plt.title('Humidity vs Demand')
plt.scatter(df['humidity'],df['demand'],s=2,c='m')

plt.subplot(2,2,3)
plt.title('Windspeed vs Demand')
plt.scatter(df['windspeed'],df['demand'],s=2,c='c')

plt.subplot(2,2,4)
plt.title('aTemp vs Demand')
plt.scatter(df['atemp'],df['demand'],s=2,c='b')
plt.tight_layout()

plt.savefig('cont_variables.png')
plt.show()
