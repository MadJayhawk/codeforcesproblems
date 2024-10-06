#http://codeforces.com/contest/1003/problem/0
n=int(input())
c=list(map(int,input().split()))
print (max([c.count(x) for x in set(c)]))

ACCEPTED
--------------------------------------------------------------------------------------------
Input
50
7 7 3 3 7 4 5 6 4 3 7 5 6 4 5 4 4 5 6 7 7 7 4 5 5 5 3 7 6 3 4 6 3 6 4 4 5 4 6 6 3 5 6 3 5 3 3 7 7 6
Answer
10
--------------------------------------------------------------------------------------------
By Yee_172, contest: Codeforces Round #494 (Div. 3), problem: (A) Polycarp's Pockets, Accepted, #
 input()
a = input().split()
print(max(a.count(x) for x in a))
--------------------------------------------------------------------------------------------
n=int(input())
a=list(map(int,input().split()))
b=set(a);r=1
for i in b:
    r=max(r,a.count(i))
print(r)
--------------------------------------------------------------------------------------------
input()
arr = str(input()).split(' ')
import collections
c = collections.Counter(arr)
print (c.most_common(1)[0][1])