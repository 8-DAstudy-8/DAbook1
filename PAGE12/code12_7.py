#collection : 동일한 값의 자료가 몇 개인지 파악하는데 사용되는 모듈
#counter() 메서드 : 동일한 값의 빈도수를 구하는 메서드
#most_common(n) : 가장 빈도수가 많은 순서대로 n개 추출

import collections
from konlpy.tag import Okt
okt = Okt()

text='서기가 영원해도 난 마지막 나야 난 나라는 시대의 처음과 끝이야 난 나라는 인류의 기원과 종말이야 너 나라는 마음의 유일한 무덤이야 넌 나라는 시계의 마지막 시침이야 난 나라는 우주의 빅뱅과 블랙홀이야 난 나라는 신화의 실체와 허구야 난 너의 이름을 닮은 집을 지을 거야'
sentence_tag=okt.pos(text)

adj_list=[]
for word, tag in sentence_tag:
    if tag in ['Noun', 'Adjective'] : #품사가 명사 또는 형용사인것 추출
        adj_list.append(word)
counts=collections.Counter(adj_list)
tag=counts.most_common(10)
print(tag)
