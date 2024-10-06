#http://codeforces.com/problemset/problem/1007/A     Reorder the Array

from collections import Counter
n=int(input())
a =map(int, input().split())
b=Counter(a).values()
maxx=max(b)
print(n-maxx)
----------------------------------------------------------------------------------------------
By avalya7, contest: Codeforces Round #497 (Div. 1), problem: (A) Reorder the Array, Accepted, #
from collections import *
print(int(input()) - max(Counter(map(int,input().split())).values()))

----------------------------------------------------------------------------------------------
By LowNoon, contest: Codeforces Round #497 (Div. 1), problem: (A) Reorder the Array, Accepted, #
 n = int(input())
a = list(map(int, input().split(' ')))
a.sort()
d = 0
j = 0
m = 1
for i in range(1, len(a)):
    if a[i] == a[j]:
        m += 1
    else:
        if m > d:
            d = m
        m = 1
        j = i

if m > d:
    d = m

print(len(a) - d)

----------------------------------------------------------------------------------------------
def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    li.reverse()
    i, j, count = 0, 1, 0
    while j < len(li):
        if li[j] < li[i]:
            j += 1
            i += 1
            count += 1
        else:
            j += 1
    print(count)


if __name__ == "__main__":
    main()
----------------------------------------------------------------------------------------------
By bendyna.ivan, contest: Codeforces Round #497 (Div. 1), problem: (A) Reorder the Array, Accepted, #
 n = int(input())
arr = [int(t) for t in input().split()]
arr.sort()

nx = 0
i = 0
res = 0
while i < n:
    j = i
    while j < n and arr[i] == arr[j]:
        j += 1
    nx = max(nx, j)
    t = min(j - i, n - nx)
    nx += t
    nx = min(nx, n)
    res += t
    i = j
print(res)
----------------------------------------------------------------------------------------------