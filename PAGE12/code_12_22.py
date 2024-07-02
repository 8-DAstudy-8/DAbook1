import pandas as pd
import matplotlib.pyplot as plt
import collections
from wordcloud import WordCloud
from konlpy.tag import Okt
okt = Okt()

#글꼴 설치 
import matplotlib.font_manager as fm
#폰트 설정
font_path = r'D:\nanum-gothic\NanumGothicBold.ttf'
fontprop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = fontprop.get_name()


#데이터 가져오기 
dict_df=pd.read_csv('D:\PAGE12\FlimCritics\comment_rank.csv')
#dict_df.head(3)
#dict_df.info()
#dict_df['movie'].unique() #영화 개수 확인 

#dict_df.groupby('movie')['rank'].mean() #영화별 평점 확인 
#dict_df.groupby('movie')['comment'].count()

#영화 리뷰 형태소 분석 

#'고양이 집사' 데이터만 추출하기 
cat_df=dict_df[dict_df.movie=='고양이 집사']
cat_df

#리뷰 분석하기 
temp_list=[]
for sentence in cat_df['comment']:
    s_list=okt.pos(sentence)
    for word, tag in s_list:
        if tag in ['Noun', 'Adjective']:
            temp_list.append(word)
counts=collections.Counter(temp_list)
tag=counts.most_common(50)


#워드클라우드 생성하기 
tag_dic={}
for k,v in tag:
    tag_dic[k] = v

#워드클라우드 시각화 
wc=WordCloud(font_path=font_path, background_color='white', max_font_size=60)
cloud=wc.generate_from_frequencies(tag_dic)
plt.figure(figsize=(10,8))
plt.imshow(cloud)
