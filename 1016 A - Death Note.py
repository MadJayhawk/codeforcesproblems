#https://codeforces.com/contest/1016/problem/A  Death Note

M = lambda: list(map(int,input().split()))
n, m = M()
a = M()
t = []
s=[]
sm = 0
nex=a[0]

b=0
for i in range(0,len(a)):
    c=b+a[i]
    s.append(c//m)
    b=c%m
print(*s)
