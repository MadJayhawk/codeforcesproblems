# https://codeforces.com/problemset/problem/50/A -  Domino Piling
# Start: 11:00    Finish:  xx   Duration: xx   Attempts: 3     Difficulty:  800
n, m = list(map(int, input().split()))
r = 0
if n == 1 or m == 1:
    print((n * m) // 2)
else:
    if n % 2 != 0:
        n -= 1
        r = m // 2
    else:
        if m % 2 != 0:
            m -= 1
            r = n // 2
    print((n * m) // 2 + r)
#
# c = min(m, n)
# d = max(m, n)
# if m%2 == 0 or n%2 == 0:
#     ans = (m*n)//2
# else:
#     if d % 2 != 0:
#         d -= 1
#     else:
#         c -= 1
#     if c == 1 or d == 1:
#         ans = (c*d)//2
#     else:
#         ans = (c*d)//2+d//2
# print(ans)
