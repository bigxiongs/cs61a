def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
    	return 1
    else:
    	res = 1
    	cnt = 0
    	while cnt < k:
    		res = res * (n - cnt)
    		cnt = cnt + 1
    	return res




def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    total = 0
    res = y
    while res >= 10:
        total = total + res % 10
        res = res // 10
    total = total + res
    return total



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    res = n
    cnt = 0
    while res > 0:
        if res % 10 == 8:
            cnt = cnt + 1
            if cnt == 2:
                return True
        else:
            cnt = 0
        res = res // 10
    return False


