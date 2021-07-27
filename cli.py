import sys
import requests
"""[2:-1]"""

if len(sys.argv) != 3:
	print("more or less arguments than required!")
	exit()

#gathering arguments
action = sys.argv[1:2][0]
key = sys.argv[2:3][0]

key = key.lower()

if not key.isalpha():
	print("not a valid format!")
	exit()

#returns the trie or wordlist from the database
#num should be 0 for trie and 1 for words list
def get(num):
	st = ""
	result = requests.get("https://trie-system-atiksh.herokuapp.com/show")
	for r in result:
		st += str(r)[2:-1]
	return st.split("<br/>")[num]

def add(data):
	st = ""
	result = requests.get("https://trie-system-atiksh.herokuapp.com/add/" + data)
	for r in result:
		st += str(r)
	return st[2:-1]
def find(data):
	st = ""
	result = requests.get("https://trie-system-atiksh.herokuapp.com/find/" + data)
	for r in result:
		st += str(r)
	return st[2:-1]
def prefix(data):
	st = ""
	result = requests.get("https://trie-system-atiksh.herokuapp.com/prefix/" + data)
	for r in result:
		st += str(r)
	return st[2:-1]

if action == '-a':
	print("are you sure you want to add the word \'" + key + "\'?(y/n)")
	confirm = input()
	if confirm == 'y':
		print(add(key))
	elif confirm == 'n':
		print("run the script again!")
		exit()

elif action == '-f':
	print(find(key))
elif action == '-p':
	print(prefix(key))
elif action == '-s':
	if key == "trie":
		print('\n' + get(0))
	elif key == "words":
		print('\n' + get(1))
	else:
		print(key + " is not a valid request")