#importing stuff
import ast
from flask import Flask
from psycopg2 import connect, Error

######################################
#trie class using python dictionaries instead of objects
class Trie:
	#each node is a dictionary item with its own dictionary values
	#each dictionary contains its own children as other dictionaries
	#the end of a word is represented by a '.' in its children
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

myData = ''
myKeywords = ''

#connecting to the database
try:
	connection = connect(
		host="chunee.db.elephantsql.com",
		user="cdkclnkt",
		password="dbv0ntLPe71E-JEyvdoXNkzZpgk3GJrr",
		database="cdkclnkt"
	)
	cur = connection.cursor()
except Error as e:
	print(e)
# adding refresh functionality to call before and after every execution
def refresh():
	global myData, myKeywords
	cur.execute("SELECT trie FROM data")
	myData = cur.fetchone()[0]
	cur.execute("SELECT keywords FROM data")
	myKeywords = cur.fetchone()[0]

##############################
#converting to usable flask app
app = Flask(__name__)

@app.route('/')
#we don't need this path in our project
def noVal():
	return "Not a valid function"
#the below shows some interaction with the database
#we get the trie to change our data for us
#then we rewrite the whole data after being processed
#this is very risky so I have added multiple validations
@app.route('/add/<string:data>')
def addWord(data):
	if str(data).isalpha():
		refresh()
		myTrie = Trie(ast.literal_eval(myData), ast.literal_eval(myKeywords))
		myTrie.add_word(data)
		cur.execute("UPDATE data SET trie = %s, keywords = %s", [str(myTrie.root), str(myTrie.wordslist)])
		connection.commit()
		refresh()
		return "done!!"
	else:
		return "not a valid format"

@app.route('/rem/<string:data>')
def remWord(data):
	if str(data).isalpha():
		refresh()
		keywords = ast.literal_eval(myKeywords)
		if str(data) not in keywords:
			return "word not found"
		keywords.remove(str(data))
		myTrie = Trie({}, keywords)
		for kw in keywords:
			myTrie.add_word(kw)
		cur.execute("UPDATE data SET trie = %s, keywords = %s", [str(myTrie.root), str(myTrie.wordslist)])
		connection.commit()
		refresh()
		return "done!!"
	else:
		return "not a valid format"

@app.route('/find/<string:data>')
def findWord(data):
	if str(data).isalpha():
		refresh()
		myTrie = Trie(ast.literal_eval(myData), ast.literal_eval(myKeywords))
		if myTrie.find_word(data):
			return "word found"
		else:
			return "word not found"
		refresh()
	else:
		return "not a valid format"

@app.route('/prefix/<string:data>')
def prefixOfWord(data):
	if str(data).isalpha():
		refresh()
		myTrie = Trie(ast.literal_eval(myData), ast.literal_eval(myKeywords))
		return str(myTrie.prefix_of(data))
		refresh()

@app.route('/show')
def showData():
	refresh()
	cur.execute("SELECT trie FROM data")
	tr = cur.fetchone()[0]
	cur.execute("SELECT keywords FROM data")
	kw = cur.fetchone()[0]
	return str(tr) + "<br/>" + str(kw)
	refresh()

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0')

##############################
