import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import openpyxl

data=pd.read_excel('health_screenings_2020_1000ea.xlsx')
data3=data.loc[:,['city_code', 'gender', 'waist']]

waistData=data3.loc[100:110,['waist']]

plt.figure(figsize=(10,5))

plt.bar(waistData.index, waistData['waist'], color='b')

plt.ylim(50,100)
plt.xlabel('Count')
plt.ylabel('Waist')
plt.title('2020 Health Screenings Waist')
plt.grid()
plt.show()
