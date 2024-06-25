import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import openpyxl

data=pd.read_excel('health_screenings_2020_1000ea.xlsx')
data6=data.loc[:,['gender', 'height', 'weight', 'waist', 'drinking', 'smoking']]

plt.figure(figsize=(10,6))

correlation_data6=data6.corr()
upp_mat=np.triu(correlation_data6)

sns.heatmap(correlation_data6, annot=True, cmap='YlGnBu', mask=upp_mat)
plt.title('Heat Map Graph')
plt.show()

