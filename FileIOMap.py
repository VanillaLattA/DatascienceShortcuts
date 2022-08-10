import math
import numpy as np
import collections 

letter_count={'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 0, 'k': 0, 'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0, '1': 0, '0': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

#open the file 
openFile= open("sampletext.txt")
#read all the lines and not the text
allText= openFile.read()
#print line by line
for line in allText:
    line = line.lower()
    if line in letter_count:
        letter_count[line]+=1
openFile.close()
print(letter_count)

