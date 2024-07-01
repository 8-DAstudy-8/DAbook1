#!/usr/bin/env python3

from konlpy.tag import Okt
okt = Okt()
token=okt.morphs('꿈의 거처')
print(token)