import pandas as pd
import matplotlib.pyplot as plt
import collections
from wordcloud import WordCloud

from konlpy.tag import Okt
okt = Okt()

#데이터 가져오기
df=pd.read_table('ratings_train.txt')
df.head(4)

#데이터 전처리 : 하나의 아이디로 같은 영화의 리뷰를 반복했는지 확인 & Null 값 있는지 확인 
print(df['id'].nunique())
print(df.isnull().sum())

#null 값이 5개이므로 해당 행 제거 
df=df.dropna(how='any') #null 값이 존재하는 행 제거
print(df.isnull().values.any()) #null 있냐? 

#불용어 제거 : 한글과 공백을 제외하고 모두 제거하기 위해 사용하는 정규표현식 
df['document'] = df['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣]","")
print(df)

#중복 제거 및 결측치 확인 
temp_list=[]
for sentence in df['document']:
    s_list=okt.pos(sentence)
    for word, tag in s_list:
        if tag in ['Noun', 'Adjective']:
            temp_list.append(word)
counts=collections.Counter(temp_list)
tag=counts.most_common(50)
print(tag)

import matplotlib.font_manager as fm
#폰트 설정
font_path = r'D:\nanum-gothic\NanumGothicBold.ttf'
fontprop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = fontprop.get_name()

wc=WordCloud(font_path=font_path, background_color='skyblue', max_font_size=60)
cloud=wc.generate_from_frequencies(dict(tag))

plt.figure(figsize=(10,8))
plt.imshow(cloud)

#상관없는 단어를 삭제하기 [점, 정말, 왜, 말, 그, 없다] 등

list=[]
stopword=['점', '왜', '정말', '말', '그', '없다', '정도', '걸', '뭐', '이건', '영화', '완전', '좀', '있는', '거', '나', '이', '볼', '입니다', '것', '이런', '더', '수', '때']
for sentence in df['document']:
    s_list=okt.pos(sentence)
for word, tag in s_list:
    if word not in stopword:
        if tag in ['Noun', 'Adjective']:
            temp_list.append(word)
counts=collections.Counter(temp_list)
tag=counts.most_common(50)
tag


#워드클라우드 시각화 
wc=WordCloud(font_path=font_path, background_color='white', max_font_size=60)
cloud=wc.generate_from_frequencies(dict(tag))
plt.figure(figsize=(10,8))
plt.imshow(cloud)
