from __future__ import division
__author__ = 'leeladhar'

import nltk
from nltk.book import *


#concordance to get word in text with some context
print text1.concordance("doleful")

#similar lets us see what other words appeared in similar context
print text2.similar("monstrous")

#describe location of word and positional info
print text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

#no of distinct words in text
print len(set(text3))

#sorted text3
print sorted(set(text1))

#lelxical diversity

def lexical_diversity(text):
    return len(set(text)) / len(text)

print lexical_diversity(text1)
print lexical_diversity(text3)

print nltk.FreqDist(text3)
