# Question 1.1
class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return self.x
    def __str__(self):
        return self.x * 2

class B:
    def __init__(self):
        print("boo!")
        self.a = []
    def add_a(self, a):
        self.a.append(a)
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret

"""
>>> A("one")
one
>>> print(A("one"))
oneone
>>> repr(A("two"))
'two'
>>> b = B()
boo!
>>> b.add_a(A("a"))
>>> b.add_a(A("b"))
>>> b
2
aabb
"""

# Implementation Link
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    def __len__(self):
        if self is Link.empty:
            return 0
        else:
            return 1 + self.rest.__len__()

    def __getitem__(self, i):
        if i == 0 or self is Link.empty:
            return self
        else:
            return Link.__getitem__(self.rest, i - 1)

# Question 2.1
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk is not Link.empty:
        return lnk.first + sum_nums(lnk.rest)
    else:
        return 0

# Question 2.2
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    n = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        n *= lnk.first
    return Link(n, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))


# Question 2.3
def flip_two(lnk):
    """Write a recursive function flip two that takes as input a linked 
    list lnk and mutates lnk so that every pair is flipped.

    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if len(lnk) > 1:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        flip_two(lnk[2])
    else:
        pass

# Question 2.4
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    # with while loop version
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

    # without while loop version
    # if link is not Link.empty:
    #     if f(link.first):
    #         yield link.first
    #     yield from filter_link(link.rest, f)

# Tree
class Tree:
    def __init__(self, label, branches=[]):
        """
        >>> t = Tree(3, [Tree(4), Tree(5)])
        >>> t.label = 5
        >>> t.label
        5
        """
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)


# Question 3.1
def make_even(t):
    """Define a function make even which takes in a tree t 
    whose values are integers, and mutates the tree such that 
    all the odd integers are increased by 1 and all the 
    even integers remain the same.

    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    def is_odd(n):
        return n % 2 == 1

    def is_even(n):
        return n % 2 == 0

    if is_odd(t.label):
        t.label += 1
    if not t.is_leaf():
        for b in t.branches:
            make_even(b)

# Question 3.2
def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    t.label *= t.label
    if not t.is_leaf():
        for b in t.branches:
            square_tree(b)

# Question 3.3
def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.is_leaf():
        return [[t.label]] if t.label == entry else []
    for b in t.branches:
        if entry in b:
            paths += [[t.label] + el for el in find_paths(b, entry)]
    return paths

# Question 3.4
def combine_tree(t1, t2, combiner):
    """Write a function that combines the values of two trees t1 and t2 together
    with the combiner function. Assume that t1 and t2 have identical structure.
    This function should return a new tree.

    >>> from operator import mul
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    >>> a = Tree(1, [Tree(2), Tree(3)])
    >>> b = Tree(4, [Tree(5), Tree(6)])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    return Tree(combiner(t1.label, t2.label), [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)])

# Question 3.5
def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    t.label = map_fn(t.label)
    if t.is_leaf():
        pass
    else:
        for b in t.branches:
            for bb in b.branches:
                alt_tree_map(bb, map_fn)
    return t