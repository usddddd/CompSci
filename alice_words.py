#!/usr/bin/env python
"""Program to compute number of times each word occurs in Alice in Wonderland"""
import wordtools

infile = open('alice_in_wonderland.txt', 'r')
outfile = open('alice_words.txt', 'w')
word_list = {}
text = infile.read().split()
for word in text:
    word = wordtools.cleanword(word).lower() 
    word_list[word] = word_list.get(word, 0) + 1

print("%-18s%s")%('Word', 'Count')
print("=======================")
most_frequent = 'a'
for word in sorted(word_list.keys()):
    print("%-18s%i")%(word, word_list[word])
    if word_list[word] > word_list[most_frequent]:
        most_frequent = word
    
infile.close()
outfile.close()

print "Most frequent word is %s, it appeared %i times" % (most_frequent, word_list[most_frequent])
print "The word 'alice' appeared %i times" % word_list['alice']



