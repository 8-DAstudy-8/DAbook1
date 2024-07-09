#원-핫 인코딩 : 피처 값의 유형에 따라 새로운 피쳐를 추가해 고유 값에 해당하는 칼럼에만 1을 표시하는 방식

from sklearn.preprocessing import OneHotEncoder
import numpy as np 

items = ['TV', '냉장고', '전자레인지', '컴퓨터', '선풍기','선풍기', '믹서', '믹서']

#2차원 ndarray로 변환
items = np.array(items).reshape(-1, 1)

#원-핫 인코딩 적용 
oh_encoder = OneHotEncoder()
oh_encoder.fit(items)
oh_labels = oh_encoder.transform(items)

#toarray를 이용해 밀집행렬(?) 로 변환
print(oh_labels.toarray())
print(oh_labels.shape)

#pandas 이용 

import pandas as pd
df = pd.DataFrame({'item' : ['TV', '냉장고', '전자레인지', '컴퓨터', '선풍기','선풍기', '믹서', '믹서']})
pd.get_dummies(df)

#여기 true/false 로 뜸 



