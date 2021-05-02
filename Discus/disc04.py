def count_stair_ways(n):
    if n == 1 or n == 0:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n, k):
    if n == 1 or n == 0:
        return 1
    elif k == 1:
        return 1
    else:
        return count_n(n, k)

def count_n(n, k, cnt=0):
    if cnt == k or cnt == n:
        return 0
    else:
        return count_k(n-cnt-1, k) + count_n(n, k, cnt+1)
     
# assert count_k(3, 3) == 4

def even_weighted(s):
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]

assert even_weighted([1, 2, 3, 4, 5, 6]) == [0, 6, 20]

def max_product(s):
    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))

assert max_product([10, 3, 1, 9, 2]) == 90
assert max_product([5, 10, 5, 10, 5]) == 125
assert max_product([]) == 1