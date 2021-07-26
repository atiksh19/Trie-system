import requests
import sys
import codecs
from mysql.connector import connect, Error
"""
data = requests.get("https://trie-system-atiksh.herokuapp.com/show")

for d in data:
	print(d)
data.close()
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
tr = cur.fetchone()[0]
cur.execute("SELECT keywords FROM data")
kw = cur.fetchone()[0]
print(tr, kw)