#!/usr/bin/env python


def encapsulate(val, seq):
    """
    >>> encapsulate('2', [])
    ['2']
    >>> encapsulate(2, ' ')
    '2'
    >>> encapsulate(2, (4,))
    (2,)
    """
    
    if type(seq) == type(""):
        return str(val)
    if type(seq) == type([]):
        return [val]
    return (val,)

def insert_in_middle(val, seq):
    """
    >>> insert_in_middle(5, [1, 2, 4, 5])
    [1, 2, 5, 4, 5]
    >>> insert_in_middle('a', 'abcd')
    'abacd'
    >>> insert_in_middle('a', ('b', 'c', 'd', 'e'))
    ('b', 'c', 'a', 'd', 'e')
    """
    middle = len(seq)/2
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]



def make_empty(seq):
    """
      >>> make_empty([1, 2, 3, 4])
      []
      >>> make_empty(('a', 'b', 'c'))
      ()
      >>> make_empty("No, not me!")
      ''
    """
    tup = ('',)
    lst = ['']
    st = ''
    
    if type(seq) == type(""):
        return ""
    elif type(seq) == type([]):
        return []
    return ()
    

def insert_at_end(val, seq):
    """
      >>> insert_at_end(5, [1, 3, 4, 6])
      [1, 3, 4, 6, 5]
      >>> insert_at_end('x', 'abc')
      'abcx'
      >>> insert_at_end(5, (1, 3, 4, 6))
      (1, 3, 4, 6, 5)
    """
    seq = seq[:] + encapsulate(val, seq)
    return seq
    

def insert_in_front(val, seq):
    """
      >>> insert_in_front(5, [1, 3, 4, 6])
      [5, 1, 3, 4, 6]
      >>> insert_in_front(5, (1, 3, 4, 6))
      (5, 1, 3, 4, 6)
      >>> insert_in_front('x', 'abc')
      'xabc'
    """
    seq = encapsulate(val, seq) + seq[:]
    return seq

def index_of(val, seq, start=0):
    """
      >>> index_of(9, [1, 7, 11, 9, 10])
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
      6
      >>> index_of('y', 'happy birthday')
      4
      >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
      1
      >>> index_of(5, [2, 3, 4])
      -1
      >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
      -1
    """
    i = start
    while i < len(seq):
        if seq[i] == val:
            return i
        i += 1
    else:
        return -1

def remove_at(index, seq):
    """
      >>> remove_at(3, [1, 7, 11, 9, 10])
      [1, 7, 11, 10]
      >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
      (1, 4, 6, 7, 0, 3, 5)
      >>> remove_at(2, "Yomrktown")
      'Yorktown'
    """
    seq = seq[:index] + seq[index + 1:]
    return seq

def remove_val(val, seq):
    """
      >>> remove_val(11, [1, 7, 11, 9, 10])
      [1, 7, 9, 10]
      >>> remove_val(15, (1, 15, 11, 4, 9))
      (1, 11, 4, 9)
      >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
      ('who', 'when', 'where', 'why', 'how')
    """
    i = 0
    while i < (len(seq)):
        if seq[i] == val:
            seq = remove_at(i, seq)
        i += 1
    return seq


def remove_all(val, seq):
    """
      >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
      [1, 7, 9, 10, 2]
      >>> remove_all('i', 'Mississippi')
      'Msssspp'
    """
    while val in seq:
        seq = remove_at(index_of(val, seq), seq)
    return seq
        
        
def count(val, seq):
    """
      >>> count(5, (1, 5, 3, 7, 5, 8, 5))
      3
      >>> count('s', 'Mississippi')
      4
      >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
      2
    """
    count = 0
    for i in range(len(seq)):
        if seq[i] == val:
            count += 1
    return count


def reverse(seq):
    """
      >>> reverse([1, 2, 3, 4, 5])
      [5, 4, 3, 2, 1]
      >>> reverse(('shoe', 'my', 'buckle', 2, 1))
      (1, 2, 'buckle', 'my', 'shoe')
      >>> reverse('Python')
      'nohtyP'
    """
   
    new = make_empty(seq)
    for i in range(len(seq) - 1, -1, -1):
        new = new[:] + encapsulate(seq[i], seq)
    return new

def sort_sequence(seq):
    """
      >>> sort_sequence([3, 4, 6, 7, 8, 2])
      [2, 3, 4, 6, 7, 8]
      >>> sort_sequence((3, 4, 6, 7, 8, 2))
      (2, 3, 4, 6, 7, 8)
      >>> sort_sequence("nothappy")
      'ahnoppty'
    """
    
    new = make_empty(seq)
    if type(seq) == type([]):
        seq.sort()
        return seq
    elif type(seq) == type(''):
        seq = list(seq)
        seq.sort()
        return "".join(seq)
    else:
        seq = list(seq)
        seq.sort()
        return tuple(seq)
            
        
    
    

    
   
           
if __name__ == "__main__":
    import doctest
    doctest.testmod()
