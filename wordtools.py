def myreplace(old, new, s):
    """Replace all occurences of old with new in the string s.
    >>> myreplace(',', ';', 'this, that, and, some, other, thing')
    'this; that; and; some; other; thing'
    >>> myreplace(' ', '**', 'Words that will now be separated by stars.')
    'Words**that**will**now**be**separated**by**stars.'
    """
    return new.join(s.split(old))

def cleanword(word):
    """
    >>> cleanword('what?')
    'what'
    >>> cleanword('"now!"')
    'now'
    >>> cleanword('?+="word!,@$()"')
    'word'
    """
    for char in word:
        if ord(char) not in range(65,91) and ord(char) not in range(97, 123):
            word = "".join(word.split(char))
    return word


def has_dashdash(s):
    """ 
    >>> has_dashdash('distance--but')
    True
    >>> has_dashdash('several')
    False
    >>> has_dashdash('critters')
    False
    >>> has_dashdash('spoke--fancy')
    True
    >>> has_dashdash('yo-yo')
    False
    """
    return '--' in s


def extract_words(s):
    """
    >>> extract_words('Now is the time! "Now", is the time? Yes, now.')
    ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
    >>> extract_words('she tried to curtsy as she spoke--fancy')
    ['she', 'tried', 'to', 'curtsy', 'as', 'she', 'spoke', 'fancy']
    """
    new_list = s.split()    
    
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            if ord(new_list[i][j]) not in range(65,92) and ord(new_list[i][j]) not in range(97,123) and ord(new_list[i][j]) != 32:
                s = " ".join(s.split(new_list[i][j])).lower()
    return s.split()
    
def wordcount(word, wordlist):  
    """
      >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['now', 2]
      >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
      ['is', 4]
      >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['time', 1]
      >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['frog', 0]
    """
    count = 0
    for i in range(len(wordlist)):
        if wordlist[i] == word:
            count += 1
    return [word,count]
    
def wordset(wordlist):
    """
    >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['is', 'now', 'time']
    >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
    ['I', 'a', 'am', 'is']
    >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
    ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    words = []
     
    for i in range(len(wordlist)):
        if wordlist[i] not in words:
            words.append(wordlist[i])
    words.sort()
    return words
    

def longestword(wordset):
    """
      >>> longestword(['a', 'apple', 'pear', 'grape'])
      5
      >>> longestword(['a', 'am', 'I', 'be'])
      2
      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
      34
    """
    
    big = 0
    for i in range(len(wordset)):
        count = 0
        for j in range(len(wordset[i])):
            count += 1
        if count > big:
            big = count
    return big
            







if __name__ == '__main__':
    import doctest
    doctest.testmod()
