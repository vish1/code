''' Goal: Create a shallow, crummy, over-priced, under-supported
    algebra package to be sold to unsuspecting school systems.
'''

import math

def quadratic(a, b, c):
    ''' Return the two roots of: ax^2 + bx + c = 0

    >>> quadratic(a=8, b=22, c=15)
    (-1.25, -1.5)
    >>> x = -1.25
    >>> 8*x**2 + 22*x + 15
    0.0
    >>> x = -1.5
    >>> 8*x**2 + 22*x + 15
    0.0
    >>>
    
    '''

    discriminant = math.sqrt(b**2.0 - 4.0 * a * c)
    x0 = (-b + discriminant) / (2.0 * a)
    x1 = (-b - discriminant) / (2.0 * a)
    return x0, x1

if __name__ == '__main__':
    import doctest
    print doctest.testmod()
