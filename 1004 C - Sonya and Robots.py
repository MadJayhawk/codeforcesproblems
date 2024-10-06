#http://codeforces.com/contest/1004/problem/C
n=int(input())
# a= list(map(int,input().split()))
n-=1
b=0
for i in range(n,1,-1):
    b+=i
print(b)



#--------------------------------------------------------
15
1 2 2 1 2 4 2 1 1 6 6 4 2 5 4
Answer
20
#--------------------------------------------------------
By orailly, contest: Codeforces Round #495 (Div. 2), problem: (C) Sonya and Robots, Accepted, #
 input()
d = {}
for x in map(int, input().split()):
    d[x] = len(d)
print(sum(d.values()))
#--------------------------------------------------------
By Hedgehogushka, contest: Codeforces Round #495 (Div. 2), problem: (C) Sonya and Robots, Accepted, #
 n = int(input())
l = [int(el) for el in input().split()]
col = 0
a = [0] * 100001
s = set()
for i in range(n):
    if a[l[i]] == 0:
        col += len(s)
        a[l[i]] += len(s)
        s.add(l[i])
    else:
        col += len(s) - a[l[i]]
        a[l[i]] = len(s)
        s.add(l[i])
print(col)
#--------------------------------------------------------
By vrublack, contest: Codeforces Round #495 (Div. 2), problem: (C) Sonya and Robots, Accepted, #
 n = int(input())
a = [int(x) for x in input().split()]

MAX_NUM = 100010
met_forw = [False] * MAX_NUM
met_backw = [False] * MAX_NUM
unique_n_backw = [0] * n

for i in range(n - 1, -1, -1):
    if i < n - 1:
        unique_n_backw[i] = unique_n_backw[i + 1]
    if not met_backw[a[i]]:
        met_backw[a[i]] = True
        unique_n_backw[i] += 1

answer = 0
for i in range(n - 1):
    if not met_forw[a[i]]:
        met_forw[a[i]] = True
        answer += unique_n_backw[i + 1]

print(answer)
#--------------------------------------------------------
By raj.lath, contest: Codeforces Round #495 (Div. 2), problem: (C) Sonya and Robots, Accepted, #
 noe = int(input())
arr = [int(x) for x in input().split()]
cnt = [0] * int(2e5)
cur = set()
for x in arr:
    cnt[x] = len(cur)
    cur.add(x)
    #print(cnt[:10], cur)
print(sum(cnt))
#--------------------------------------------------------


