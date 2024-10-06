#http://codeforces.com/contest/1004/problem/B

#By suyash01, contest: Codeforces Round #495 (Div. 2), problem: (B) Sonya and Exhibition, Accepted, #

n,m=map(int,input().split())
while m:
    l, r=map(int, input( ).split( ))
    m-=1
s='01'*(n//2)
print(s) if n%2==0 else print(s+'0')

DID NOT COMPLETE

#--------------------------------------------------------
6 2
1 6
1 4
Answer
010101
#--------------------------------------------------------
#By anujpathak1996, contest: Codeforces Round #495 (Div. 2), problem: (B) Sonya and Exhibition, Accepted, #
n,m = map(int, input().split())
while(m>0):
    i,j = map(int, input().split())
    m=m-1
s=""
if(n%2==0):
    n=n/2
    while(n>0):
        s=s+"10"
        n=n-1
else:
    n=(n/2)-1
    while(n>0):
        s=s+"10"
        n=n-1
    s=s+"1"
print(s)
#--------------------------------------------------------
#By Mansurbek, contest: Codeforces Round #495 (Div. 2), problem: (B) Sonya and Exhibition, Accepted, #
n,m = map(int,input().split())
for i in range(0,n):
    if i % 2 > 0:
        print(1,end = '')
    else :
        print(0,end = '')
#--------------------------------------------------------
#By m4tx, contest: Codeforces Round #495 (Div. 2), problem: (B) Sonya and Exhibition, Accepted, #
n, d = map(int, input().split())

print(''.join(str(i % 2) for i in range(n)))
#--------------------------------------------------------
n, m = input().split()
n = int(n)
m = int(m)
for i in range(m):
    l, r = input().split()
for i in range(n//2):
    print('01', end='')
if n % 2 != 0:
    print('0')