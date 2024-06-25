#판다스 내장 시각화 옵션 pandas_plot()_kind

#1
import pandas as pd
my_score=[[50,90,95], [60,75,100], [75,85,90], [85,75,90], [95,80,85], [90,85,80], [95,80,75]]
subject=['kor', 'math', 'eng']
df=pd.DataFrame(my_score, columns=subject)
df.plot(kind='line')
df.plot(kind='area')
df.plot(kind='box')

#interactive Window? 
