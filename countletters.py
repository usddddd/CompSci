#!/usr/bin/env python
    
#
# countletters.py
#
import sys
args = sys.argv[1:]
    

def countletters(input_file=args[0], output_file=args[1] ):    
    """
    Delivers character count of text input file to output file of users choosing
    
    Usage: countletters.py input_file output_file
    """
        
    def display(i):
        if i == 10: return 'LF'
        if i == 13: return 'CR'
        if i == 32: return 'SPACE'
        return chr(i)
    
    infile = open(str(input_file), 'r')
    text = infile.read()
    infile.close()
    
    counts = 128 * [0]
    
    for letter in text:
        counts[ord(letter)] += 1
    
    outfile = open(str(output_file), 'w')
    outfile.write("%-12s%s\n" % ("Character", "Count"))
    outfile.write("=================\n")
    
    for i in range(len(counts)):
        if counts[i]:
            outfile.write("%-12s%d\n" % (display(i), counts[i]))
    
    outfile.close()
    
if __name__ == '__main__':
    
    if len(args) != 2:
        print "Usage: countletters.py input_file output_file"
    else:   
        countletters()