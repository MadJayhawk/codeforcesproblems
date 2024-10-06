# https://codeforces.com/contest/1187/problem/0 -  Stickers and Toys
# Start:    Finish:     Duration:    Attempts: 8    Difficulty: 900
# Note, that there are exactly n−t eggs with only a sticker and, analogically, exactly n−s with only a toy. So we need to buy more than max(n−t,n−s) eggs, or exactly max(n−t,n−s)+1.
def stickers_and_toys(n, st, toy):
    if n == st == toy:
        a = 1
    if st + toy == n:
        a = max(st, toy) + 1
    else:
        a = max(st, toy) + n - (st + toy) + 1
    return a


# --------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        n,s,t = list(map(int, input().split()))
        print(stickers_and_toys(n,s,t))


# 8
# 3 1 2
# 3 1 3
# 3 2 1
# 3 2 2
# 3 2 3
# 3 3 1
# 3 3 2
# 3 3 3
#
# 4
# 1 1 1
# 1000000000 1000000000 1000000000
# 1000000000 999999999 1
# 999999999 666666667 6666666661
# 20
# 12 1 11
# 12 1 12
# 12 2 10
# 12 2 11
# 12 2 12
# 12 3 9
# 12 3 10
# 12 3 11
# 12 3 12
# 12 4 8
# 12 4 9
# 12 4 10
# 12 4 11
# 12 4 12
# 12 5 7
# 12 5 8
# 12 5 9
# 12 5 10
# 12 5 11
# 12 5 12
