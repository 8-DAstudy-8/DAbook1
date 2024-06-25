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


#기본 막대 그래프 

fig=plt.figure(figsize=(17,6))
fig.suptitle('2020 Health Screenings Drinking & Smoking Type Bar Graph', fontweight='bold')
index = np.arange(4)

fig.add_subplot(1,2,1)
#1행 2열의 서브플롯 중 첫 번째 서브플롯을 생성 
plt.bar(index, drinking['count'])
plt.title('Drinking Type')
plt.ylabel('Count')
plt.xticks(index, ['Non-driniking(Female)', 'Drinking(Female)', 'Non-drinking(Male)', 'Drinking(Male)'])

fig.add_subplot(1,2,2)
plt.bar(index, smoking['count'])
plt.title('Smoking Type')
plt.ylabel('Count')
plt.xticks(index, ['Non-smoking(Female)', 'Smoking(Female)', 'Non-smoking(Male)', 'Smoking(Male)'])

plt.show()

#시본 막대 그래프 그리기

fig = plt.figure(figsize=(17,6))
area1 = fig.add_subplot(1,2,1)
area2 = fig.add_subplot(1,2,2)

ax1 = sns.barplot(data=drinking, x='gender', y='count', hue='drinking', ax=area1)
ax2 = sns.barplot(data=smoking, x='gender', y='count', hue='smoking', ax=area2)

fig.subtitle('2020 Health Screenings Drinking & Smoking Type Seaborn Bar Graph', fontweight='bold')
area1.set_title('Drinking Type')
area2.set_title('Smoking Type')

plt.show()
