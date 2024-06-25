#상자수염 그래프 

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('health_screenings_2020_1000ea.xlsx')

import numpy as np 

female_data=data.loc[data.gender==2,['gender', 'height']]
male_data = data.loc[data.gender==1, ['gender', 'height']]

height = np.array([male_data['height'], female_data['height']], dtype=object)

plt.figure(figsize=(8,5))
plt.boxplot(height, labels=['Male', 'Female'])

plt.ylim(130,200)
plt.xlabel('gender')
plt.ylabel('height')
plt.title('2020 Health Screening Male & Female Height Box Plot')
plt.show()

#가로 상자수염 그래프 

plt.figure(figsize=(8,5))
plt.boxplot(height, labels=['Male', 'Female'], vert=False)

plt.xlim(130,200)
plt.ylabel('gender')
plt.xlabel('height')
plt.title('2020 health Screening Male & Female Height Box Plot')
plt.show()