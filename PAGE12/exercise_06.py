import pandas as pd
import matplotlib.pyplot as plt
import collections
from wordcloud import WordCloud
from konlpy.tag import Okt
okt = Okt()

font_path = r'D:\nanum-gothic\NanumGothicBold.ttf'

dict_df=pd.read_excel(r'D:\PAGE12\EwhaUniv\NewsResult_20240402-20240702.xlsx',  engine='openpyxl')
dict_df['본문'].unique() #기사 개수 확인 

#기사 본문 분석하기 
temp_list=[]
for sentence in dict_df['본문']:
    s_list=okt.pos(sentence)
    for word, tag in s_list:
        if tag in ['Noun', 'Adjective']:
            temp_list.append(word)

counts=collections.Counter(temp_list)

top_100_words = counts.most_common(100)

for word, freq in top_100_words:
    print(f'{word}: {freq}회')

# 상위 100개의 단어로 워드클라우드 생성
wordcloud_data = {word: freq for word, freq in top_100_words}
wordcloud = WordCloud(
    font_path=font_path,
    background_color='white',
    width=800,
    height=600
).generate_from_frequencies(wordcloud_data)

# 워드클라우드 표시
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
