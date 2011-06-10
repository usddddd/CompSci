#!/usr/bin/env python
import sys
args = sys.argv[1:]


def median(args):
    """
    Return median of all numbers entered on commandline
    """
    total_nums = len(args)
    middle = total_nums/2 
    avg_middle = (int(args[middle]) + int(args[middle - 1]))/float(2)
    if total_nums % 2 == 0:
        print avg_middle
    else:
        print int(args[middle])

    
if __name__ == '__main__':
    median(args)
