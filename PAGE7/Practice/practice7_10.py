import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import openpyxl

data=pd.read_excel('health_screenings_2020_1000ea.xlsx')
data6=data.loc[:,['gender', 'height', 'weight', 'waist', 'drinking', 'smoking']]

data6.loc[data6['gender']==1, ['gender']] = 'Male'
data6.loc[data6['gender']==2, ['gender']] = 'Female'
data6.loc[(data6['smoking']==1) | (data6['smoking']==2), ['smoking']] = 'Non-smoking'
data6.loc[data6['smoking']==3, ['smoking']] = 'Smoking'

smoking=data6.groupby(['gender', 'smoking'])['smoking'].count()
smoking=smoking.to_frame(name='count')
smoking=smoking.reset_index()

plt.figure(figsize=(10,6))
plt.title('Violin Plot Graph')
sns.violinplot(data=data6[data6.weight<120], x='gender', y='weight', hue='smoking')

plt.show()