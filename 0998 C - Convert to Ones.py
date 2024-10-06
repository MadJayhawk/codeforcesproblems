# http://codeforces.com/contest/998/problem/C
#
# NOT ENTERED -
--------------------------------------------------------------------------------------------
# By pyrus, contest: Codeforces Round #493 (Div. 2), problem: (C) Convert to Ones, Accepted, #
n,x,y=map(int,input().split())
a=input()+'1'
k = a.count('01')
print(0) if k==0 else print ((k-1 ) * min(x, y) + y)
# if k == 0:
# 	print (0)
# else:
# 	print ((k-1 ) * min(x, y) + y)
--------------------------------------------------------------------------------------------
By dvec, contest: Codeforces Round #493 (Div. 2), problem: (C) Convert to Ones, Accepted, #
import re
_, x, y = map(int, input().split())
n = len(re.findall('0+', input()))
print(y + (n - 1) * min(x, y) if n else 0)
--------------------------------------------------------------------------------------------
n,x,y = map(int,input().split())
s = input()
c = 0
f = 0
for i in range(n):
    if(s[i]=='0'):
        if(not f):
            c+=1
            f = 1
    else:
        f = 0
if(c==0):
    print(0)
    exit(0)
ans = y+(c-1)*min(x,y)
print(ans)
--------------------------------------------------------------------------------------------
By F0UR, contest: Codeforces Round #493 (Div. 2), problem: (C) Convert to Ones, Accepted, #
 n, x, y = tuple(map(int, input().split()))
str = input()
num = 0
i = 0
while i < len(str):
    if str[i] == '0':
        j = i + 1
        num += 1
        while j < len(str) and str[j] == '0':
            j += 1
        i = j
    i += 1
if n*'1' == str:
    print(0)
else:
    if x <= y:
        print((num-1)*x+y)
    else:
        print(num*y)
--------------------------------------------------------------------------------------------
By Pr0tick, contest: Codeforces Round #493 (Div. 2), problem: (C) Convert to Ones, Accepted, #
 from math import *
n,x,y=map(int,input().split())
s=str(input())
arr=[]
k=0
for i in s:
    if(i=='0'):
        k+=1
    else:
        if(k==0):
            pass
        else:
            arr.append(k)
        k=0
if(k!=0):
    arr.append(k)
if(y<=x):
    print(len(arr)*y)
else:
    z=x-y
    j=1
    ans=y*len(arr)
    while(j<len(arr)):
        #print((y*len(arr))+(z*j))
        ans=min(ans,(y*len(arr))+(z*j))
        j+=1
    print(ans)
--------------------------------------------------------------------------------------------

