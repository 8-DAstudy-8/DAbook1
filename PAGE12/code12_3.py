#pos(): 품사 정보를 추가하여 형태소로 토큰화한 결과를 튜플로 쌍을 이루어 반환 


from konlpy.tag import Okt
okt = Okt()

sentence_tag=okt.pos('달이 참 예쁘다고')
print(sentence_tag)
sentence_tag=okt.pos('달이 참 예쁘다고', join=True)
print(sentence_tag)
