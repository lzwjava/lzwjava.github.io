import MeCab

t = MeCab.Tagger("-r /opt/homebrew/etc/mecabrc")
sentence = "太郎はこの本を女性に渡した。"
print(t.parse(sentence))