#산점도 그래프

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('health_screenings_2020_1000ea.xlsx')

heightdata=data['height']
weightdata=data['weight']

plt.figure(figsize=(10,4))
plt.scatter(heightdata, weightdata)

plt.xlabel('height')
plt.ylabel('weight')
plt.title('2020 Health Screenings Scatter Graph')
plt.grid()
plt.show()

#그룹 산점도 그래프 : 기존 산점도 그래프 위에 산점도 그래프 하나 더 그리기 

systolic_data=data['systolic']
diastolic_data=data['diastolic']
blood_sugar_data=data['blood_sugar']

plt.figure(figsize=(10,6))

plt.scatter(systolic_data, diastolic_data, color='r', edgecolors='w', label='systolic*diastolic')
plt.scatter(systolic_data, blood_sugar_data, color='g', edgecolors='w', label='systolic*blood_suger')
plt.scatter(diastolic_data, blood_sugar_data, color='b', edgecolors='w', label='diastolic*blood_suger')

plt.xlim(40,180)
plt.ylim(30,300)
plt.title('2020 Health Screenings Group Scatter Graph')
plt.legend()
plt.grid()
plt.show()