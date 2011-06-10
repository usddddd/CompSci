def only_evens(numbers):
    """
    >>> only_evens([1, 3, 4, 5, 6, 7, 8])
    [4, 6, 8]
    >>> only_evens([2, 4, 6, 8, 10, 11, 0])
    [2, 4, 6, 8, 10, 0]
    >>> only_evens([1, 3, 5, 7, 9, 11])
    []
    >>> only_evens([4, 0, -1, 2, 6, 7, -4])
    [4, 0, 2, 6, -4]
    >>> nums = [1, 2, 3, 4]
    >>> only_evens(nums)
    [2, 4]
    >>> nums
    [1, 2, 3, 4]
    """
    new_list = []
    for i in range(len(numbers)):
        if numbers[i]%2 == 0:
            new_list += [numbers[i]]
    return new_list


def only_odds(numbers):
    """
    >>> only_odds([1, 3, 4, 6, 7, 8])
    [1, 3, 7]
    >>> only_odds([2, 4, 6, 8, 10, 11, 0])
    [11]
    >>> only_odds([1, 3, 5, 7, 9, 11])
    [1, 3, 5, 7, 9, 11]
    >>> only_odds([4, 0, -1, 2, 6, 7, -4])
    [-1, 7]
    >>> nums = [1, 2, 3, 4]
    >>> only_odds(nums)
    [1, 3]
    >>> nums
    [1, 2, 3, 4]
    """
    new_list = []
    for i in range(len(numbers)):
        if numbers[i]%2 != 0:
            new_list += [numbers[i]]
    return new_list


def multiples_of(num, numlist):
    """
    >>> multiples_of(3, [1,4,6,9,13])
    [6, 9]
    >>> multiples_of(2, [1, 2, 4, 5, 6, 7, 8, 9, 10])
    [2, 4, 6, 8, 10]
    >>> nums = [10, 20, 30, 40, 50, 51]
    >>> multiples_of(10, nums)
    [10, 20, 30, 40, 50]
    >>> nums
    [10, 20, 30, 40, 50, 51]
    """
    new_list = []
    for i in range(len(numlist)):
        if numlist[i] % num == 0:
            new_list += [numlist[i]]
    return new_list


def replace(s, old, new):
    """
    >>> replace('Mississippi', 'i', 'I')
    'MIssIssIppI'
    >>> s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
    >>> replace(s, 'om', 'am')
    'I love spam! Spam is my favorite food. Spam, spam, spam, yum!'
    >>> replace(s, 'o', 'a')
    'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!'
    >>> s = 'My name is Adam and I am the goddamn man!'
    >>> replace(s,'dam', 'tommmm')
    'My name is Atommmm and I am the godtommmmn man!'
    """
    import string
    j = 0
    new_list = []
    while j < (len(s)):
        if s[j:(j + len(old))] == old:
            new_list += [new]
            j += len(old)
        else:
            new_list += s[j]
            j += 1    
                
    new_list = string.join(new_list, '')
    return new_list
        
            





if __name__ == '__main__':
    import doctest
    doctest.testmod()
