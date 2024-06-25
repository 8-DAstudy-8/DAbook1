import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel('health_screenings_2020_1000ea.xlsx')
data6=data.loc[:,['gender', 'height', 'weight', 'waist', 'drinking', 'smoking']]
data6.loc[data6['gender']==1, ['gender']] = 'Male'
data6.loc[data6['gender']==2, ['gender']] = 'Female'
data6.loc[data6['drinking']==0, ['drinking']] = 'Non-drinking'
data6.loc[data6['drinking']==1, ['drinking']] = 'Drinking'
data6.loc[(data6['smoking']==1) | (data6['smoking']==2), ['smoking']] = 'Non-smoking'
data6.loc[data6['smoking']==3, ['smoking']] = 'Smoking'

drinking = data6.groupby(['gender', 'drinking'])['drinking'].count()
#성별, 음주 여부의 그룹별 개수..?
smoking = data6.groupby(['gender', 'smoking'])['smoking'].count()
drinking = drinking.to_frame(name='count')
smoking = smoking.to_frame(name='count')
#위에서 구한 그룹별 개수의 시리즈를 데이터프레임으로 변경 
drinking=drinking.reset_index()
smoking=smoking.reset_index()
#위에서 그룹화 된 인덱스를 초기화함 

#데이터 준비하기 - data
male_data=data6.loc[data6.gender=='Male', ['gender', 'weight', 'waist', 'drinking', 'smoking']]
female_data=data6.loc[data6.gender=='Female', ['gender', 'weight', 'waist', 'drinking', 'smoking']]

plt.figure(figsize=(10,5))
plt.title('Seaborn Strip Plot Graph')
sns.stripplot(data=male_data, x='waist', y='weight')
sns.stripplot(data=female_data, x='waist', y='weight')

plt.xticks(np.arange(0,127,63), labels=[53,90.5,128]) #? 
plt.show()
