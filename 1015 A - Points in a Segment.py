# http://codeforces.com/contest/1015/problem/A  Points in a Segment
M = lambda: list(map(int,input().split()))

n, m = M()
e=[]
a=[0]*(m+1)
for i in range(n):
    l,r = M()
    for j in range (l,r+1):
        a[j]=1
for i in range(1,m+1):
        if a[i]:
            pass
        else:
            e.append(i)
print(len(e))
print(*e)
--------------------------------------------------------------------------------------------------------
By happy_New_Year, contest: Codeforces Round #501 (Div. 3), problem: (A) Points in Segments, Accepted, #, hack it!
n, m = map(int, input().split())
a = [0]*(m+1)
for i in range(n):
    l, r = map(int, input().split())
    while l!=r+1:
        a[l] = 1
        l+=1

print(a.count(0)-1)
for i in range(1,m+1):
    if a[i]==0:
        print(i, end = ' ')
--------------------------------------------------------------------------------------------------------
By dilipsobindar, contest: Codeforces Round #501 (Div. 3), problem: (A) Points in Segments, Accepted, #, hack it!
n,m = input().split()
n = int(n)
m = int(m)


ints = []
for i in range(1,m+1):
    ints.append(i)
for i in range(0,n):
    l,r = input().split()
    l = int(l)
    r = int(r)
    for i in range(l,r+1):
        if i in ints:
            ints.remove(i)

if len(ints)==0:
    print("0")
else:
    print(len(ints))
    for i in ints:
        print(i,end = " ")
--------------------------------------------------------------------------------------------------------
By avtahovfarit, contest: Codeforces Round #501 (Div. 3), problem: (A) Points in Segments, Accepted, #, hack it!
 n, m = list(map(int, input().split()))
a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
ans = []
for i in range(1, m + 1):
    boo = 0
    for j in a:
        if j[0] <= i and j[1] >= i:
            boo = 1
    if not boo:
        ans.append(i)
print(len(ans))
print(*ans
--------------------------------------------------------------------------------------------------------