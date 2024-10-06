# http://codeforces.com/contest/1017/problem/A  The Rank

import operator

def sort_list_by_multiple_attributes(y):
    return sorted(y, key = operator.itemgetter(1, 1), reverse=True)

M = lambda: list(map(int,input().split()))

n = int(input())
s = []
for i in range(0, n):
    s.append(sum(M()))
d = sort_list_by_multiple_attributes(list(zip(list(range(1, n+1)), s)))

print([d.index(item) for item in d if item[0] == 1][0]+1)
-----------------------------------------------------------------------------------------------------------
By adjanybekov, contest: Codeforces Round #502 (in memory of Leopoldo Taravilse, Div. 1 + Div. 2), problem: (A) The Rank, Accepted, #
 N = int (input())
Arr1= sum(list(map(int,input().split())))
L=[Arr1]
Res=1
for i in range(N-1):
  Arr= sum(list(map(int,input().split())))
  if(Arr>Arr1):
    Res+=1
print(Res)
-----------------------------------------------------------------------------------------------------------
By .o., contest: Codeforces Round #502 (in memory of Leopoldo Taravilse, Div. 1 + Div. 2), problem: (A) The Rank, Accepted, #
 n = int(input())
a = [sum(map(int, input().split())) for _ in range(n)]
print(sum(v > a[0] for v in a[1:]) + 1)
-----------------------------------------------------------------------------------------------------------
By saku7, contest: Codeforces Round #502 (in memory of Leopoldo Taravilse, Div. 1 + Div. 2), problem: (A) The Rank, Accepted, #
 n = int(input())
j = list(map(int, input().split()))
q = sum(j)
k = 1
for i in range(n - 1):
    x = list(map(int, input().split()))
    y = sum(x)
    if y > q:
        k += 1

print(k)
-----------------------------------------------------------------------------------------------------------
By Emillio, contest: Codeforces Round #502 (in memory of Leopoldo Taravilse, Div. 1 + Div. 2), problem: (A) The Rank, Accepted, #
 n=int(input())
a,b,c,d=map(int,input().split())
s=a+b+c+d
k=1
for i in range(n-1):
    a,b,c,d=map(int,input().split())
    if a+b+c+d>s:
        k+=1
print(k)
-----------------------------------------------------------------------------------------------------------
By kmad1729, contest: Codeforces Round #502 (in memory of Leopoldo Taravilse, Div. 1 + Div. 2), problem: (A) The Rank, Accepted, #
 n = int(input())
results = []
for line_no in range(n):
    l = input()
    s = sum(int(i) for i in l.split(' '))
    results.append((-s, line_no+1))

results.sort()
for rank,r in enumerate(results):
    if r[1] == 1:
        print(rank+1)
        break
-----------------------------------------------------------------------------------------------------------