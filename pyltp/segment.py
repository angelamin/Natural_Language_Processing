# -*- coding: utf-8 -*-
from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load("/Users/xiamin/Downloads/ltp_data/cws.model")
words = segmentor.segment("元芳你怎么看")
print "|".join(words)
segmentor.release()