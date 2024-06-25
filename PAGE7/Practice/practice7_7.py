import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import openpyxl

data=pd.read_excel('health_screenings_2020_1000ea.xlsx')
data3=data.loc[:,['city_code', 'gender', 'waist']]

male_data=data3.loc[data3.gender==1, ['gender', 'waist']]
female_data=data3.loc[data3.gender==2, ['gender', 'waist']]

plt.figure(figsize=(10,6))

plt.hist(male_data['waist'], bins=8, alpha=0.5, label='Male')
plt.hist(female_data['waist'], bins=8, alpha=0.5, label='Female')

#bins=?? 

plt.xlim(50,115)
plt.xlabel('Waist')
plt.ylabel('Frequency')
plt.legend()
plt.grid()
plt.show()
