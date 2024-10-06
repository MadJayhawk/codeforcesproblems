#https://codeforces.com/contest/1016/problem/B  Segment Occurrences

def olpcount(string,pattern):
    l = len(pattern)
    ct = 0
    for c in range(0,len(string)):
        if string[c:c+l] == pattern:
            ct += 1
    return ct

M = lambda: list(map(int,input().split()))
n, m,q= M()
s ='a'*10000 #input()
t = 'aa'#input()
u=[]
for i in range(0,q):
    l,r = M()
    u.append([l,r])
for l,r in u:
    if t in s[l-1:r]:
        print(olpcount(s[l-1:r],t))
    else:
        print(0)
------------------------------------------------------------------------------------------------------
By sergovoy, contest: Educational Codeforces Round 48 (Rated for Div. 2), problem: (B) Segment Occurrences, Accepted, #, hack it!
 from itertools import accumulate
from sys import stdin

all_in = list(el.rstrip('\n') for el in stdin.readlines())

n, m, q = map(int, all_in[0].split())
s = all_in[1]
t = all_in[2]
l_r = [tuple(map(int, el.split())) for el in all_in[3:]]

in_ = [int(t == s[i: i + m]) for i in range(n - m + 1)]
acc = [0] + list(accumulate(in_))

ans = list()
for a, b in l_r:
    if b - a + 1 < m:
        ans.append(0)
        continue

    ans.append(acc[max(0, b - m + 1)] - acc[a - 1])

print('\n'.join(map(str, ans)))
------------------------------------------------------------------------------------------------------
By qLethon, contest: Educational Codeforces Round 48 (Rated for Div. 2), problem: (B) Segment Occurrences, Accepted, #, hack it!
 n, m, q = [int(i) for i in input().split()]
S = input()
T = input()
A = [[int(i) for i in input().split()] for j in range(q)]

s = []

for i in range(len(S)):
    if S[i:i+len(T)] == T:
        s.append(1)
    else:
        s.append(0)

csum = [0]
for s_ in s:
    csum.append(csum[-1] + s_)

for a, b in A:
    print(csum[max(a-1, b-len(T)+1)] - csum[a-1])
------------------------------------------------------------------------------------------------------
By mvs2667, contest: Educational Codeforces Round 48 (Rated for Div. 2), problem: (B) Segment Occurrences, Accepted, #, hack it!
 n,m,q=map(int,input().split(" "))
s=input()
t=input()
o=""
for i in range(0,n-m+1):
    if s[i:i+m]==t:
        o+="1"
    else:
        o+="0"
for i in range(0,q):
    l,r=map(int,input().split(" "))
    if r-l+1>=m:
       print(o[l-1:r-m+1].count("1"))
    else:
        print("0")
------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------

