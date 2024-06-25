#막대 그래프

import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

data=pd.read_excel('fine_dust.xlsx', index_col='area')
data2017 = data[2017]

plt.figure(figsize=(15,4))
plt.bar(data2017.index, data2017, color='g')
plt.ylim(35,55)
plt.xlabel('area')
plt.ylabel('micormeter')
plt.title('2017 Fine Dust Bar Graph')
plt.grid()
plt.show()

#지역별 미세먼지 그룹 세로 막대 그래프 

import numpy as np
index = np.arange(4)

plt.figure(figsize=(15,4))

data4 = data.loc['Gyeonggi':'Daegu', 2016:2019]
for year in range(2016, 2020):
    chartdata=data4[year]
    plt.bar(index, chartdata, width=0.2, label=year)
    index = index + 0.2 #막대 그래프가 출력되는 위치를 0.2씩 이동 

plt.ylim(35,55)
plt.xlabel('area')
plt.ylabel('micrometer')
plt.xticks(index-0.5,['Gyeonggi', 'Incheon', 'Busan', 'Daegu']) #x축 눈금을 가운데로 지정하기 위해 0.5 빼주기 
plt.title('2016~2019 Fine Dust Group Bar Graph')
plt.legend()
plt.show()

#2016-2019 지역별 미세먼지 그룹 누적 가로 막대 그래프 

plt.figure(figsize=(10,4))
index = np.arange(4)

data4 = data.loc['Gyeonggi':'Daegu', 2016:2019]
for year in range(2016, 2020):
    chartdata=data4[year]
    plt.barh(index, chartdata, label=year)

plt.xlim(30,55)
plt.ylabel('area')
plt.xlabel('micrometer')
plt.yticks(index, ['Gyeonggi', 'Incheon', 'Busan','Daegu'])
plt.title('2016-2019 Fine Dust Group Barh Graph')
plt.legend()
plt.show()


