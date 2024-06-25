#선 그래프 

import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

data=pd.read_excel('fine_dust.xlsx', index_col='area')

plt.figure(figsize=(15,4))
for year in range(2016,2019):
    chartdata=data[year]
    plt.plot(chartdata, marker='s', label=year)

plt.xlabel('area')
plt.ylabel('micrometer')
plt.title('2016~2019 Fine Dust Line Graph')
plt.legend()
plt.grid()
plt.show()




