#http://codeforces.com/contest/994/problem/0
n,m = map(int,input().split())
s=input().split()#[3,4,1,0] #
f=input().split()##
g=set(s)
f=set(f)
b=list(g&f)
for i in s:
    if i in b:
        print (i,end=" ")
---------------------------------------------------------------------------------------
SOLUTIONS
The problem can be solved by iterating over every number of the sequence, then iterating over the sequence of fingerprints to check if the number corresponds to a key with a fingerprint, resulting in an O(n × m) solution.
Input
10 10
1 2 3 4 5 6 7 8 9 0
4 5 6 7 1 2 3 0 9 8
Answer
1 2 3 4 5 6 7 8 9 0
---------------------------------------------------------------------------------------
By dhruvsomani, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (A) Fingerprints, Accepted, #
a, b = input().split()
a, b = int(a), int(b)

arr = list(map(int, input().split()))
a2 = list(map(int, input().split()))

for i in arr:
    if i in a2:
        print(i, end=' ')
---------------------------------------------------------------------------------------
n, m = [int(_) for _ in input().split()]
x1 = [int(_) for _ in input().split()]
x2 = [int(_) for _ in input().split()]
for i in x1:
    if i in x2:
        print(i, end=' ')
---------------------------------------------------------------------------------------
s = input().split()
n, m = int(s[0]), int(s[1])
a = input().split()
b = input().split()
res = ''
for x in a:
    if x in b:
        res+=str(x) + ' '

print(res)
---------------------------------------------------------------------------------------
n, m = map(int, input().split())
x = input().split()
y = input().split()
x = [e for e in x if e in y]
print(' '.join(x))
---------------------------------------------------------------------------------------
n, k = map(int, input().split())
a1=[int(x) for x in input().split()]
a2=[int(x) for x in input().split()]
new=[]
for i in a1:
    if i in a2:
        new.append(i)

print(*new)
---------------------------------------------------------------------------------------
By starternoob, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (A) Fingerprints, Accepted, #
 input()
a=input().split()
b=input().split()
c=[]
for i in a:
    if i in b:
        c.append(i)
print(*c)
