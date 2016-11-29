# -*- coding: utf-8 -*-
from pyltp import Postagger
postagger = Postagger() # 初始化实例
postagger.load('/path/to/your/model')  # 加载模型
postags = postagger.postag(words)  # 词性标注
print '\t'.join(postags)
postagger.release()  # 释放模型