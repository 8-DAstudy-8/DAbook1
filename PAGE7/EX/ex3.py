#범례 


import matplotlib.pyplot as plt 
plt.title('Line Graph')
data1=[2,3,4,5]
data2=[8,6,4,2]
plt.plot(data1, label= 'asc')
plt.plot(data2, label='desc')
plt.legend()
plt.show()
