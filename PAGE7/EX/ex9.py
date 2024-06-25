import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

data=pd.read_excel('fine_dust.xlsx', index_col='area')
data2018=data[2018]

plt.figure(figsize=(15,4))
plt.plot(data2018,color='b', marker='o')
plt.xlabel('area')
plt.ylabel('micrometer')
plt.title('2018 Fine Dust Line Graph')
plt.grid()
plt.show()

#openpyxl

