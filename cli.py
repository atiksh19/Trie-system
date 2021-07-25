import requests
import sys
from mysql.connector import connect, Error

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

cur.execute("UPDATE data SET trie = %s, keywords = %s", [str({'a': {'p': {'p': {'.': '.', 'l': {'e': {'.': '.'}}}}, 'n': {'y': {'t': {'h': {'i': {'n': {'g': {'.': '.'}}}}}}}}, 'd': {'e': {'v': {'e': {'l': {'o': {'p': {'e': {'r': {'.': '.'}}}}}}}}}}), str(['app', 'apple', 'anything', 'developer'])])
connection.commit()
"""data = requests.get("https://trie-system-atiksh.herokuapp.com/show")
for d in data:
	print(d)
data.close()"""