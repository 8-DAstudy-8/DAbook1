import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import openpyxl

data=pd.read_excel('health_screenings_2020_1000ea.xlsx')
data3=data.loc[:,['city_code', 'gender', 'waist']]

male_data=data3[data3['gender']==1].groupby('city_code')['waist'].mean()
female_data=data3[data3['gender']==2].groupby('city_code')['waist'].mean()

plt.figure(figsize=(12,4))

plt.plot(male_data, marker='o', color='b', linestyle='--')
plt.plot(female_data, marker='o', color='r', linestyle='--')

plt.xlabel('Count')
plt.ylabel('Waist')
plt.title('2020 Heath Screenings Waist')
plt.legend()
plt.grid()
plt.show()
