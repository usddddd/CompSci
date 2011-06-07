#!/usr/bin/env python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)
        
if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    
    print factorial(int(args[0]))