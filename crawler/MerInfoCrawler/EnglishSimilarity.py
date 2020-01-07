import logging
from gensim import models, similarities, corpora
from collections import defaultdict
import os

# 停用词
stoplist = set('for a of the and to in'.split())
# 英文标点符号
punctions = [' ', '\n', '\t', ',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
documents = open('en.txt', 'r')
lines = documents.readlines()
print(lines)
texts = [[word for word in document.lower().split() if word not in stoplist and punctions]
         for document in lines]
print(texts)
# 词标记
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts1 = [[token for token in text if frequency[token] > 1] for text in texts]
print(texts1)
# 建立词典和语料库
dictionary = corpora.Dictionary(texts)
dictionary.save('desc_en.dict')
# print(dictionary)
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('desc_en.mm', corpus)
print(corpus)
# 下载存储的建立好的词典和语料库
if os.path.exists('desc_en.dict'):
    dictionary = corpora.Dictionary.load('desc_en.dict')
    corpus = corpora.MmCorpus('desc_en.mm')
    print('used english files generated')
else:
    print('please generate the files again!')

# 建立模型
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

# make transformations serialized
lsi_model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
corpus_lsi = lsi_model[corpus_tfidf]

index = similarities.MatrixSimilarity(lsi_model[corpus])


# test english string

en_str = 'From 20 days to 2 hours, the inspection efficiency of Shenzhen Power Supply Bureau of China Southern Power Grid increased by 80 times'
en_str_vec = dictionary.doc2bow(en_str.lower().split())
print(en_str_vec)
lsi_str_vec1 = lsi_model[en_str_vec]
print(lsi_str_vec1)
# 计算相似度
sims = index[lsi_str_vec1]
print(list(enumerate(sims)))
# sorted
print(1111111111111)
simsorted = sorted(enumerate(sims), key=lambda item: -item[1])
print(simsorted)

