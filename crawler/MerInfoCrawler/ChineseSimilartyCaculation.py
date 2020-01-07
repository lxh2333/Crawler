import codecs
from gensim import corpora, models, similarities
from collections import defaultdict
import jieba

def CSV(new_doc, path):

    f = codecs.open(path, 'rb', 'utf-8')
    documents = f.readlines()
    f.close()


    # 1.文本预处理：中文分词，去除停用词
    #print('1.文本预处理：中文分词，去除停用词')
    # 获取停用词
    stopwords = set()
    file = open("stopwords.txt", 'r', encoding='UTF-8')
    for line in file:
        stopwords.add(line.strip())
    file.close()

    # 将分词、去停用词后的文本数据存储在list类型的texts中
    texts = []
    for line in documents:
        words = ' '.join(jieba.cut(line)).split(' ')  # 利用jieba工具进行中文分词
        text = []
        # 过滤停用词，只保留不属于停用词的词语
        for word in words:
            if word not in stopwords:
                text.append(word)
        texts.append(text)
    #for line in texts:
        #print(line)

    # 待比较的文档也进行预处理（同上）
    words = ' '.join(jieba.cut(new_doc)).split(' ')
    new_text = []
    for word in words:
        if word not in stopwords:
            new_text.append(word)
    #print(new_text)

    # 2.计算词频
    #print('2.计算词频')
    frequency = defaultdict(int)  # 构建一个字典对象
    # 遍历分词后的结果集，计算每个词出现的频率
    for text in texts:
        for word in text:
            frequency[word] += 1
    # 选择频率大于1的词(根据实际需求确定)
    texts = [[word for word in text if frequency[word] > 1] for text in texts]
    #for line in texts:
        #print(line)

    # 3.创建字典（单词与编号之间的映射）
    #print('3.创建字典（单词与编号之间的映射）')
    dictionary = corpora.Dictionary(texts)
    #print(dictionary)
    # 打印字典，key为单词，value为单词的编号
    #print(dictionary.token2id)

    # 4.将待比较的文档转换为向量（词袋表示方法）
    #print('4.将待比较的文档转换为向量（词袋表示方法）')
    # 使用doc2bow方法对每个不同单词的词频进行了统计，并将单词转换为其编号，然后以稀疏向量的形式返回结果
    new_vec = dictionary.doc2bow(new_text)
    #print(new_vec)

    # 5.建立语料库
    #print('5.建立语料库')
    # 将每一篇文档转换为向量
    corpus = [dictionary.doc2bow(text) for text in texts]
    #print(corpus)

    # 6.初始化模型
    #print('6.初始化模型')
    lsi = models.LsiModel(corpus)
    corpus_lsi = lsi[corpus]
    #for doc in corpus_lsi:
        #print(doc)

    # 7.创建索引
    #print('7.创建索引')
    index = similarities.MatrixSimilarity(corpus_lsi)

    # 8.相似度计算并返回相似度最大的文本
    #print('# 8.相似度计算并返回相似度最大的文本')
    new_vec_lsi = lsi[new_vec]
    #print(new_vec_lsi)
    # 计算要比较的文档与语料库中每篇文档的相似度
    sims = index[new_vec_lsi]
    #print(sims)
    sims_list = sims.tolist()

    #print("最相似的文本为：", documents[sims_list.index(max(sims_list))])  # 返回相似度最大的文本\
    if max(sims_list) >= 0.85:
        return documents[sims_list.index(max(sims_list))]
    else:
        return 0


#if __name__ == "__main__":
    #pass
