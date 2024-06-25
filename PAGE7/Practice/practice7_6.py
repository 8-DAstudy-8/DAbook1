import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import openpyxl

data=pd.read_excel('health_screenings_2020_1000ea.xlsx')
lEyeData=data['eye_left']
rEyeData=data['eye_right']

plt.figure(figsize=(5,5))

plt.scatter(lEyeData, rEyeData)

plt.xlim(0,2.5)
plt.ylim(0,2.5)
plt.xlabel('Eye Left')
plt.ylabel('Eye Right')
plt.title('2020 Health Screenings Scatter Gragh')
plt.show()