#시본 스웜 플롯 그래프 그리기

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
#데이터 전처리 
data=pd.read_excel('health_screenings_2020_1000ea.xlsx')
data6=data.loc[:,['gender','weight', 'waist']]
data6.loc[data6['gender']==1, ['gender']] = 'Male'
data6.loc[data6['gender']==2, ['gender']] = 'Female'

#데이터 준비하기 - data
male_data=data6.loc[data6.gender=='Male', ['gender', 'weight', 'waist']]
female_data=data6.loc[data6.gender=='Female', ['gender', 'weight', 'waist']]

male_data_100=male_data.head(100)
female_data_100=female_data.head(100)

plt.figure(figsize=(10,5))
plt.title('Seaborn Swarm Plot Graph')
sns.swarmplot(data=male_data, x='waist', y='weight', hue='gender', palette='dark', size=4)
sns.swarmplot(data=female_data, x='waist', y='weight', hue='gender', palette='Set1', size=4)
plt.xlim(53, 98)
plt.xticks(np.arange(0,46,22.5), labels=[53,75.5,98])
plt.show()