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

cur.execute("UPDATE data SET trie = %s, keywords = %s", ['{}', '[]'])