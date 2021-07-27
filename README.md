# Trie-system
This repository is made for the Slingshot take home challenge
# About
A lot of the code I wrote has been explained using comments. I used python dictionaries instead of making them objects, as that was much easier to store in a database. Each node is just a dictionary object with a value of other dictionary objects, which are its children nodes. I originally used mySQL database but I had to later switch to postgreSQL.
# How I made it
I have my exams going on and they will go on until 7 August, so I got very little time to work on this. I am surprised I managed to get it to work but I couldn't add too much funcionality to it. I made a very simple CLI for it, the instructions for which are given below
# How to use
I deployed the product as a flask app so you can access that but I did not make that interactive so I made a CLI for it. It is very easy to use and can be run from the command line like any other python script. You can download it from this repository, it is named cli.py. to run it the commands are very easy:
1. _Add a word to the trie:_ python cli.py -a <your word>
2. _Show the trie:_ python cli.py -s trie
3. _Show a list of all the words in the trie:_ python cli.py -s words
4. _Find a word in the trie:_ python cli.py -f <your word>
5. _Find all words with a given prefix:_ python cli.py -p <your word>
