#!/usr/bin/env python

import sys

args = sys.argv[1:]


def mean(args):
    """
    Return mean of all numbers entered on commandline
    """
    nums = []

    for i in args:
        nums.append(float(i))
    mean = (sum(nums))/len(args)
    
    print mean

if __name__ == '__main__':
    mean(args)
