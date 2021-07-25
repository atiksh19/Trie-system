import ast
from flask import Flask
from mysql.connector import connect, Error

######################################

class Trie:
	def __init__(self, root, wordslist):
		self.root = root
		self.wordslist = wordslist
	def add_word(self, keyword):
		node = self.root
		for char in keyword:
			if not char in node:
				node[char] = {}
			node = node[char]
		node["."] = "."
		if keyword not in self.wordslist:
			self.wordslist.append(keyword)
	def find_word(self, word):
		node = self.root
		for char in word:
			if char in node:
				node = node[char]
			else:
				return False
		return "." in node
	def prefix_of(self, prefix):
		wordsFound = []
		node = self.root
		words = self.wordslist
		for word in words:
			if word.startswith(prefix):
				wordsFound.append(word)
		return wordsFound

######################################

"""
Username: kzEaB8dSjz

Database name: kzEaB8dSjz

Password: 5xZWr3JUQr

Server: remotemysql.com

Port: 3306
"""

try:
	connection = connect(
		host="remotemysql.com",
		user="kzEaB8dSjz",
		password="5xZWr3JUQr",
		database="kzEaB8dSjz"
	)
	cur = connection.cursor()
except Error as e:
	print(e)

cur.execute("SELECT trie FROM data")
myData = cur.fetchone()[0]
cur.execute("SELECT keywords FROM data")
myKeywords = cur.fetchone()[0]

##############################

app = Flask(__name__)

@app.route('/')
def noVal():
	return "Not a valid function"

@app.route('/add/<string:data>')
def addWord(data):
	if str(data).isalpha():
		myTrie = Trie(ast.literal_eval(myData), ast.literal_eval(myKeywords))
		myTrie.add_word(data)
		cur.execute("UPDATE data SET trie = %s, keywords = %s", [str(myTrie.root), str(myTrie.wordslist)])
		connection.commit()
		return "done!!"
	else:
		return "not a valid format"

@app.route('/find/<string:data>')
def findWord(data):
	if str(data).isalpha():
		myTrie = Trie(ast.literal_eval(myData), ast.literal_eval(myKeywords))
		if myTrie.find_word(data):
			return "word found"
		else:
			return "word not found"
	else:
		return "not a valid format"

@app.route('/prefix/<string:data>')
def prefixOfWord(data):
	if str(data).isalpha():
		myTrie = Trie(ast.literal_eval(myData), ast.literal_eval(myKeywords))
		return str(myTrie.prefix_of(data))

@app.route('/show')
def showData():
	cur.execute("SELECT trie FROM data")
	tr = cur.fetchone()[0]
	cur.execute("SELECT keywords FROM data")
	kw = cur.fetchone()[0]
	return str(tr) + "<br/>" + str(kw)


if __name__ == "__main__":
	app.run(debug=True)

##############################