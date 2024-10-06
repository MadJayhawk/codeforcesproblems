# https://codeforces.com/problemset/problem/136/A -  Presents (Difficulty: 700)
#  Start: 11:08  Finish: 11:18  10 minutes  No of submissions: 1

n = int(input())
p = list(map(int, input().split()))
b={}
for indx,i in enumerate(p):
    b[i] = indx+1
c = []
for i in p:
    c.append(str(b[b[i]]))
print(" ".join(c))