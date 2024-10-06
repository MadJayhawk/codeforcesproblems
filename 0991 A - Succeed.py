#http://codeforces.com/contest/991/problem/0
A,B,C,N=map(int,input().split())
F=N-(A+B-C)
if F>0 :
    print (N-(A+B-C))
else:
    print ('-1')
------------------------------------------------------------------
SOLUTIONS
------------------------------------------------------------------
Input
8 3 2 12
Answer
3
------------------------------------------------------------------
a,b,c,n=map(int,input().split())
n-=a+b-c
print((-1,n)[n>0and a>=c<=b])
------------------------------------------------------------------
a,b,c,n=map(int,input().split(' '))
ans=n-(a+b-c)
if ans<=0 or c>a or c>b:
    print(-1)
else:
    print(ans)
--------------------------------------------------------------
a,b,c,n=map(int,input().split())
if a+b-c >= n or a>=n or b>=n or c>a or c>b:
    print(-1)
else:
    print(n-(a+b-c))
-----------------------------------------------------------
a,b,c,n=map(int,input().split())
t=a+b-c
if max(a,b)>n-1 or t>n-1 or t<0 or c>min(a,b):
	print("-1")
else:
	print(n-t)
---------------------------------------------------------------
a,b,c,n=[int(x) for x in input().split()]
l=a+b-c
if a<c or b<c:
    print(-1)
elif l<n:
    print(n-l)
else:
    print(-1)
-----------------------------------------------------------------
a, b, c, d = map(int, input().split())

if a >= c and b >= c :
	if a + b - c < d : print(d + c - a - b)
	else : print(-1)
else : print(-1)
