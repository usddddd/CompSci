#!/usr/bin/env python

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    print fibonacci(int(args[0]))