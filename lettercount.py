#!/usr/bin/env python

"""Write a program that reads in a string on the command line and returns a table of
the letters of the alphabet in alphabetical order which occur in the string together
with the number of times each letter occurs. Case should be ignored."""

import sys
args = sys.argv[1:]

letter_counts = {}
word = args[0]
for letter in word:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
letter_counts.keys().sort()
for letter in letter_counts:
    print letter,':', letter_counts[letter]