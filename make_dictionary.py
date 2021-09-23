import os
from collections import defaultdict
from operator import itemgetter

def make_dictionary(_file): 
    _dict = defaultdict(int)
    for line in _file:
        for word in line.strip().split():
            _dict[word] += 1

    return _dict

if __name__ == "__main__":
    # 获取当前目录
    path_now = os.getcwd()
    # 返回上一级并进入到翻译数据的目录中
    path_data = os.path.abspath(os.path.join(path_now, '../translation_data'))
    
    # 用训练集中的数据建立中文和英文词表
    f_zh = open(os.path.join(path_data, 'train.zh'), 'r', encoding='utf-8')
    dict_zh = make_dictionary(f_zh)
    
    f_en = open(os.path.join(path_data, 'train.en'), 'r', encoding='utf-8')
    dict_en = make_dictionary(f_en)

    # 按值对字典进行降序排序
    list_dict_zh = sorted(dict_zh.items(), key=itemgetter(1), reverse=True)
    list_dict_en = sorted(dict_en.items(), key=itemgetter(1), reverse=True)
    
    # 将字典写入文件
    out_zh = open('dict.zh.txt', 'w', encoding='utf-8')
    out_en = open('dict.en.txt', 'w', encoding='utf-8')
    
    for word, frequence in list_dict_zh:
        out_zh.write(word + ' ' + str(frequence) + '\n')
    
    for word, frequence in list_dict_en:
        out_en.write(word + ' ' + str(frequence) + '\n')
