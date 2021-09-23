import os
from collections import defaultdict
import math
import operator
 
def calculate_tf_idf(list_document):
    # 总词频统计
    dict_frequence = defaultdict(int)
    for document in list_document:
        list_word = document.split()
        for word in list_word:
            dict_frequence[word] += 1
 
    # 计算每个词的TF值
    tf = {}
    _sum = sum(dict_frequence.values())		# 单词总数
    for word in dict_frequence.keys():
        tf[word] = dict_frequence[word] / _sum		# 词频/总次数 
 
    # 计算每个词的IDF值
    doc_num = len(list_document)	# 统计文档数量
    idf = {}
    df = defaultdict(int)	# 每个单词出现在几个文档中
    
    for word in dict_frequence.keys():
        for doc in list_document:
            if word in doc:
                df[word] += 1
    
    for word in dict_frequence:
        idf[word] = math.log(doc_num / (df[word]+1))	# +1防止除0
 
    # 计算每个词的TF*IDF的值
    tf_idf = {}
    for word in dict_frequence:
        tf_idf[word] = tf[word] * idf[word]
 
    # 对字典按值由大到小排序
    result = sorted(tf_idf.items(), key=operator.itemgetter(1), reverse=True)
    return result

def read_file(filename):
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            result.append(line.strip())

    return result
 
if __name__=='__main__':
    # 获取当前目录
    path_now = os.getcwd()
    # 返回上一级并进入到翻译数据的目录中
    path_data = os.path.abspath(os.path.join(path_now, '../translation_data'))
    
    # 以一个句子为一个文档, 得到中文验证集文档列表(句子列表)
    list_document = read_file(os.path.join(path_data, 'dev.zh'))
    list_tf_idf = calculate_tf_idf(list_document)

    # 将得到的关键词和它的分数写入文件
    out = open('keywords.txt', 'w', encoding='utf-8')
    for keyword, score in list_tf_idf:
        out.write(keyword + ' ' + str(score) + '\n')

