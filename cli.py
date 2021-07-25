import requests
import sys
import codecs

data = requests.get("https://trie-system-atiksh.herokuapp.com/add/word/")

for d in data:
	print(d)
data.close()