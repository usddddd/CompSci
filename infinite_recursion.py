#!/usr/bin/env python

#
#infinite_recursion.py
#

def recursion_depth(number):
    print "Recursion depth %d." % number
    try:
        recursion_depth(number + 1)
    except:
        print "Maximum recursion depth exceeded."
    
recursion_depth(0)