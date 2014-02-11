#Write a program, lettercount.py, that opens a file named on the 
#command line and counts how many times each letter occurs 
#in that file. Your program 
#should then print those counts to the screen, in alphabetical order

#get filename from command line
from sys import argv
script, filename = argv

#open file
f = open(filename, "r")
#read file
myfile = f.read()
#close file
f.close()
#separate into letters
#there are 26 letters in alphabet
alphabet = [0] * 26
#letters = "lsdkjflskdjfLFKJGDLFKJieurvmls"
letters = myfile.lower()
letters = letters.strip()
#print letters
#count letter occurances
for letter in letters:
    index = ord(letter) - 97 #list starts at a. 97 is value of a.
    if index > 25:
        del index
    elif index < 0:
        del index
    else:
        alphabet[index] += 1
#print counts in alphabetical order
for i in range(len(alphabet)):
    print chr(i + 97) + str(alphabet[i])