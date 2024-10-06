# https://codeforces.com/problemset/problem/1028/B -  Unnatural Conditions

import itertools as it

n, m = list(map(int, input().split()))
combs = {}
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for x in it.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], i):
        combs.setdefault(sum(x), set()).add(x)
cnt = 0
print(combs)
for i in combs[n]:
    print(i)
    if len(i) > 0:
        print("".join([str(k) for k in i]))
        cnt += 1
    if cnt > 1:
        break
