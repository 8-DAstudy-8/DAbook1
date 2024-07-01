from konlpy.tag import Okt
okt = Okt()

text=input()
sentence_tag=okt.pos(text)
print(sentence_tag)
