from sklearn.preprocessing import MinMaxScaler
import numpy as np 

train_array = np.arange(0,11).reshape(-1,1)
test_array = np.arange(0,6).reshape(-1,1)

scaler = MinMaxScaler()
scaler.fit(train_array)
train_scaled = scaler.transform(train_array)

print('원본 train_array 데이터: ', np.round(train_array.reshape(-1), 2))
print('Scale 된 train_array 데이터: ', np.round(train_scaled.reshape(-1), 2))

scaler.fit(test_array)
test_scaled = scaler.transform(test_array)

print('원본 train_array 데이터: ', np.round(test_array.reshape(-1), 2))
print('Scale 된 train_array 데이터: ', np.round(test_scaled.reshape(-1), 2))

#올바른 예 

scaler.fit(train_array)
train_scaled = scaler.transform(train_array)
print('원본 train_array 데이터: ', np.round(train_array.reshape(-1), 2))
print('Scale 된 train_array 데이터: ', np.round(train_scaled.reshape(-1), 2))

test_scaled = scaler.transform(test_array)
print('원본 train_array 데이터: ', np.round(test_array.reshape(-1), 2))
print('Scale 된 train_array 데이터: ', np.round(test_scaled.reshape(-1), 2))
