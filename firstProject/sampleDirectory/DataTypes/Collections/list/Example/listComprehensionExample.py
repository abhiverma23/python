# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 15th Dec, 2016
# Title  : List Comprehension Example
# Description : Collecting words and converting it into capital with lower and its length.
# Tested On   : python 3.5.0

line = 'The quick brown fox jumps over the lazy ladki'
words = line.split(" ")
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)
