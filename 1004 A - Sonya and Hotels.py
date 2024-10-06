#http://codeforces.com/contest/1004/problem/A  Sonya and Hotels
n,d = map(int,input().split())
x= list(map(int,input().split()))
b=[]
c=[]
e=[]
for i in x:
    b.append(i-d)
    b.append(i+d)
    c.append(b)
    b=[]
y=[x for bb in c for x in bb]
z=sorted(y)
for i in range(0,len(z)):
    if y[i]==z[i]:
        e.append(y[i])
v=set(e)
print (len(v))

DID NOT SUBMIT - Ran out of time
-----------------------------------------------------------------------
Input
10 2
-93 -62 -53 -42 -38 11 57 58 87 94
Answer
17
-----------------------------------------------------------------------
By mashot228, contest: Codeforces Round #495 (Div. 2), problem: (A) Sonya and Hotels, Accepted, #
 n, d = map(int, input().split())
X = [-(10**10)] + list(map(int, input().split())) + [10**10]
ans = 0
p = 0
for i in range(1, n + 1):
    if abs(X[i - 1] - (X[i] - d)) > d:
        ans += 1
    if abs(X[i + 1] - (X[i] + d)) > d:
        ans += 1
    if abs(X[i - 1] - (X[i] - d)) == d:
        p += 1
        ans += 1
    if abs(X[i + 1] - (X[i] + d)) == d:
        p += 1
        ans += 1
p = p // 2
ans -= p
print(ans)
-----------------------------------------------------------------------
By itz_me9, contest: Codeforces Round #495 (Div. 2), problem: (A) Sonya and Hotels, Accepted, #
 a=input().split()
n=int(a[0])
d=int(a[1])
b=input().split()
x=[]
count=0
for i in range(len(b)):
	x.append(int(b[i]))
for i in range(len(x)-1):
	if x[i+1]-x[i]>(2*d):
		count=count+2
	if x[i+1]-x[i]==(2*d):
		count=count+1
print(count+2)
-----------------------------------------------------------------------
By SenTinel_LoRd, contest: Codeforces Round #495 (Div. 2), problem: (A) Sonya and Hotels, Accepted, #
 n, d = map(int, input().split())
hotels = list(map(int, input().split()))
count = 2
for i in range(n - 1):
    if (hotels[i + 1] - hotels[i]) / (2 * d) == 1:
        count += 1
    elif (hotels[i + 1] - hotels[i]) / (2 * d) > 1:
        count += 2
print(count)

-----------------------------------------------------------------------
By lraszkiewicz, contest: Codeforces Round #495 (Div. 2), problem: (A) Sonya and Hotels, Accepted, #
 import sys

n, d = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]

res = 2

for i in range(len(x)):
    if i > 0 and abs(x[i] - d - x[i-1]) >= d:
        res += 1
    if i < len(x) - 1 and abs(x[i] + d - x[i+1]) > d:
        res += 1

print(res)

-----------------------------------------------------------------------
