# https://codeforces.com/problemset/problem/82/A -  Double Cola
# Start:    Finish:     Duration:    Attempts:     Difficulty: 
# import logging
# logging.basicConfig(format='%(message)s')
# logging.error(f'n: {n}')
from math import ceil


def double_cola(n):
    big_bang = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
    i = 0
    j = 1
    k = len(big_bang)
    
    while i <= n:
        i += k
        k += k
        j += j
    return big_bang[int(ceil((n - (i - k * 0.5)) / (j * 0.5)) - 1)]


# --------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    print(double_cola(n))

    n = 1
    print(double_cola(n))
    n = 6
    print(double_cola(n))
    n = 1802
    print(double_cola(n))