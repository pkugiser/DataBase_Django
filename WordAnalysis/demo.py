# coding: utf-8

import jieba


lt = jieba.cut("我是中国人，你是吗？", cut_all=False)

print(" ".join(lt))