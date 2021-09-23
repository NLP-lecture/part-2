import os
import jieba.analyse
from tf_idf import read_file 
 
text=u"线程是程序执行时的最小单位，它是进程的一个执行流，\
    是CPU调度和分派的基本单位，一个进程可以由很多个线程组成，\
    线程间共享进程的所有资源，每个线程有自己的堆栈和局部变量。\
    线程由CPU独立调度执行，在多CPU环境下就允许多个线程同时运行。\
    同样多线程也可以实现并发操作，每个请求分配一个线程来处理。"

'''
# 获取当前目录
path_now = os.getcwd()
# 返回上一级并进入到翻译数据的目录中
path_data = os.path.abspath(os.path.join(path_now, '../translation_data/old_data'))

# 以一个句子为一个文档, 得到中文验证集文档列表(句子列表)
list_document = read_file(os.path.join(path_data, 'dev.zh'))

text = ''.join(list_document)
'''

keywords=jieba.analyse.extract_tags(text, topK=15, withWeight=False, allowPOS=())
print(keywords)
