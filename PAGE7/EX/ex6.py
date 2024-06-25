#그래프 선 모양 

# 실선 '-' , 파선 '--', 점쇄선 '-.', 점선 ':'

import matplotlib.pyplot as plt 
plt.title('Line Graph')
data1=[2,3,4,5]
data2=[8,6,4,2]
plt.plot(data1, color='r', label='dashed', linestyle='--')
plt.plot(data2, color='g', label='doted', linestyle=':')
plt.legend()
plt.show()