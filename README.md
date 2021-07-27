# Trie-system
This repository is made for the Slingshot take home challenge
# About
A lot of the code I wrote has been explained using comments. I used python dictionaries instead of making them objects, as that was much easier to store in a database. Each node is just a dictionary object with a value of other dictionary objects, which are its children nodes. It has multiple validations for security as it has to rewrite the data everytime so the processing may take a few seconds(anywhere from less than a second to about 12), depending on your internet speed, before it completes. The CLI connects to a flask app I made that does the main interaction with the database. This was a much faster and safer option. adding the interaction to the cli itself would make the application too bulky. To use the trie system you just need to download the file named cli.py.
# How I made it
I have my exams going on and they will go on until 7 August, so I got very little time to work on this. I originally used mySQL database but I had to later switch to postgreSQL. I am surprised I managed to get it to work but I couldn't add too much funcionality to it. I made a very simple CLI for it, the instructions for which are given below
# How to use
I deployed the product as a flask app so you can access that but I did not make that interactive so I made a CLI for it. It is very easy to use and can be run from the command line like any other python script. You can download it from this repository, it is named cli.py. to run it the commands are very easy:
1. ***Add a word to the trie:*** python cli.py -a (keyword)
2. ***Show the trie:*** python cli.py -s trie
3. ***Show a list of all the words in the trie:*** python cli.py -s words
4. ***Find a word in the trie:*** python cli.py -f (keyword)
5. ***Find all words with a given prefix:*** python cli.py -p (prefix)
