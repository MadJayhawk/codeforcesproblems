# http://codeforces.com/contest/998/problem/D  Roman Digits
from itertools import combinations_with_replacement
n=10
num={}
num['I']=1
num['V']=5
num['X']=10
num['L']=50
print(num)
b= (list(combinations_with_replacement(num.keys(), 2)))
print (b)
x = list(zip(*b))
print ('x  ',x)
a=[]
d=[]
for i in x[0]:
        a.append(num[i])
for i in x[1]:
        d.append(num[i])
c=list(zip(a,d))
print (c)
f=[]
for i in c:
    f.append(sum(i))
print (f)

from math import factorial
ggg=factorial(13)/(factorial(10)*12)
print (ggg)
--------------------------------------------------------------------------------------------
By charlieyan, contest: Codeforces Round #493 (Div. 2), problem: (D) Roman Digits, Accepted, #
By Pastafarianist, contest: Codeforces Round #493 (Div. 2), problem: (D) Roman Digits, Accepted, #
a=[0,4,10,20,35,56,83,116,155,198,244]
b=292
n=int(input())
if n<=10:
	print(a[n])
else:
	print(b+(n-11)*49)
--------------------------------------------------------------------------------------------
By bendyna.ivan, contest: Codeforces Round #493 (Div. 2), problem: (D) Roman Digits, Accepted, #
 from collections import defaultdict

n = int(input())

if n > 11:
    print(292 + 49 * (n - 11))
else:
    d = defaultdict(list)
    for L in range(n + 1):
        for X in range(n + 1 - L):
            for V in range(n + 1 - X - L):
                I = n - X - V - L
                s = L * 50 + X * 10 + V * 5 + I
                d[s].append((L, X, V, I))
    print(len(d))
--------------------------------------------------------------------------------------------

By pyrus, contest: Codeforces Round #493 (Div. 2), problem: (D) Roman Digits, Accepted, #
 #!/usr/bin/env python3

n = int(input().strip())

R1 = [4, 9, 49]
# number of distinct number >=T represented using no more than k ROMES-1
def get_after_slow(k, T=0):
	dp = [(k + 1) for _ in range(49*k + 1)]
	dp[0] = 0
	for i in range(1, 49*k + 1):
		for R in R1:
			if i >= R:
				dp[i] = min(dp[i], dp[i - R] + 1)
	return len(dp) - T - dp[T:].count(k + 1)


def get_fast(k):
	if k <= 20:
		return get_after_slow(k)
	else:
		return (k - 19)*49 - 12 + get_after_slow(20, 49)

print (get_fast(n))
--------------------------------------------------------------------------------------------
By Chilli, contest: Codeforces Round #493 (Div. 2), problem: (D) Roman Digits, Accepted, #
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom


N = int(input())
ans = 0
for b in range(9):
    for c in range(9):
        if b+c > N or (b >= 5 and c >= 1):
            continue
        ans += ncr(N-b-c+1, 1)


print(ans)
--------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------


