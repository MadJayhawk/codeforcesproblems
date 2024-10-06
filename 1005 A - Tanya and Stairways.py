#http://codeforces.com/contest/1005/problem/0
n=int(input())
a=list(map(int,input().split()))
d=[index+1 for index in range(len(a)) if a[index] == 1]
d.append(len(a)+1)
print (a.count(1))
for i in range(0,len(d)-1):
    print(d[i+1]-d[i],end = " ")

ACCEPTED
-------------------------------------------------------------------------------
8
1 2 3 1 2 3 4 5
Answer
2
3 5
------------------------------------------------------------------------------
By larryboy825, contest: Codeforces Round #496 (Div. 3), problem: (A) Tanya and Stairways, Accepted, #
 input()

x = [int(i) for i in input().split()]
a = []

for i in range(len(x)):
    if i == len(x) - 1 or x[i + 1] == 1:
        a.append(x[i])

print(len(a))
print(" ".join([str(x) for x in a]))
----------------------------------------------------------------------------
By Suneet02, contest: Codeforces Round #496 (Div. 3), problem: (A) Tanya and Stairways, Accepted, #
 n = int(input())
a = [int(x) for x in input().split()]
ansL = []; thisIsStart = True
for i in range(n):
    if thisIsStart:
        count = 1
        thisIsStart = False
    else:
        count+=1
    if i != n-1:
        if a[i+1] == 1:
            thisIsStart = True
            ansL.append(count)
    else:
        ansL.append(count)
print(a.count(1))
print(*ansL)
-------------------------------------------------------------------------------
By Stephan_, contest: Codeforces Round #496 (Div. 3), problem: (A) Tanya and Stairways, Accepted, #
 n=int(input())
s=list(map(int,input().split()))
x=s[0]
ans=1
ans1=[]
for i in range(1,n):
    if s[i]!=s[i-1]+1:
        ans+=1
        ans1.append(s[i-1])
ans1.append(s[-1])
print(ans)
for i in ans1:
    print(i,end=" ")
-------------------------------------------------------------------------------



