"""
>>> import string
>>> string.split(message, '??')
['this', 'and', 'that']
"""

message = 'this??and??that'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
