#그림 범위 수동으로 지정하기 

import matplotlib.pyplot as plt
plt.title('X, Y range')
xdata = [5,10,15,20]
ydata = [1,3,5,7]
plt.plot(xdata, ydata, color='b', linestyle='--', marker='o', markersize='10')
plt.xlim(0,25)
plt.ylim(-2,10)
plt.show()

#marker = 선의 점 모양 
