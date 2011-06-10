def is_divisible_by_2_or_5(n):
    """
    >>> is_divisible_by_2_or_5(8)
    True
    >>> is_divisible_by_2_or_5(7)
    False
    >>> is_divisible_by_2_or_5(5)
    True
    >>> is_divisible_by_2_or_5(9)
    False
    """

    return  n % 2 == 0 or n % 5 == 0


def compare(a,b):
    """
    >>> compare(5, 4)
    1
    >>> compare(7, 7)
    0
     
    >>> compare(2, 3)
    -1
    >>> compare(42, 1)
    1
    """
    
    
    if a > b:
        return 1
    if b > a:
        return -1
    else: 
        return 0


def hypotenuse(a,b):
    """
    >>> hypotenuse(3, 4)
    5.0
    >>> hypotenuse(12, 5)
    13.0
    >>> hypotenuse(7, 24)
    25.0
    >>> hypotenuse(9, 12)
    15.0
    """
    c = (a**2 + b**2)**0.5
    return c


def slope(x1,y1,x2,y2):
    """
    >>> slope(5,3,4,2)
    1.0
    >>> slope(1,2,3,2)
    0.0
    >>> slope(1,2,3,3)
    0.5
    >>> slope(2,4,1,2)
    2.0
    """
    dx = x2 - x1
    dy = y2 - y1
    return float(dy)/dx


def intercept(x1,y1,x2,y2):
    """
    >>> intercept(1,6,3,12)
    3.0
    >>> intercept(6,1,1,6)
    7.0
    >>> intercept(4,6,12,8)
    5.0
    """
    yint = y1 - (slope(x1,y1,x2,y2)*x1)
    return yint


if __name__ == '__main__':
    import doctest
    doctest.testmod()
