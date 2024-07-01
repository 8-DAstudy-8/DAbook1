
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import collections

from konlpy.tag import Okt
okt = Okt()

#폰트 설정
font_path = r'D:\nanum-gothic\NanumGothicBold.ttf'
fontprop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = fontprop.get_name()

#워드클라우드 생성
from wordcloud import WordCloud
wc = WordCloud(font_path = font_path, background_color='skyblue', max_font_size=60)

#텍스트 가져오기
text = '서기가 영원해도 난 마지막 나야 난 나라는 시대의 처음과 끝이야 난 나라는 인류의 기원과 종말이야 넌 나라는 마음의 유일한 무덤이야 넌 나라는 시계의 마지막 시침이야 난 나라는 우주의 빅뱅과 블랙홀이야 난 나라는 신화의 실체와 허구야 난 너의 이름을 닮은 집을 지을 거야'
sentence_tag=okt.pos(text)
adj_list=[]
for word, tag in sentence_tag:
    if tag in ['Noun', 'Adjective']: 
        adj_list.append(word)

#동일한 단어의 빈도수 구하기
counts = collections.Counter(adj_list)
tag=counts.most_common(10)
print(tag)

#wordcloud 텍스트 가져오기 
cloud=wc.generate_from_frequencies(dict(tag))
#워드클라우드 출력 - 맷플롯립 이용 
plt.figure(figsize=(10,8))
plt.imshow(cloud)


