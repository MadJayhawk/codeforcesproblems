#http://codeforces.com/contest/992/problem/B  Nastya Studies Informatics
from math import gcd
# l,r,x,y = map(int,input().split())
x=3
y=30
ans=[]
a=[]
for i in range(1, y + 1):
    if y % i == 0:
        ans.append(i)
        a.append([i,y//i])
print (ans,a)

for i in a: #x is the GCD
    y=i[1]
    x=i[0]

    while y != 0:
        (x, y) = (y, x % y)
        print (i[0],i[1])
    print ('--------',"GCD: ",x)
def lowest_common_denominator(st): #will work for an int array of any length
    lcm = st[0]
    for i in st[1:]:
      lcm = lcm*i//gcd(lcm, i)
    print (st[0],st[1:],'LCD: ',lcm)
for lst in a:
    lowest_common_denominator(lst)
----------------------------------------------------------------
SOLUTIONS
Input
47259 3393570 267 600661890
Answer
30
----------------------------------------------------------------
l,r,x,y=map(int,input().split())
h=()
a=0
if y%x<1:
 y//=x;s=y;l=(l-1)//x+1;r//=x;i=2
 while i*i<=y:
  j=1
  while y%i<1:
   j*=i;y//=i
  if j>1:h+=j,
  i+=1
 if y>1:h+=y,
 for i in range(1<<len(h)):
  p=1
  for j, u in enumerate(h):
   if(i>>j)&1:p*=u
  a+=l<=p<=r and l<=s//p<=r
print(a)
--------------------------------------------------------------

 from math import sqrt,gcd

l,r,x,y=map(int,input().split())
m=x*y
p=int(sqrt(m))
start=(l//x)*x
while start<l:
    start+=x
ans=0
for a in range(start,p+1,x):
    if m%a>0:
        continue
    b=m//a
    if b>r:
        continue
    if gcd(a,b)==x:
        #print(*[a,b])
        ans+=1
        if a!=b:
            ans+=1
print(ans)
--------------------------------------------------------------
import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

l, r, x, y = [int(t) for t in input().split()]
n = y / x
ans = 0
for i in range(1, int(math.sqrt(n)) + 1):
    a = i * x
    b = int(y / i)
    if y % i == 0 and a >= l and b <= r and gcd(a, b) == x:
        ans += (1, 2)[a != b]
print(ans)
----------------------------------------------------------------
import sys

def gcd (a, b):
  if b == 0:
    return a
  return gcd (b, a % b)

l, r, x, y = map (int, input().split())
if y % x != 0:
  print (0)
else:
  res = 0
  p = y // x
  t = 1
  while t * t <= p:
    if p % t == 0:
      a = x * t
      b = x * y / a
      if l <= a <= r and l <= b <= r and gcd (a, b) == x:
        if b != a:
          res += 2
        else:
          res += 1

    t += 1
  print (res)
