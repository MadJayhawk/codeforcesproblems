# https://codeforces.com/problemset/problem/1006/D Two Strings Swaps

DID NOT SUBMIT AN ANSWER

from collections import*
n=int(input())
a,b=input(),input()
c=0
k=n//2
print (a[:k])  # first 2 in a
print(a[::-1])  # reverse of a
print(b)        # all of b
print(b[::-1])  # reverse of b
print(list(zip(a[:k],a[::-1],b,b[::-1])))
for t in zip(a[:k],a[::-1],b,b[::-1]):

 d=Counter(t); l=len(d)
 print(Counter(t),l)

 if l==2 and 1 in d.values():c+=1
 if l==3:c+=1+(t[0]==t[1])
 if l==4:c+=2
 print(c,n%2, a[k]!=b[k],n%2 and a[k]!=b[k])

---------------------------------------------------------------------------------------
By eugalt, contest: Codeforces Round #498 (Div. 3), problem: (D) Two Strings Swaps, Accepted, #
n=int(input())
a,b=input(),input()
k=n//2
c=a[k]!=b[k]and n%2
for u,v,x,y in zip(a[:k],a[::-1],b,b[::-1]):c+=(len({x,y}-{u,v}),u!=v)[x==y]
print(c)
---------------------------------------------------------------------------------------
By Mohamed_Ayman, contest: Codeforces Round #498 (Div. 3), problem: (D) Two Strings Swaps, Accepted, #
 n = int(input())
a = input()
b = input()
res = 0
for i in range(n//2):
    x, y, z, w = a[i], b[i], a[n-i-1], b[n-i-1]
    if (x==y and z==w or x==z and y==w or x==w and y==z):
        continue
    elif (x==y or x==w or z==y or z==w or y==w):
        res+= 1
    else:
        res += 2
if (n%2 == 1):
    if (a[n//2] != b[n//2]):
        res += 1
print(res)
---------------------------------------------------------------------------------------
By ragnar_7, contest: Codeforces Round #498 (Div. 3), problem: (D) Two Strings Swaps, Accepted, #
 n=int(input())
a=list(input())
b=list(input())
temp=[]
count=0
for i in range((n+1)//2):
	#print(count)
	temp=[a[i],b[i],a[n-1-i],b[n-1-i]]
	tems=list(set(temp))
	c=len(tems)
	#print(temp,tems)
	if(c==4):
		count +=2
	elif(c==2):
		if(i==n-1-i):
			count +=1
		elif(temp.count(tems[0])==1 or temp.count(tems[1])==1):
			#if(a[i]!=a[n-i-1]):
			count +=1
	elif(c==3):
		if(a[i]==a[n-1-i]):
			#print(temp,tems)
			count +=2
		elif(b[i]==b[n-1-i]):
			count+=1
		else:
			count +=1
print(count)
---------------------------------------------------------------------------------------
By Myusic, contest: Codeforces Round #498 (Div. 3), problem: (D) Two Strings Swaps, Accepted, #
 n=int(input())
a=input()
b=input()
count=0
for i in range(n//2):
    d={}
    for c in [a[i],a[n-i-1],b[i],b[n-i-1]]:
        d[c]=d.get(c,0)+1
    if a[i]==a[n-i-1]==b[i]==b[n-i-1]:
        continue
    count+=2
    if a[i]==a[n-i-1] and b[i]!=b[n-i-1] and a[i]!=b[i] and a[i]!=b[n-i-1]:
        continue
    for v in d.values():
        if v>=2:count-=1
if n%2==1 and a[n//2]!=b[n//2]:
    count+=1
print(count)
---------------------------------------------------------------------------------------
By
reireg, contest: Codeforces
Round  # 498 (Div. 3), problem: (D) Two Strings Swaps, Accepted, #
from collections import Counter

n = int(input())
a = input()[:n]
b = input()[:n]
prelim = 0
for i in range(n // 2):
    c = Counter([a[i], a[n - 1 - i], b[i], b[n - 1 - i]])
    k = len(c)
    if k == 4:
        """
        a x +2op
        b y
        """
        prelim += 2
    elif k == 3:
        """
        a c  +1op
        a b

        a a  +2op
        b c

        a c  +1op
        b b
        """
        prelim += 2 if a[i] == a[n - 1 - i] else 1
    elif k == 2:
        """
        3 3
        3 5

        3 5
        3 3

        2 5
        2 5
        """
        if 3 in c.values():
            prelim += 1
if n % 2:
    if a[n // 2] != b[n // 2]:
        prelim += 1

print(prelim)
---------------------------------------------------------------------------------------
