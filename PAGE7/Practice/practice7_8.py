import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import openpyxl

data=pd.read_excel('health_screenings_2020_1000ea.xlsx')
data3=data.loc[:,['city_code', 'gender', 'waist']]

mandata=data3.loc[data3.gender==1, ['gender', 'waist']]
womandata=data3.loc[data3.gender==2, ['gender', 'waist']]

male=np.array(mandata['waist'], dtype=object)
female=np.array(womandata['waist'])

plt.figure(figsize=(10,5))
waist=[male, female]

plt.boxplot(waist, labels=['Male', 'Female'])

plt.xlabel('Gender')
plt.ylabel('Waist')
plt.title('2020 Health Screenings Male & Female Waist Box Plot')
plt.show()

#실행결과가 다름 
