def merge(n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    last_n1 = n1 % 10
    last_n2 = n2 % 10
    if last_n1 < last_n2:
        return merge(n1 // 10, n2) * 10 + last_n1
    else:
        return merge(n1, n2 // 10) * 10 + last_n2

assert merge(31, 42) == 4321
assert merge(21, 0) == 21
assert merge(21, 31) == 3211

def make_func_repeater(f, x):
    def repeat(n):
        if n > 1:
            return f(repeat(n - 1))
        else:
            return f(x)
    return repeat

incr_1 = make_func_repeater(lambda x: x + 1, 1)
assert incr_1(2) == 3
assert incr_1(5) == 6

def is_prime(n):
    """Implement the recursive is_prime function. 
    Do not use a while loop, use recursion. 
    As a reminder, an integer is considered prime 
    if it has exactly two unique factors: 1 and itself.
    """
    if n == 1:
        return False
    return prime_helper(n, 2)
    


def prime_helper(n, k):
    if n == k:
        return True
    elif n % k != 0:
        return prime_helper(n, k + 1)
    else:
        return False
    return False

assert is_prime(7) == True
assert is_prime(10) == False
assert is_prime(1) == False