# -*- coding: utf-8 -*-
import MeCab

# 辞書ファイルパス
DIC_PATH = ' -d /usr/local/mecab/lib/mecab/dic/mecab-ipadic-neologd'

if __name__ == '__main__':
  sample_text = 'すもももももももものうち'
  print(MeCab.Tagger(DIC_PATH).parse(sample_text))
