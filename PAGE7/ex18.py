import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('health_screenings_2020_1000ea.xlsx')

female_data=data.loc[data.gender==2,['gender', 'height']]

plt.figure(figsize=(10,6))
plt.hist(female_data['height'], bins=7, label='Female')

plt.xlim(130,180)
plt.xlabel('height')
plt.ylabel('frequency')
plt.title('2020 Health Screenings Female Height Histogram')
plt.legend()
plt.grid()
plt.show()

#그룹 히스토그램 그리기 

male_data = data.loc[data.gender==1, ['gender', 'height']]

plt.figure(figsize=(10,6))
plt.hist(male_data['height'], bins=7, alpha=0.5, label='Male')
plt.hist(female_data['height'], bins=7, alpha=0.5, label='Female')

#alpha 가 투명도 설정인가? 

plt.xlim(130,195)
plt.xlabel('height')
plt.ylabel('frequency')
plt.title('2020 Health Screenings Male & Female Hight Group Histogram')
plt.legend()
plt.grid()
plt.show()

#그룹 누적 히스토그램 그리기 

import numpy as np
height = np.array([male_data['height'], female_data['height']], dtype=object)

plt.figure(figsize=(10,6))
plt.hist(height, bins=6, label=['Male', 'Female'], stacked=True)

#bins = 계급 계수 = ? 

plt.xlim(130,195)
plt.xlabel('height')
plt.ylabel('frequency')
plt.title('2020 Health Screenings Male & Female Height Stacked Histogram')
plt.legend()
plt.show()

