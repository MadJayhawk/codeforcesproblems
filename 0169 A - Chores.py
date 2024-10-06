# https://codeforces.com/problemset/problem/169/A -  Chores
# Start: 8:52   Finish:  xx   Duration:    Attempts: 4    Difficulty: 900

n, a, b = list(map(int, input().split()))
h = sorted(list(map(int, input().split())))
ans = h[b]-h[b-1]
if ans == 0:
    print(ans)
else:
    print(ans)
---------------------------------------------------------------
a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
tr=[int(x) for x in input().split(" ")]
tr.sort()
print(tr[c]-tr[c-1])
---------------------------------------------------------------
def inp():
    return map(int, input().split())
n,a,b = inp()
h = list(inp())
h.sort()
print(h[b] - h[b-1])
--------------------------------------------------------------
