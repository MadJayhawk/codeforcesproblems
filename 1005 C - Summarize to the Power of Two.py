#http://codeforces.com/contest/1005/problem/C   Summarize to the Power of Two
def is_power2(num):
	return num != 0 and ((num & (num - 1)) == 0)


n=int(input())
a=list(map(int, input().split()))
d=[]
for i in range(0, n):
    for j in range(i+1, n):
        if is_power2(a[i]+a[j]):
            d.append(a[i])
            d.append(a[j])
s = set(d)
print(len([x for x in a if x not in s]))

DID NOT COMPLETE  TIME_LIMIT_EXCEEDED ON PROBLEM #6
-----------------------------------------------------------------

import collections

int(input())
values = [int(i) for i in input().split()]

li = [2**i for i in range(30, 0, -1)]


ss = collections.Counter(values)

count = 0

for value in values:
    options = []
    for item in li:
        diff = item - value
        if diff < 0:
            break
        options.append(diff)
        print (diff,options)
    for option in options:
        if option in ss and (option != value or ss.get(value, 0) > 1):
            break
    else:
       count += 1

print(count)
-----------------------------------------------------------------
By k0jump, contest: Codeforces Round #496 (Div. 3), problem: (C) Summarize to the Power of Two, Accepted, #
import bisect
n = int(input())
nums = list(map(int,input().split()))
pows = [pow(2,x) for x in range(31)]
dict = {}
for num in nums:
  if num not in dict:
    dict[num] = 1
  else:
    dict[num] += 1

count = 0
for k,v in dict.items():
  count += v
  for i in range(bisect.bisect_right(pows,k),31):
    if (pows[i] - k) in dict:
      if pows[i] == 2*k and v == 1:
        continue
      count -= v
      break
print(count)
-----------------------------------------------------------------
from math import *
dict1={}
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    try:
        dict1[arr[i]]+=1
    except:
        KeyError
        dict1[arr[i]]=1
ans=0
#print(dict1)
for i in range(n):
    flag=0
    for j in range(ceil(log2(arr[i])),32):
        try:
            if(pow(2,j)==2*arr[i]):
                if(dict1[pow(2,j)-arr[i]]>1):
                    flag=1
                    break
            elif(dict1[pow(2,j)-arr[i]]>0):
                flag=1
                break
        except:
            KeyError
    if(flag==0):
        #print(arr[i])
        ans+=1
print(ans)
-----------------------------------------------------------------
from bisect import bisect_right as bs

n=int(input( ))
s=list(map(int, input( ).split( )))
s.sort( )
d=dict( )
for i in range(n):
    try:
        d[s[i]]+=1
    except:
        d.update({ s[i]:1 })
ans=0
d1=dict( )
for i in range(n-1, -1, -1):
    x=len(bin(s[i]))-2
    y=2**x
    dif=abs(y-s[i])
    ind=bs(s, dif)
    if s[ind-1]==dif:
        if s[ind-1]==s[i] and d[s[i]]==1:
            True
        else:
            d1.update({ s[i]:1 })
            d1.update({ s[ind-1]:1 })

for i in range(n):
    try:
        d1[s[i]]
    except:
        ans+=1
print(ans)
-----------------------------------------------------------------
from collections import Counter
z=input()
b=Counter(list(map(int,input().split())))
x=[2**i for i in range(1,31) ]
c=0
for i in b:
    cor=True
    for e in x:
        if b.get(e-i):
            cor = False
            if (e-i)==i and b[e-i]==1:
                cor=True
            else:
                break
    if cor:
        c+=b[i]

print(c)
