#http://codeforces.com/contest/1006/problem/0 Adjacent Replacements
n = int(input())
s =  list(map(int, input().split()))
for i in range(0,n-1):
        if s[i]!=s[i+1]:
            if s[i]&1:
                pass
            else:
                s[i]-=1
        else:
            if s[i] & 1:
                pass
            else:
                s[i] -= 1
        if s[i]==100000000:
            s[i]=99999999
if s[n-1]&1:
    pass
else:
    s[n-1]-=1
for i in s:
    print(i,end=" ")
--------------------------------------------------------------------------------------------------
By eugalt, contest: Codeforces Round #498 (Div. 3), problem: (A) Adjacent Replacements, Accepted, #
 input()
print(*(i+i%2-1for i in map(int,input().split())))
--------------------------------------------------------------------------------------------------
By grigorij.shveps, contest: Codeforces Round #498 (Div. 3), problem: (A) Adjacent Replacements, Accepted, #
 n = int(input())
c = list(map(int, input().split()))
for i in range(len(c)):
    if c[i] % 2 == 0:
        c[i] -= 1
print(*c)
--------------------------------------------------------------------------------------------------
By Captainum, contest: Codeforces Round #498 (Div. 3), problem: (A) Adjacent Replacements, Accepted, #
 n = int(input())
a = [int(x) for x in input().split()]
for i in range(n):
    if a[i] % 2 == 0:
        a[i] = a[i] - 1
    else:
        a[i] = a[i]
for i in a:
    print(i, end=" ")
--------------------------------------------------------------------------------------------------
By karth2512, contest: Codeforces Round #498 (Div. 3), problem: (A) Adjacent Replacements, Accepted, #
 n=int(input())
L=list(map(int,input().split()))
for a in range(n):
    if(L[a]%2!=0):
        L[a]+=1
for a in range(n):
    if(L[a]%2==0):
        L[a]-=1
print(' '.join(map(str,L)))
--------------------------------------------------------------------------------------------------
By nigo, contest: Codeforces Round #498 (Div. 3), problem: (A) Adjacent Replacements, Accepted, #
 n = int(input())
a = [int(x) for x in input().split()]

print(*[x - ((x ^ 1) & 1) for x in a])
------------------------
n = int(input())
a = [int(x) for x in input().split()]
s=[]
for x in a:
    print(x^1)
    print((x ^ 1) & 1)
    print(x - ((x ^ 1) & 1))
    print('----------------------')
    s.append(x - ((x ^ 1) & 1))
print(*s)
--------------------------------------------------------------------------------------------------
