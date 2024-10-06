# http://codeforces.com/contest/994/problem/B
#     0 3 10 16 14 17 18
n=7
m=1
s=[2,3,4,5,7,8,9]
f=[0,3,7,9,5,8,9]
# n,m = map(int,input().split())
# s=list(map(int,input().split()))
# f=list(map(int,input().split()))
a=dict(zip(s,f))
import copy
maximum=max(a,key=a.get)
c = copy.deepcopy(a)
m=max(a.values())

# for name, age in a.items():    # for name, age in list.items():  (for Python 3.x)
#     if age == 9:
#         print (name)
# print(list(a.keys())[list(a.values()).index(9)])
# del a[list(a.keys())[list(a.values()).index(9)]]
print (a)
for i in range(0,n):
    sm=0
    for j in range(i+1,n):
        print (i,j,"   ",list(a.keys())[j],list(a.keys())[i],a)
        if list(a.keys())[j] > list(a.keys())[i]:
            sm=sm+list(a.values())[i]
    # del a[list(a.keys())[i]]
    # m=sum(a.values())
    print (sm)
    --------------------------------------------------------------------------------------------
    # http://codeforces.com/contest/994/problem/B
n,m = map(int,input().split())
s=list(map(int,input().split()))
f=list(map(int,input().split()))
# n=1
# m=0
# s=[2]
# f=[3]
a=sorted(dict(zip(s,f)).items(),reverse=True)
coins=0
cnt=0
w=dict()
for i in range(0,n):
    coins=a[i][1]
    cnt=0
    for j in range(i+1,n):
        if cnt>=m:
            break
        else:
            cnt+=1
        coins+=a[j][1]
    w[a[i][0]]=coins
for i in s:
    print (w[i],end=" ")
--------------------------------------------------------------------------------------------
Input
7 2
2 4 6 7 8 9 10
10 8 4 8 4 5 9
Answer
10 18 22 26 22 23 27
--------------------------------------------------------------------------------------------
By eugalt, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (B) Knights of a Polygonal Table, Accepted, #
 R=lambda:map(int,input().split())
n,k=R()
r=[0]*n
l=[]
s=0
for _, c, i in sorted(zip(R(),R(),range(n))):
 s+=c;r[i]=s;l=sorted(l+[c])
 if len(l)>k:
  s-=l[0];del l[0]
print(*r)
--------------------------------------------------------------------------------------------
By pyrus, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (B) Knights of a Polygonal Table, Accepted, #
 #!/usr/bin/env python3

from heapq import heappop, heappush

[n, k] = map(int, input().strip().split())
pis = list(map(int, input().strip().split()))
cis = list(map(int, input().strip().split()))

res = [0 for _ in range(n)]
nis = list(range(n))
nis.sort(key=lambda i: pis[i])

hc = []
l = 0
sc = 0

for i in nis:
	sc += cis[i]
	res[i] = sc
	heappush(hc, cis[i])
	if l == k:
		sc -= heappop(hc)
	else:
		l += 1

print (' '.join(map(str, res)))
--------------------------------------------------------------------------------------------
By Knowmyself, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (B) Knights of a Polygonal Table, Accepted, #
 # -*- coding: utf-8 -*-
"""
@Project : CodeForces
@File    : 2.py
@Time    : 2018/6/17 0:27
@Author  : Koushiro
"""

if __name__ == "__main__":
    r_int = lambda: map(int, input().split())
    n, k = r_int()
    knight = list(zip(range(n), r_int(), r_int()))
    result = [0] * n
    knight.sort(key=lambda x: x[1])
    yong = []
    yong_sum = 0
    for i in range(n):
        result[knight[i][0]] = knight[i][2] + yong_sum
        if k == 0:
            continue
        elif len(yong) < k:
            yong.append(knight[i][2])
            yong_sum += knight[i][2]
            yong.sort()
        else:
            if yong[0] < knight[i][2]:
                yong_sum = yong_sum + knight[i][2] - yong[0]
                yong[0] = knight[i][2]
                yong.sort()

    print(" ".join(str(result[i]) for i in range(n)))
--------------------------------------------------------------------------------------------
By snv2, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (B) Knights of a Polygonal Table, Accepted, #
 from heapq import heapify, heappush, heappushpop

n , k = list(map(int , input().split()))

power = list(map(int , input().split()))
coins = list(map(int , input().split()))

knights = [i for i in range(n)]
knights.sort(key=lambda x:power[x])

cursum = 0
curcoin = []
heapify(curcoin)
res = [0] * n
for i in range(min(k,n)):
    res [knights[i]] = cursum +coins[knights[i]]
    heappush(curcoin, coins[knights[i]])
    cursum += coins[knights[i]]

for i in range(min(k,n), n):
    res [knights[i]] = cursum +coins[knights[i]]
    cursum += coins[knights[i]] - heappushpop(curcoin, coins[knights[i]])

print(*res)
--------------------------------------------------------------------------------------------
By sergovoy, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (B) Knights of a Polygonal Table, Accepted, #
 from collections import defaultdict

n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

pairs = {p[i]: c[i] for i in range(n)}
s_p = sorted(pairs.items(), key=lambda x: x[0])

p_ = [k for k, v in s_p]
c_ = [v for k, v in s_p]

for_ans = {el: 0 for el in p}

money = 0
set_ = set()
dict_ = defaultdict(int)
for i in range(min(k + 1, n)):
    money += c_[i]
    for_ans[p_[i]] = money
    set_.add(c_[i])
    dict_[c_[i]] += 1

for i in range(k + 1, n):
    min_ = min(set_)
    set_.add(c_[i])
    dict_[c_[i]] += 1
    dict_[min_] -= 1
    if dict_[min_] == 0:
        set_.remove(min_)
    money += c_[i] - min_
    for_ans[p_[i]] = money

ans = [for_ans[el] for el in p]

print(' '.join(map(str, ans)))
--------------------------------------------------------------------------------------------
By komolakanto, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (B) Knights of a Polygonal Table, Accepted, #
 n, k = list( map( int, input().split()))
p = list( map( int, input().split()))
c = list( map( int, input().split()))

m = {}
for i in range( n ):
    if p[ i ] not in m:
        m[ p[ i ] ] = list()
    m[ p[ i ] ].append( c[ i ] )

a = {}
t = []
for key, val in sorted( m.items() ):
    a[ key ] = sum( t )
    t += val
    t.sort()
    t = t[ max( 0, len( t ) - k ) : len( t ) ]

print( " ".join( [ str( a[ p[ i ] ] + c[ i ] ) for i in range( n )]))
