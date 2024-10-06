#http://codeforces.com/contest/998/problem/B
n,b=map(int,input().split())
p=list(map(int,input().split()))
s=[]
for i in range (1,n-1,2):
    d=abs(p[i+1]-p[i])
    s.append(d)
for i in range(0,n-1,2):
    if (p[i]%2 == 0 and p[i+1]%2==0) or (p[i]%2 != 0 and p[i+1]%2!=0):
        print ('0')
    else:
        t=0
        cnt=0
        a=sorted(s,reverse=True)
        ans=0
        for i in a:
            cnt+=1
            t+=i
            if t>b:
                ans=cnt-1
        if t<b: ans=cnt
print (ans)
NOT CORRECT

--------------------------------------------------------------------------------------------
Input
10 10
94 32 87 13 4 22 85 81 18 95
Answer
1
--------------------------------------------------------------------------------------------
By kevin1kevin1k, contest: Codeforces Round #493 (Div. 2), problem: (B) Cutting, Accepted, #
 n, B = list(map(int, input().split()))
a = list(map(int, input().split()))
# print(n, B, a)

oMe = 0
Bs = []
for i in range(n):
    if a[i] % 2 == 0:
        oMe -= 1
    else:
        oMe += 1
    if oMe == 0 and i + 1 != n:
        Bs.append(abs(a[i] - a[i+1]))
Bs = sorted(Bs)
ans = 0
for i in range(len(Bs)):
    if B - Bs[i] >= 0:
        B -= Bs[i]
        ans += 1
print(ans)
--------------------------------------------------------------------------------------------
By pyrus, contest: Codeforces Round #493 (Div. 2), problem: (B) Cutting, Accepted, #
 #!/usr/bin/env python3

[n, B] = map(int, input().strip().split())
ais = list(map(int, input().strip().split()))

c = [0, 0]
cutcost = []
for i in range(n - 1):
	c[ais[i] % 2] += 1
	if c[0] == c[1]:
		cutcost.append(abs(ais[i] - ais[i + 1]))

cutcost.sort()
cnt = 0
for cost in cutcost:
	if cost <= B:
		cnt += 1
		B -= cost

print (cnt)
--------------------------------------------------------------------------------------------
By vg_0617, contest: Codeforces Round #493 (Div. 2), problem: (B) Cutting, Accepted, #
 n,b=map(int,input().split())
l=[int(x) for x in input().split()]
if(n<=3 or n%2!=0):
    print(0)
else:
    l2=[]
    o=0
    e=0
    for i in range(len(l)-2):
        if(l[i]%2==0):
            e+=1
        else:
            o+=1
        if(o==e and o>0):
            l2.append(abs(l[i+1]-l[i]))
    l2.sort()
    sum1=0
    c=0
    for i in range(len(l2)):
        sum1+=l2[i]
        if(sum1<=b):
            c+=1
        else:
            break
    print(c)
--------------------------------------------------------------------------------------------

