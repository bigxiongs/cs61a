def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

def add_this_many(x, el, s):
    """Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    for _ in range(s.count(x)):
        s.append(el)
    return

def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0 
    >>> list(filter(range(5), is_even)) #a list of the values yielded from the call to filter 
    [0, 2, 4]
    >>> all_odd = (2 * y - 1 for y in range(5)) 
    >>> list(filter(all_odd, is_even)) 
    []
    >>> naturals = (n for n in range(1,100)) 
    >>> s = filter(naturals, is_even) 
    >>> next(s) 
    2
    >>> next(s) 
    4
    """
    for el in iterable:
        if fn(el):
            yield el

def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3)
    >>> b = sequence(3, 2)
    >>> result = merge(a, b)
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    x = next(a)
    y = next(b)
    while True:
        if x == y:
            yield x
            x = next(a)
            y = next(b)
        elif x < y:
            yield x
            x = next(a)
        else:
            yield y
            y = next(b)




