import MeCab

t = MeCab.Tagger("-d /opt/homebrew/lib/mecab/dic/ipadic")
sentence = "太郎はこの本を女性に渡した。"
print(t.parse(sentence))