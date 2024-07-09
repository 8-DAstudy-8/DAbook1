from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

import pandas as pd

iris = load_iris()

iris_data = iris.data

iris_label = iris.target 
print('iris target 값:', iris_label)
print('iris target 명:', iris.target_names)

# iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
# iris_df['label'] = iris.target
# iris_df.head(3)


#학습용 데이터와 테스트용 데이터 분리 
#train_test_split() : test size(비율) 파라미터로 구분
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.2, random_state=11)
#random_state 는 호출할 때마다 같은 학습/테스트용 데이터를 만들 수 있게 함 


#의사 결정 트리를 이용해 학습과 예측 수행 
dt_clf = DecisionTreeClassifier(random_state=11)
#학습 수행 
dt_clf.fit(X_train, y_train)
#예측 수행 
pred = dt_clf.predict(X_test)
#예측 성능 평가 (정확도 : 예측 결과가 실제 레이블 값과 얼마나 일치하는지)
from sklearn.metrics import accuracy_score
print('예측 정확도: {0: .4f}'.format(accuracy_score(y_test,pred)))
