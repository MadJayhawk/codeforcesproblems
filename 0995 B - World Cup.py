#http://codeforces.com/contest/995/problem/B  World Cup  Rating -1
def run():
    n =int(input())
    a = list(map(int, input().strip().split()))
    allen=0
    i=0# for i in range(0,len(a)):
    bb=True
    while bb==True:
        for k in range(0,n):
            if a[k]==0:
                return k+1
            else:
                for j in range(0,n):
                    if a[j]!=0:a[j]-=1
if __name__ == "__main__":
    print(run())
--------------------------------------------------------
    Input  -  Exceeded Time Limit  No 4
2
483544186 940350702
---------------------------------------------------------
SOLUTION
---------------------------------------------------------
Input
10
3 3 3 5 6 9 3 1 7 3
Answer
7
-----------------------------------------------------------

By ArthurT, contest: Codeforces Round #492 (Div. 2) [Thanks, uDebug!], problem: (B) World Cup, Accepted, #
 input()
queue=list(map(int,input().split()))
t=len(queue)
base=min(queue)
minu=int(base/t)*t
while(queue[minu%t]>minu):
    minu+=1
print(minu%t+1)
---------------------------------------------------------
By eugalt, contest: Codeforces Round #492 (Div. 2) [Thanks, uDebug!], problem: (B) World Cup, Accepted, #
 n=int(input())
a=[x-i for i,x in enumerate(map(int,input().split()))]
m=(min(a)+n-1)//n*n
print(next(i+1 for i in range(n)if a[i]<=m))
---------------------------------------------------------
By pyrus, contest: Codeforces Round #492 (Div. 2) [Thanks, uDebug!], problem: (B) World Cup, Accepted, #
 #!/usr/bin/env python3

n = int(input().strip())
ais = list(map(int, input().strip().split()))

def ceil(a, b):
	return -((-a) // b)

bis = [ceil(ai - i, n) for i, ai in enumerate(ais)]

bmin = min(bis)
ibmin = bis.index(bmin)

print (ibmin + 1)
---------------------------------------------------------
By sergovoy, contest: Codeforces Round #492 (Div. 2) [Thanks, uDebug!], problem: (B) World Cup, Accepted, #
 from math import ceil

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] -= i

for i in range(n):
    a[i] = ceil(a[i] / n)

ans = -1
s = 10 ** 9 + 7

for i in range(n):
    if a[i] < s:
        s = a[i]
        ans = i + 1

print(ans)
---------------------------------------------------------
import math
n = int(input())
a = list(map(int, input().split()))
k = [0] * n
for i in range(n):
    if a[i] > i:
        k[i] = math.ceil((a[i] - i) / n)
    else:
        print(i + 1)
        quit()
m = min(k)
for i in range(n):
    if k[i] == m:
        print(i + 1)
        quit()
# ---------------------------------------------------------
By Zhandos99, contest: Codeforces Round #492 (Div. 2) [Thanks, uDebug!], problem: (B) World Cup, Accepted, #
 import math
n = int(input())
a = list(map(int, input().split()))
s = [0] * n
for i in range (n):

	if a[i] > i:
		s[i] = math.ceil((a[i] - i) / n)
	if a[i] <= i:
		print(i + 1)
		quit()
m = min(s)
for i in range (n):
	if s[i] == m:
		print(i + 1)
		quit()
