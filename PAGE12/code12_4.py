#pharses(): 문장 내의 단어들을 하나의 구(phrase) 로 인식하여 해당 구를 하나의 단어로 처리하는 방법 

from konlpy.tag import Okt
okt = Okt()

sentence=okt.phrases('달이 참 예쁘다고')
print(sentence)